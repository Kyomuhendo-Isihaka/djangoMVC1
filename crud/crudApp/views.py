from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import Student,Account

# Create your views here.
def account_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            account = None

        if account and password== account.password:
            return redirect('home') 

    return render(request, 'login.html')    

def account_signup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        date = request.POST.get('date')
        password = request.POST.get('password')

        account = Account.objects.create(username=username, email=email, birthdate=date, password=password)
        account.save()
        return redirect(account_login)

    return render(request, 'signup.html') 

def home(request):
    students = Student.objects.all()
    if request.method == "POST":
        std_name = request.POST.get('stdName')
        std_age = request.POST.get('stdAge')
        std_course = request.POST.get('stdCourse')

        student = Student.objects.create(stdName=std_name, stdAge=std_age, stdCourse=std_course)
        student.save()
    
    return render(request, 'index.html', {'students':students})

# updating 
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.stdName = request.POST.get('stdName')
        student.stdAge = request.POST.get('stdAge')
        student.stdCourse = request.POST.get('stdCourse')
        student.save()
        return redirect(home)
    return render(request, 'pages/student-edit.html', {'std' : student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect(home)