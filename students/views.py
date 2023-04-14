from django.shortcuts import render
from .models import Student, Teacher
from django.http import HttpResponse
from django.db import connection
from django.db.models import Q # To run more complex quries
# Create your views here.
################## 2ST (OR) ########################
def student_list_1(request):
    post = Student.objects.all() # To get all objects
    
    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

def student_list_2(request):
    post = Student.objects.filter(surname__startswith='Mohane') | Student.objects.filter(surname__startswith='Jhod')# To filter from objects
    
    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

def student_list_3(request):
    post = Student.objects.filter(Q(surname__startswith='Mohane') | Q(surname__startswith='Jhod') | ~Q (surname__startswith='Jhod'))# To filter from objects ~Q is querie that is not in (!=)
    
    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

################# 3nd (AND) #####################

def student_list_4(request):
    post = Student.objects.filter(classroom=12) & Student.objects.filter(firstname__startswith='Shivam')# To filter from objects
    
    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

def student_list_5(request):
    post = Student.objects.exclude(classroom=12) & Student.objects.filter(firstname__startswith='Shivam')# To filter from objects by exclude
    
    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

def student_list_(request):
    post = Student.objects.filter(Q(classroom=12) & Q(age=17)) # To filter from objects ~Q is querie that is not in (!=)
    
    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

########### 4th (UNION) ###############

def student_list_(request):
    
    post = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname'))# Gives list 

    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

def student_list_(request):
    
    post = Student.objects.all().values('firstname').union(Teacher.objects.all().values('firstname')) # Give dict 

    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')


################### 5th (NOT) ########################

def student_list_(request):
    
    post = Student.objects.exclude(firstname='shivam') 
    
    # gt greater than
    # gte greater then or equals to
    # lt less then
    # lte less then or equal to
    # eg: age__gt = 19

    print(post)
    print(post.query)
    print(connection.queries)
    
    
    return HttpResponse('Ok')

def student_list_(request):
    
    post = Student.objects.filter(~Q(age__gt = 19))

    print(post)
    print(post.query)
    print(connection.queries)
    
    return HttpResponse('Ok')

#################### 6th(SELECT and OUTPUT) ###############

def student_list_(request):
    
    post = Student.objects.filter(classroom = 12).only('firstname', 'age')
    print(post)
    print(post.query)
    print(connection.queries)
    
    return HttpResponse('Ok')

############################ 7th(RAW) #########################

def student_list_(request):
    
    post = Student.objects.all()
    
    for s in  Student.objects.raw("SELECT * FROM  students_student WHERE age=17"):
        print(s)
    print(post)
    print(post.query)
    print(connection.queries)
    
    return HttpResponse('Ok')

def student_list_(request):
    
    # post = Student.objects.all()
    
    sql = "SELECT * FROM  students_student WHERE age=17"
    
    post=  Student.objects.raw(sql)[:2]  #limit
    print(post)
    print(post.query)
    print(connection.queries)
    
    return HttpResponse('Ok')

################ 8th (Custom SQL) Simple BYpassing ORM ############

def student_list(request):
    
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM students_student")
    r = cursor.fetchone()
    print(r)
    print(connection.queries)
    
    return HttpResponse('Ok')

