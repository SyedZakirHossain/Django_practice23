from django.contrib import admin
from .models import stu,Contact,Homework,Notice,User
from django.contrib.auth.forms import User

##from .models import Student
#from .models import Subject



class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','n','c','r','photo','b','e','s','m','total','grade','father','mother','guardian','address','mobile','imergency','bloodgroup',)
admin.site.register(stu,ServiceAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('pk','name','email','desc',)
admin.site.register(Contact,ContactAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display=('pk','name','clas','roll','desc',)
admin.site.register(Homework,HomeworkAdmin)



class NoticeAdmin(admin.ModelAdmin):
    list_display=('pk','title','date','desc','content',)
admin.site.register(Notice,NoticeAdmin)

