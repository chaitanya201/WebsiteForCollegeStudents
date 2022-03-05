from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.db import models

import home
from .models import Data_register, Assignments, Answers

from login_system.forms import Model_register, Sign
from login_system.models import Data_register

# admin stuff
""""

def admin_upload_profile(request):
    if request.method=='POST':
        profilephoto=request.FILES
        user=Data_register(profile_photo=profilephoto)
        user.save()
        return render(request,'profile.html')
    else:
        return render(request,'profile.html')

def admin_upload_pan(request):
    if request.method=='POST':
        panimage=request.FILES
        user=Data_register(pancard=panimage)
        user.save()
        return render(request,'profile.html')
    else:
        return render(request,'profile.html')

"""
""""
def admin_upload_timetable(request):
    if request.method=='POST':
        adharimage=request.FILES.get('admin_timetable')
        user=Data_register(adhar_card=adharimage)
        user.save()
        return render(request,'profile.html')
    else:
        return render(request,'profile.html')
"""


def admin_login_page(request):
    if request.method == 'POST':
        data = AuthenticationForm(request=request, data=request.POST)
        if data.is_valid():
            # global UNAME # it's scope is now global.
            UNAME = data.cleaned_data[
                'username']  # username is the name of field where data is stored in the form(AuthenticationForm)
            upassword = data.cleaned_data[
                'password']  # if you run the server and press the "control+u" then in the name field you will see)# that the data entered in the username and password is stored in "username" and "password" fields.
            user = authenticate(username=UNAME,
                                password=upassword)  # this function checks that the entered username and password are in the database in or not.
            if user is not None:
                login(request, user)
                n_user = User.objects.get(username=UNAME)
                print('This is first name ', n_user.first_name, 'this is user id ', n_user.id)
                all_data = Data_register.objects.all()
                admin = User.objects.get(username=UNAME)
                admin_id = admin.id

                que = Assignments.objects.all()
                print(all_data, 'this is all data')
                return render(request, 'profile.html',
                              {'name': n_user.first_name, 'data': all_data, 'admin_id': admin_id, 'que': que})
            else:
                user_form = AuthenticationForm()
                return render(request, 'user login.html', {'error': 'enter valid username and password'},
                              {'form': user_form})
        else:
            user_form = AuthenticationForm()
            return render(request, 'user login.html', {'error': 'enter valid data'}, {'form': user_form})

    else:
        user = AuthenticationForm()
        return render(request, 'user login.html', {'form': user})


''''
def register(request):
    if request.method == 'POST':
        user_f_name = request.POST['first_name']
        user_l_name = request.POST['last_name']
        user_user_name = request.POST['user_name']
        user_pass = request.POST['Password']
        user_c_pass = request.POST['Confirm_Password']
        user_email = request.POST['Email']
        if user_pass == user_c_pass :
            if User.objects.filter(username=user_user_name).exists():
                print("user name is taken")
                redirect("register/register")
            elif User.objects.filter(email=user_email):
                print("email is already taken")
                redirect("register/register")
            else:
                user = User.objects.create_user(first_name=user_f_name, last_name=user_l_name,  username=user_user_name, email=user_email, password=user_pass)
                user.save();
                print('hii',user_f_name)
                return render(request, "login.html")
        else:
            return render(request,"regestrion.html",{'error':'password not matched'})

    else:
        return render(request,"regestrion.html")
'''


def timetabel(request):
    last_user = User.objects.all().last()


def index(request):
    return render(request, 'index1.html')

def contact(request):
    return render(request,'contact.html')


def profile(request, ):
    all_data = Data_register.objects.all()
    print(all_data, 'this is all data')
    return render(request, 'profile.html', {'data': all_data})  # ,{'name':UNAME}) # uname is a global variable.


