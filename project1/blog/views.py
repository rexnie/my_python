from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
from blog.models import Employee

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def whoami(self):
        return "in whoami()," + self.name




# Create your views here.
'''
def index(req):
    return HttpResponse('<h1>hello</h1>')
'''

'''
def index(req):
    t = loader.get_template('index1.html')
    c = Context({})
    return HttpResponse(t.render(c))
'''

def index(req):
    user = { 'name':'niedaocai', 'age':22, 'sex':'male' }
    user1 = Person('huangling',23,'female')
    book_list = ["java", "python", "c++"]
    return render_to_response('index1.html', {'string':'print a string', 'user':user, 'user1':user1, "book_list":book_list}
        )

def indexdb(req):
    ''' insert a record to table:
    #methold 1
    obj1 = Employee(name = "nie")
    obj1.save()

    #methold 2
    obj2 = Employee()
    obj2.name = "dao"
    obj2.save()

    #methold 3
    Employee.objects.create(name = 'cai')
    '''

    emps = Employee.objects.all()
    return render_to_response('indexdb.html', {'emps':emps})
