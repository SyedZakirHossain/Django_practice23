
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

# Create your models here.

class stu(models.Model):
    n=models.CharField(max_length=50,null=True)
    c=models.CharField(max_length=50,null=True)
    r=models.CharField(max_length=50,null=True)
    photo=models.ImageField(null=True,blank=True,)
    father=models.CharField(max_length=50,null=True)
    mother=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    guardian=models.CharField(max_length=50,null=True)
    mobile=models.IntegerField(default=0,null=True)
    imergency=models.IntegerField(default=0,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    b=models.IntegerField(default=0,null=True)
    e=models.IntegerField(default=0,null=True)
    s=models.IntegerField(default=0,null=True)
    m=models.IntegerField(default=0,null=True)
    tm=models.IntegerField(default=0,null=True)
    grade=models.CharField(max_length=10,null=True)
    
    def total(self):
          b=0
          e=0
          m=0
          s=0
          tm=self.b +self.e +self.s +self.m 
          grade='PASS' 
          return tm   
        
          
    def grade(self):
            b=0
            e=0
            m=0
            s=0
            tm=self.b +self.e +self.s +self.m 
            grade=''
            if tm >= 200:
                  
                  grade = 'PASS'
                  
            else:
                  grade='FAIL' 
            return grade
                  
class Contact(models.Model):
       name=models.CharField(max_length=50,null=True)
       email=models.EmailField(max_length=50,null=True) 
       desc=models.TextField(max_length=5000,null=True)
       
class Homework(models.Model):
       name=models.CharField(max_length=50,null=True)
       clas=models.CharField(max_length=50,null=True)
       roll=models.IntegerField(default=0,null=True) 
             
       desc=models.TextField(max_length=5000,null=True)     
             
                             
class Notice(models.Model):
      title=models.CharField(max_length=50,null=True)
      date=models.DateTimeField() 
      content=models.FileField(upload_to="notice/",null=True,default=None)        
      desc=models.TextField(max_length=5000,null=True)     


class User(models.Model):
            name=models.CharField(max_length=50,null=True)        
            email=models.EmailField(max_length=50,null=True)      
            password1=models.CharField(max_length=50,null=True)  
            password2=models.CharField(max_length=50,null=True)  
            
            
class Student(models.Model):
            user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
            name=models.CharField(max_length=50,null=True)        
            _clas=models.CharField(max_length=50,null=True)
            roll=models.IntegerField(default=0,null=True)    
 
class Teacher(models.Model):
            user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
            name=models.CharField(max_length=50,null=True)        
            email=models.EmailField(max_length=50,null=True)                
            