""""''''
def register(request):
    if(request.method=="POST"):
        filled_form= Model_register(request.POST)
        if(filled_form.is_valid()):   # is_valid() is checks the deatails entered in the form are correct or not.
            first_name=filled_form.cleaned_data['first_name'] # here the first_name is from forms file
            last_name=filled_form.cleaned_data['last_name']
            user_name=filled_form.cleaned_data['user_name']
            email=filled_form.cleaned_data['Email']
            password=filled_form.cleaned_data['Password']
            confirm_password=filled_form.cleaned_data['Confirm_Password']

            if(password==confirm_password):
               if user_name not in Data_register.objects.all():
                   if email not in Data_register.objects.all():
                       store_data = Data_register(first_name=first_name, last_name=last_name, Email=email,
                       user_name=user_name, Password=password,
                       Confirm_Password=confirm_password)
                       store_data.save()
                       return redirect(login_page)
                   else:
                       return render(request,'Student register.html',{'error':"this email is already taken .."})
               else:
                   return render(request,'Student register.html',{"error":"username is already taken by someone"})
            else:
                return render(request,'Student register.html',{"error":"Please enter the same password.."})
        else:
            return render(request,'Student register.html',{"error":"data is invalid"})

    else:
        blank_form= Model_register()
        return render(request,'Student register.html',{'form':blank_form})


def new_register(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        user = Sign(request.POST)
        if user.is_valid():
            user.save()
            return redirect(index)
        else:
            return render(request,'Register.html',{'error':'enter valid details'})
    else:
        user=Sign()
        return render(request,'Register.html',{'form':user})
''' """


# this is the simplest code for saving the data into the database.

def register(request):
    if request.method == 'POST':
        user_f_name = request.POST['first_name']
        user_l_name = request.POST['last_name']
        user_user_name = request.POST['user_name']
        user_pass = request.POST['Password']
        user_c_pass = request.POST['Confirm_Password']
        user_email = request.POST['Email']
        if user_pass == user_c_pass:
            if Data_register.objects.filter(user_name=user_user_name).exists():
                print("user name is taken")
                return render(request, 'regestrion.html', {'error': 'Username is already taken'})
            elif Data_register.objects.filter(Email=user_email).exists():
                print("email is already taken")
                return render(request, 'regestrion.html', {'error': 'Email is already taken by someone'})
            else:
                user = Data_register(first_name=user_f_name, last_name=user_l_name, user_name=user_user_name,
                                     Email=user_email, Password=user_pass)
                user.save();
                print('Hii', user_f_name)
                return render(request, "login.html")
        else:
            return render(request, "regestrion.html", {'error': 'Password not matched'})

    else:
        return render(request, "regestrion.html")


# user stuff regarding the upload
""""
def upload_pan(request):
    if request.method ==login 'POST' and request.FILES:
        pan = request.FILES.get("panisuploaded")
        user = Data_register(id=user_id,pancard=pan)
        user.save(update_fields=['pancard'])
        if user.pancard:
            u_pancard=user.pancard
        else:
            u_pancard=None
        if user.adhar_card:
            u_adhar=user.adhar_card.url
        else:
            u_adhar=None
        if user.profile_photo:
            u_profile=user.profile_photo.url
        else:
            u_profile=None

        return render(request, 'panCard.html',{'pan_abc':u_pancard})#{'name':u_name,'u_pancard':u_pancard,'u_adhar': u_adhar, 'u_profile': u_profile,})
                     # {'u_adhar': u_adhar, 'u_pancard': u_pancard, 'u_profile': u_profile}
    else:
        all_objects = Data_register.objects.filter(user_name=uname)
        for obj in all_objects:
            if obj.id==user_id:
                u_adhar=obj.adhar_card.url
                u_pancard=obj.pancard
                u_profile = obj.profile_photo.url
        #print("this is from pan card",u_adhar, u_profile, u_pancard)
        return render(request, 'student profile.html',{'name':u_name,'u_adhar':u_adhar,'u_pancard':u_pancard,'u_profile':u_profile})
"""

# do not delete this:
""""
def upload_adhar(request):
    if request.method == 'POST' and request.FILES:
        adhar = request.FILES.get("adarisuploaded")
        user = Data_register(id=user_id, adhar_card=adhar)
        user.save(update_fields=['adhar_card'])
        if user.pancard:
            u_pancard = user.pancard.url
        else:
            u_pancard = None
        if user.adhar_card:
            u_adhar = user.adhar_card.url
        else:
            u_adhar = None
        if user.profile_photo:
            u_profile = user.profile_photo.url
        else:
            u_profile = None
        return render(request, 'adharCard.html',{'adhar_user':u_adhar})#{'name':u_name,'u_adhar':u_adhar, 'u_pancard': u_pancard, 'u_profile': u_profile})
    else:
        for obj in Data_register.objects.filter(user_name=uname):
            if obj.id == user_id:
                u_adhar = obj.adhar_card.url
                u_pancard = obj.pancard.url
                u_profile = obj.profile_photo.url
            # print("this is from pan card",u_adhar, u_profile, u_pancard)
        return render(request, 'student profile.html',
                          {'name': u_name, 'u_adhar': u_adhar, 'u_pancard': u_pancard, 'u_profile': u_profile})

"""


