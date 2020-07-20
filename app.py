from flask import Flask,render_template,request, redirect, flash, url_for, session, g

import logic as logic

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adminlogin',methods=['POST'])
def adminlogin():
    
    uname = request.form['uname']
    pwd = request.form['pwd']
    if request.method == 'POST':
        if uname!='admin' or pwd != 'admin':
            print("SUCCSSES")
            return redirect(url_for('index'))
        else:
            session['username'] = 'admin'
            return redirect(url_for('admin'))


@app.route('/admin')
def admin():
    if 'username' in session:
        res = fo.product_list()
        return render_template('AdminAfterLogin.html' , res = res)
    else:
        return redirect(url_for('error'))

@app.route('/adminlogout')
def AdminLogout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/addcourse')
def AdminAddCourse():
    if 'username' in session:
        return render_template('AddCourse.html')
    else:
        return redirect(url_for('error'))

@app.route('/addcoursebackend' , methods = ['POST'])
def AddCourseBackend():
    name = request.form['cname']
    des = request.form['cdes']
    if fo.add_course(name,des):
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('addcourse'))

@app.route('/updatedelete')
def updatedelete():
    if 'username' in session:
        res = fo.list_course()
        return render_template('update_delete.html' , res = res)
    else:
        return redirect(url_for('error'))
        
@app.route('/delete/<id>')
def deleteCourse(id):
    if 'username' in session:
        if(fo.delete_course(id)):
            return redirect(url_for('admin'))
        else:
            return render_template(url_for('updatedelete'))
    else:
        return redirect(url_for('error'))

@app.route('/updatecourse/<id>')
def updatecourse(id):
    res = fo.update_course_details(id)
    return render_template('update.html' , res = res)

@app.route('/updatecoursebackend/<id>' , methods = ['POST'] )
def updateBackend(id):
    name = request.form['cname']
    des = request.form['cdes']
    if fo.update_backend_course(id,name,des):
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('updatedelete'))

@app.route('/adminviewcourse')
def adminViewcourse():
    res = fo.user_usn()
    return render_template('admincourseview.html' , res = res)

@app.route('/signup')
def signup():
    return render_template('create_user.html')

@app.route('/CreateAccount' , methods = ['POST'])
def create_account():
    name = request.form['name']
    pnumber = request.form['usn']
    sname = request.form['sem']
    address = request.form['pnum']
    uname = request.form['uname']
    pwd = request.form['pwd']
    if(fo.create_account(name,usn,sem,pnum,uname,pwd)):
        flash("Account Created Successfully!")
        return redirect(url_for('index'))
    else:
        flash("Account Creation Failed!")
        return redirect(url_for('signup'))

@app.route('/login' , methods = ['POST'] )
def student_login():
    uname = request.form['uname']
    pwd = request.form['pwd']
    res = fo.user_checking(uname)
    r = res.split('|')
    if r[4]!=uname and pwd!=r[5]:
        return redirect(url_for('index'))
    else:
        session['usn'] = r[1]
        return redirect(url_for('user'))

@app.route('/user')
def user():
    if 'usn' in session:
        res = fo.list_course()
        return render_template('userAfterLogin.html' , res = res , name = session['usn'])
    else:
        return redirect(url_for('error'))

@app.route('/addtolist/<usn>' , methods = ['POST'])
def addToList(usn):
    id = request.form['cid']
    if fo.add_to_list(id,usn):
        return redirect(url_for('user'))
    else:
        return redirect(url_for('user'))

@app.route('/userlogout')
def userLogout():
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.secret_key = "yoyo"
    app.run(port=7777,debug=True)
    