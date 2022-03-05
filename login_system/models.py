from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data_register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.TextField(max_length=50)
    Email = models.EmailField()
    Password = models.TextField(max_length=20)
    Confirm_Password = models.TextField(max_length=20)
    adhar_card=models.FileField(default=0,upload_to='profile')
    pancard=models.FileField(default=0,upload_to='profile')
    profile_photo=models.FileField(default=0,upload_to='profile')
    def __str__(self):
        return self.first_name



class Assignments(models.Model):
    questions=models.FileField(upload_to='All Assignments',null=True,blank=True)
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.questions.url

class Answers(models.Model):
    answer=models.FileField(upload_to='All Answers',null=True,blank=True)
    question=models.IntegerField(null=True,blank=True)
    marks=models.IntegerField(null=True,blank=True)
    student=models.ForeignKey(Data_register,on_delete=models.CASCADE)
    def __str__(self):
        return self.answer






"""
    

    def get_password(self):
        return Data_register.objects.filter(Password=self)

    def get_pan(self):
        pan=Data_register.objects.get(user_name=self)
        return pan.pancard.url

    def get_adhar(self):
        pan=Data_register.objects.get(user_name=self.user_name)
        return pan.adhar_card.url


    def get_photo(self):
        pan=Data_register.objects.get(user_name=self)
        return pan.profile_photo.url
        
    def get_user(self):
        return self.user_name
    
        def __str__(self):
        return self.first_name

"""









# if model field has attribute blank=True then this field is not necessary during form filling.