def upload_pan(request, id):
    if request.method == 'POST' and request.FILES:
        pan = request.FILES.get("panisuploaded")
        user = Data_register(id=id, pancard=pan)
        user.save(update_fields=['pancard'])
        print('Pan is uploaded')
        if user.pancard:
            u_pancard = user.pancard.url
        else:
            u_pancard = None

        return render(request, 'panCard.html', {'pan_abc': u_pancard,
                                                'id': id})  # {'name':u_name,'u_pancard':u_pancard,'u_adhar': u_adhar, 'u_profile': u_profile,})
        # {'u_adhar': u_adhar, 'u_pancard': u_pancard, 'u_profile': u_profile}
    else:
        all_objects = Data_register.objects.filter(id=id)
        for obj in all_objects:
            if obj.id == id:
                u_pancard = obj.pancard
                print(u_pancard, 'else part of pan card')
        # print("this is from pan card",u_adhar, u_profile, u_pancard)
        return render(request, 'student profile.html', {
            'u_pancard': u_pancard})  # ,{'name':u_name,'u_adhar':u_adhar,'u_pancard':u_pancard,'u_profile':u_profile})


def view_adhar(request, id):
    if request.session['key']:
        for obj in Data_register.objects.filter(id=id):
            if obj.id == id:
                u_adhar = obj.adhar_card.url
        print(u_adhar, 'else part of the adhar card')
        return render(request, 'adharCard.html', {'adhar_user': u_adhar, 'id': id})
    else:
        return render(request, 'login.html', {'error': 'First Login '})


def view_pan(request, id):
    if request.session['key']:
        for obj in Data_register.objects.filter(id=id):
            if obj.id == id:
                u_pan = obj.pancard.url
        print(u_pan, 'pan card !!!!!!!!!!!')
        return render(request, 'panCard.html', {'pan_abc': u_pan, 'id': id})
    else:
        return render(request, 'login.html', {'error': 'First Login '})


def front(request, id):
    user = Data_register.objects.get(id=id)
    u_profile = user.profile_photo.url
    u_name = user.first_name
    return render(request, 'front.html', {'name': u_name, 'u_profile': u_profile, 'id': id})


def log_out(request):
    # logout(request)
    # print(request.session['key']) # we can give any value insted of 'key'
    # del request.session['key']
    print('Loging OUT!!!!!')
    return render(request, 'index1.html')


def upload_adhar(request, id):
    if request.method == 'POST' and request.FILES:
        adhar = request.FILES.get("adarisuploaded")
        user = Data_register(id=id, adhar_card=adhar)
        user.save(update_fields=['adhar_card'])

        if user.adhar_card:
            u_adhar = user.adhar_card.url
            print(u_adhar)
        else:
            u_adhar = None

        return render(request, 'adharCard.html', {'adhar_user': u_adhar,
                                                  'id': id})  # {'name':u_name,'u_adhar':u_adhar, 'u_pancard': u_pancard, 'u_profile': u_profile})
    else:
        for obj in Data_register.objects.filter(id=id):
            if obj.id == id:
                u_adhar = obj.adhar_card.url
        print(u_adhar, 'else part of the adhar card')
        return render(request, 'adharCard.html', {'adhar_user': u_adhar, 'id': id})


def upload_profile(request, id):
    if request.method == 'POST' and request.FILES:

        u_profile = request.FILES.get("profileisuploaded")
        user = Data_register(id=id, profile_photo=u_profile)
        user.save(update_fields=['profile_photo'])
        n_user = Data_register.objects.get(id=id)
        u_name = n_user.first_name
        # u_name = user.first_name
        print('first name is ', u_name)
        if user.profile_photo:
            u_profile_up = user.profile_photo.url
        else:
            u_profile_up = None
        return render(request, 'front.html', {'name': u_name, 'u_profile': u_profile_up,
                                              'id': id})  # {'u_adhar': u_adhar, 'u_pancard': u_pancard, 'u_profile': u_profile}
    else:
        for obj in Data_register.objects.filter(id=id):
            if obj.id == id:
                u_name = obj.first_name
                u_profile = obj.profile_photo.url
            # print("this is from pan card",u_adhar, u_profile, u_pancard)
        return render(request, 'student profile.html',
                      {'name': u_name, 'u_profile': u_profile})


