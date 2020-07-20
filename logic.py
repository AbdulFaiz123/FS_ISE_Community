import uuid
import os,glob
# glob is for retrieve files/pathnames matching  glob.globr(wherver)
print("happy")

def create_account(name,usn,sem,pnum,uname,pwd):
    data = name +'|'+ usn +'|'+ sem +'|'+ pnum +'|'+ uname +'|'+ pwd +'$'
    fp = open("files/user.txt",'a')
    fp.write(data)
    fp.close()
    return True


def add_event(name,des,date):
    id = str(uuid.uuid4())
    id = id[:5]
    fp = open("files/event.txt",'a')
    data = str(id) +'|'+ name +'|'+ des + '|'+date +'$'
    fp.write(data)
    fp.close()
    return True

def list_event():
    fp = open("files/event.txt","r")
    file = fp.read()
    fp.close()
    res = file.split('$')
    li = []
    for r in res:
        data = r.split('|')
        li.append(data)
    li.pop()
    return li

def delete_event(id):
    fp = open("files/event.txt","r")
    file = fp.read()
    fp.close()
    res = file.split('$')
    li = []
    for r in res:
        if r.startswith(id):
            continue
        else:
            li.append(r)
    data = '$'.join(li)
    fp = open("files/event.txt","w")
    fp.write(data)
    fp.close()
    return True



def update_event_details(id):
    fp = open('files/event.txt','r')
    data = fp.read()
    li = []
    res = data.split('$')
    for r in res:
        if r.startswith(id):
            data =r.split('|')
            li.append(data[0])
            li.append(data[1])
            li.append(data[2])
        else:
            continue
    return li

def update_backend(id,name,des,date):
    fp = open('Files/event.txt','r')
    data = fp.read()
    fp.close()
    li = []
    res = data.split('$')
    for r in res:
        if r.startswith(str(id)):
            continue
        else:
            li.append(r)
    li.pop()
    st = id + '|' + name + '|' + des + '|' + date + '$'
    li.append(st)
    final_r = '$'.join(li)
    fp = open('Files/event.txt','w')
    fp.write(final_r)
    fp.close()
    return True

# course

def add_course(name,des):
    id = str(uuid.uuid4())
    id = id[:5]
    fp = open("files/course.txt",'a')
    data = str(id) +'|'+ name +'|'+ des +'$'
    fp.write(data)
    fp.close()
    return True




def list_course():
    fp = open("files/course.txt",'r')
    data = fp.read()
    fp.close()
    li = []
    res = data.split("$")
    for r in res:
        li.append(r)
    li.pop()
    return li
res = list_course()
print(res)

def delete_course(id):
    fp = open("files/course.txt","r")
    file = fp.read()
    fp.close()
    res = file.split('$')
    li = []
    for r in res:
        if r.startswith(id):
            continue
        else:
            li.append(r)
    data = '$'.join(li)
    fp = open("files/event.txt","w")
    fp.write(data)
    fp.close()
    return True

def update_course_details(id):
    fp = open('files/course.txt','r')
    data = fp.read()
    li = []
    res = data.split('$')
    for r in res:
        if r.startswith(id):
            data =r.split('|')
            li.append(data[0])
            li.append(data[1])
            li.append(data[2])
        else:
            continue
    return li

def update_backend_course(id,name,des):
    fp = open('Files/course.txt','r')
    data = fp.read()
    fp.close()
    li = []
    res = data.split('$')
    for r in res:
        if r.startswith(str(id)):
            continue
        else:
            li.append(r)
    li.pop()
    st = id + '|' + name + '|' + des + '$'
    li.append(st)
    final_r = '$'.join(li)
    fp = open('Files/course.txt','w')
    fp.write(final_r)
    fp.close()
    return True


# def choose_course(course):
#     fp = open("files/course.txt",'r')
#     data =fp.read()
#     fp.close()
#     res = data.split("$")
#     li = []
#     for r in res:
#         if course == r:
#             li.append(r)
#         else:
#             return False
#         return li


def write_feedback(fd):
    data = fd +'$'
    fp = open("files/feedback.txt",'a')
    fp.write(data)
    fp.close
    return True

def feedback_list():
    fp = open("files/feedback.txt",'r')
    data = fp.read()
    fp.close()
    res = data.split('$')
    li = []
    for r in res:
        li.append(r)
    li.pop()
    return li

def add_to_list(cid,usn):
    fp = open('Files/course.txt','r')
    data = fp.read()
    fp.close()
    data1 = ''
    res = data.split('$')
    for r in res:
        if r.startswith(cid):
            l = r.split('|')
            data1 = cid + '|' + l[1] + '|' + l[2] + '$'
        else:
            continue
    if data1 != '':
        fname = usn + '.txt'
        fp = open(fname,'a')
        fp.write(data1)
        fp.close()
        return True
    else:
        return False


def user_usn():
    li = []
    for file in glob.glob("*.txt"):
        li.append(file)
    li2 = []
    for l in li:
        r = l.split('.')
        li2.append(r[0])
    return li2

def user_checking(uname):
    fp = open('Files/users.txt','r')
    data = fp.read()
    fp.close()
    res = data.split('$')
    for r in res:
        l = r.split('|')
        if l[4] == uname:
            return r
        else:
            continue
    return 'NO'

# if __name__ == "__main__":
#     ch = int(input("enter the choice"))


        


    
            




