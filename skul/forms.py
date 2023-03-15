from django import forms
from skul import models


from .models import User


class stud(forms.ModelForm):
    class Meta:
        model = models.stu
        fields ="__all__"
        
class Homework(forms.ModelForm):
    class Meta:
        model = models.Homework
        fields ="__all__"
        
class Contact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields ="__all__"        
class User(forms.ModelForm):
    class Meta:
        model = models.User
        fields ="__all__"   
