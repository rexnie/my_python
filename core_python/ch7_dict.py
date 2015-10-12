#!/usr/bin/env python
import os
import time

""" userpw """
db = {}
def newuser():
    prompt = "login desired:"
    while True:
        name = raw_input(prompt)
        #if name in db:
        if db.has_key(name):
            prompt = "name taken,try another"
            continue
        else:
            break
    pwd = raw_input("password:")
    db[name] = pwd

def olderuser():
    name = raw_input("login:")
    pwd = raw_input("passwd:")
    passwd = db.get(name)
    if passwd == pwd:
        print "welcome back"
    else:
        print "login error"

def viewdb():
    for key in db.keys():
        print key,db[key]

def userpw():
    prompt = """
    (N)ew user login
    (E)xisting user login
    (V)iew
    (Q)uit
    Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt),reason:
                print reason
                choice = 'q'
            if choice not in "nqev":
                print "choice error,try again"
            else:
                chosen = True

        if choice == 'q':
            done = True
        elif choice =='n':
            newuser()
        elif choice =='v':
            viewdb()
        else:
            olderuser()
""" end of userpw """

""" userpw2 """
# {key,[password,last_login_timestamp]}
db2 = {}

def viewdb2():
    for key in db2.keys():
        tt = time.localtime(db2[key][1])
        print "%-10s%-10s%02d/%02d/%02d/ %02d:%02d:%02d" %(key,db2[key][0],tt.tm_year,tt.tm_mon,tt.tm_mday,tt.tm_hour,tt.tm_min,tt.tm_sec)

def deleteuser():
    dname = raw_input("name you want to delete").strip().lower()
    if dname in db2.keys():
        del db2[dname]
    else:
        print "there is no %s in db2" % dname

def userLogin():
    name = raw_input("input login name:").strip().lower()
    if name in db2.keys():
        pwd = raw_input("passwd:")
        passwd = db2.get(name)[0]
        if passwd == pwd:
            print "welcome back,last login@",db2[name][1]
            db2[name][1] = time.time()
        else:
            print "passwd error"
    else:
        print "You are new here,please register"
        prompt = "enter name:"
        while True:
            name = raw_input(prompt).strip().lower()
            if db2.has_key(name):
                prompt = "name taken,try another"
                continue
            else:
                break
        pwd = raw_input("password:").strip()
        db2.setdefault(name,[pwd,time.time()])

def userpw2():
    prompt = """
    (L)ogin
    (D)elete user account
    (V)iew
    (Q)uit
    Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            if choice not in "ldvq":
                print "choice error,try again"
            else:
                chosen = True

        if choice == 'q':
            done = True
        elif choice =='l':
            userLogin()
        elif choice =='v':
            viewdb2()
        else:
            deleteuser()
""" end of userpw2 """

def dict_sorted():
    week={'Sun':'w7','Mon':'w1','Tue':'w2','Wen':'w3','Thur':'w4','Fri':'w5','Sat':'w6',}
    print week
    print 'sort with key:'
    for k in sorted(week):
        print k,week[k]
    print 'sort with value:'
    for k,v in sorted(week.items(), key=lambda e:e[1],reverse=True):
        print k,v

if __name__ == "__main__":
    #userpw()
    #userpw2()
    dict_sorted()