def edit_profile(request, id):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        uname = request.POST['username']
        password = request.POST['password']
        user = Data_register(first_name=fname, last_name=lname, Email=email, Password=password, user_name=uname, id=id)
        user.save(update_fields=['first_name', 'last_name', 'Password', 'Email', 'user_name'])
        return render(request, 'update details.html',
                      {'success': 'Details are updated successfully!!!!!!!', 'id': id, 'test': 1})

    else:
        user_data = Data_register.objects.get(id=id)
        return render(request, 'update details.html', {'id': id, 'user_data': user_data})


# user stuff......
"""
def user_login(request):
    if request.method=='POST':
        uname=request.POST['username']
        upassword=request.POST['password']
        if Data_register.get_user(uname):
            if Data_register.get_password(upassword):
                panc=Data_register.get_pan(uname)
                adar=Data_register.get_adhar(uname)
                photo=Data_register.get_photo(uname)
                print(uname,upassword,panc,adar)
                return render(request,'student profile.html',{"pan_card":panc,"name":uname,"adhar_card":adar,"profi_photo":photo})
            else:
                return render(request, 'login.html', {"error":"Password does not match"})
        else:
            return render(request, 'login.html', {"error": 'Username is not exist'})

    else:
        return render(request,'login.html')
"""


def user_login(request):
    if request.method == 'POST':
        global uname, upass, user_id
        global user_id
        uname = request.POST['username']
        upass = request.POST['password']
        search_password = Data_register.objects.filter(Password=upass)
        if Data_register.objects.filter(user_name=uname):
            if search_password:
                for obj in Data_register.objects.filter(user_name=uname):
                    if obj.user_name == uname:
                        u_name = obj.first_name
                        global user_id
                        user_id = obj.id
                        # u_adhar=obj.adhar_card.url
                        # u_pan=obj.pancard.url
                        u_profile = obj.profile_photo.url
                        # find out how to use login method.
                        # creating an user object
                        # u_object=obj
                # u_object=Data_register.objects.get(user_name=uname)
                # login(request,u_object)
                request.session['key'] = uname
                if uname:
                    print("user id is : ", user_id)
                    return render(request, 'front.html', {'name': u_name, 'u_profile': u_profile,
                                                          'id': user_id})  # ,{'name':u_name,'u_adhar':u_adhar,'u_pancard':u_pan,'u_profile':u_profile})
                else:
                    return render(request, 'front.html', {'error': 'you are not logged in!!'})

            else:
                return render(request, 'login.html', {"error": 'Username or password is not exist'})
        else:
            return render(request, 'login.html', {"error": 'Username or password is not exist'})

    else:
        return render(request, 'login.html')


def delete_user(request, id):
    user = Data_register(id=id)
    user.delete()
    all_data = Data_register.objects.all()

    return render(request, 'profile.html', {'data': all_data})


def update_user(request, id, admin_id):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['user_name']
        email = request.POST['Email']
        password = request.POST['Password']
        user = Data_register(id=id, first_name=fname, last_name=lname, Email=email, user_name=uname, Password=password)
        user.save(update_fields=['first_name', 'last_name', 'Email', 'user_name', 'Password'])
        return render(request, 'update.html',
                      {'success': 'Profile Is upadated successfully!!!', 'id': id, 'admin_id': admin_id})
    else:
        user = Data_register.objects.get(id=id)
        print(user.first_name, user.last_name, user.Email, user.Password)
        return render(request, 'update.html',
                      {'id': id, 'fname': user.first_name, 'lname': user.last_name, 'admin_id': admin_id,
                       'email': user.Email, 'password': user.Password, 'username': user.user_name})


