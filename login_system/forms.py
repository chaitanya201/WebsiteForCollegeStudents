# creating forms here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
# this creates a form which have following fields first_name,last_name,Email,etc....
"""""
class Registration_form(forms.Form):
    first_name = forms.CharField(max_length=50 )
    last_name = forms.CharField(max_length=50)
    user_name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=15)
    Confirm_Password = forms.CharField(max_length=15)
"""
# now i am creating a form using ModelForm
# this form is inherited from the model class.
class Model_register(forms.ModelForm):
    class Meta:  # Meta class is predefined class and it is compulsory
        model=Data_register # Data_register is model class name

        # fields contains a list of fileds which would be displayed on the screen.
        # list items are from the Model Class in Model file.
        # displayed form has attribute in same order as in fields list if list items are interchanged then
        # the order will also change in the form.
        fields=["first_name","last_name","user_name","Email","Password","Confirm_Password"]
# fiels is a predefined attribute which takes

# if you want to change the names of the fields at the output then use "labels" dictionary
# key name is field name and value is name you like to give at the output form.
        labels={'first_name':'Enter First name',
                'last_name':'Enter Last name',
                'user_name':'Enter Username',
                'Password':'Enter Password',
                }

# for errors use "error_messages" dictionary
# key is the value of the field and value is another dictionary which contains the error message.
# if you want to give another erorr in email then give it in the second dic
# again same key is error name and value is what message you want to print.

#error_messages = {'Email': {'required': 'enter the first name here','new error msg':'what you want to print'}}

        error_messages={'Email':{'required':'enter the first name here'},#for more erorr messages in same field another key(error name) and value(error mesage) is given in the respective dictionary
                        'Password':{'required':'enter correct password'}}
# widgets
# we can give the widgets to form from here.
# attrs is a dictionary which takes the HTML attributes and render on the screen.
        widgets={'Password':forms.PasswordInput(attrs={'placeholder':'Enter Password'}),
                 'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
                 'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
                 #'Email':forms.EmailField(attrs={'placeholder':'Enter Valid Email ID'}),
                 'user_name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter username'}),
                 'Confirm_Password':forms.PasswordInput(attrs={'class':'myclass','placeholder':'Confirm Password'})
                 }


# python manage.py runserver

# creating sign up form using django built in form
# first inheriting the UserCreationForm in Sign class so that we can make changes in the sign up form.
class Sign(UserCreationForm):
    # below code is for overwritten the UserCreationForm fields
    # here only above Meta we can overwrite the code
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)#password2 is confirm password in the UserCreationForm
    class Meta:
        model=User  # is a built in model in Django
        fields=['first_name','last_name','email','username']
        labels = {'first_name': 'Enter First name',
                  'last_name': 'Enter Last name',
                  'username': 'Enter Username',
                  'password': 'Enter Password',
                  'confirmpassword': 'confirm Password',
                  }
        widgets={'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
                 'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
                 'username': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Username'}),

                 }