def add_user(request):
    if request.method == 'POST':
        user = Sign(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            print("in if ")
            print(User.objects.filter(username=request.POST['username']).exists() , " is user exists")
            print(user.is_valid(), " is form data is valid ")
            print(request.POST['username'], " username")
            print(request.POST['password1'], " password")
            print(request.POST['first_name'], " first name")
            print(request.POST['email'], " email")
            if User.objects.filter(username=request.POST['username']).exists():
                print("user name is taken")
                form = Sign()
                return render(request, 'add user.html', {'form': form, 'msg': 'Username is alrady taken'})


            else:
                user = User.objects.create_superuser(username=request.POST['username'],
                                                     password=request.POST['password1'],
                                                     first_name=request.POST['first_name'],
                                                     last_name=request.POST['last_name'], email=request.POST['email'])
                print(user, 'this is user')
                print()
                print()
                print("user has created")
                print()
                form = Sign()
                return render(request, 'add user.html', {'form': form, "msg": "User is created successfully!!!"})


        else:
            form = Sign()
            return render(request, 'add user.html', {'form': form, "msg": "Password Not Matched"})
    else:
        form = Sign()
        return render(request, 'add user.html', {'form': form})


def show_and_upload_questions(request):
    pass


def add_que(request, admin_id):
    if request.method == 'POST':

        ques1 = request.FILES.get('que1')
        user = Assignments(questions=ques1, admin_id=admin_id)
        user.save()
        que = Assignments.objects.all()
        all_data = Data_register.objects.all()
        user1 = User.objects.get(id=admin_id)
        name = user1.first_name
        print(name, 'all_dataad')
        all_questions = Assignments.objects.filter(admin_id=admin_id)
        all_answers = Answers.objects.filter(question=user.id)
        all_students = Data_register.objects.all()
        return render(request, 'admin see questions.html',
                      {'name': name, 'que': que, 'admin_id': admin_id, 'all_questions': all_questions, 'all_answers':all_answers,'all_students':all_students})
    else:

        user = User.objects.get(id=admin_id)
        name = user.first_name
        print(name, 'this is the name', admin_id, 'this is admin is')

        all_questions = Assignments.objects.filter(admin_id=admin_id)
        all_answers = Answers.objects.all()
        all_students= Data_register.objects.all()
        return render(request, 'admin see questions.html',
                      {'all_questions': all_questions, 'admin_id': admin_id, 'name': name,'all_answers':all_answers,'all_students':all_students})


def add_marks(request,id,que_no,admin_id):
    if request.GET['mark']:
        old_user = Answers.objects.get(student_id=id, question=que_no)
        user_id=old_user.id
        old_ans=old_user.answer
        new_user=Answers(marks=request.GET['mark'],id=user_id,student_id=id,answer=old_ans,question=que_no)
        new_user.save()
    user = User.objects.get(id=admin_id)
    name = user.first_name
    all_questions = Assignments.objects.filter(admin_id=admin_id)
    print('all questions are   ',all_questions)
    print()
    print()
    print()
    all_answers = Answers.objects.all()
    all_students = Data_register.objects.all()
    return render(request, 'admin see questions.html',
                  {'all_questions': all_questions, 'admin_id': admin_id, 'name': name, 'all_answers': all_answers,
                   'all_students': all_students})



def delete_question(request, admin_id, question):
    print('question id is ', question)
    print()

    que = Assignments(id=question)
    que.delete()
    print('question is deleted successfully!!!')
    return redirect('que', admin_id=admin_id)


def admin_back(request, admin_id):
    user = User.objects.get(id=admin_id)
    name = user.first_name
    data = Data_register.objects.all()
    return render(request, 'profile.html', {'admin_id': admin_id, 'name': name, 'data': data})


def upload_answers(request, id, que,admin_id):
    if request.method == 'POST':
        ans = request.FILES.get('ans')
        if Answers.objects.filter(student_id=id, question=que):
            old_ans = Answers.objects.get(student_id=id, question=que)
            old_id = old_ans.id
            user = Answers(answer=ans, question=que, student_id=id,id=old_id)
            user.save()
            print('answer is updated successfully')
            ques = Assignments.objects.filter(admin_id=admin_id)
            answers = Answers.objects.filter(student_id=id)
            return render(request, 'upload answers.html',
                          {'id': id, 'que': que, 'questions': ques, 'answers': answers,'admin_id':admin_id})

        user = Answers(answer=ans, question=que, student_id=id)
        user.save()
        print('answer is saved successfully..')

        ques = Assignments.objects.filter(admin_id=admin_id)
        answers = Answers.objects.filter(student_id=id)
        return render(request, 'upload answers.html', {'id': id, 'que': que, 'questions': ques, 'answers': answers,'admin_id':admin_id})
    else:
        answers = Answers.objects.filter(student_id=id)
        ques = Assignments.objects.filter(admin_id=admin_id)
        return render(request, 'upload answers.html', {'id': id, 'que': que, 'questions': ques, 'answers': answers,'admin_id':admin_id})
