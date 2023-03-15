import io
import json
import os
import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.http import (FileResponse, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from skul import forms
from .models import Contact,stu,Homework,Notice


# Create your views here.


#=========================================================

def about(request):
          
     data={ 
           'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022', 
         'title' :'Home Page, Welcome To todo page.' ,
         'bdata':'I am a full stack developer.',
         'sublist':['Bangla','English','Mathematics','Science'],
         'number':[10,20,30,40,50,60,70],
         'student_details':[
           {'name':'Raya','roll':1,'class':'Seven','Bangla':70,'English':100,'Mathematics':100,'Science':100},
           {'name':'Maya','roll':2,'class':'Seven','Bangla':70,'English':100,'Mathematics':100,'Science':100}, 
           {'name':'kayo','roll':3,'class':'Six','Bangla':70,'English':100,'Mathematics':100,'Science':100}  
         ],
           }   
     return render(request,'about.html',data)
#=========================================================   
def add(request):
    return render(request,'add.html')
     
#=========================================================   
def addsave(request):
    try:                    
        if  request.method=="POST":
                n=request.POST['n']
                r=request.POST['r']
                c=request.POST['c']  
                b=request.POST['b']
                e=request.POST['e']
                m=request.POST['m']
                s=request.POST['s']
                father=request.POST['father']
                mother=request.POST['mother']
                guardian=request.POST['guardian']  
                address=request.POST['address']
                mobile=request.POST['mobile']
                imergency=request.POST['imergency']
                bloodgroup=request.POST['bloodgroup']
                values=stu(n=n,r=r,c=c,b=b,e=e,m=m,s=s,bloodgroup=bloodgroup,imergency=imergency,mobile=mobile,address=address,guardian=guardian,mother=mother,father=father,)
                values.save();  
                messages.info(request,'Information saved and add to database. ')
    except:
        pass
    return redirect('/add')
                                        
#=========================================================
  
"""def about2(request):
            
    return render(request,'about2.html')
"""     
#=========================================================  



def admit(request):
        r= stu.objects.all()
        dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
        return render (request,'admit.html',context=dict)
 #=========================================================
def contact(request):
         return render(request,'contact.html')
#=========================================================

def contactsave(request):
        try: 
            if request.method=="POST":
                name=request.POST['name']
                email=request.POST['email']
                desc=request.POST['desc'] 
                values=Contact(name=name,email=email,desc=desc,)
                values.save();  
                messages.info(request,'Your message is saved and added to database. ')
        except:
            pass    
        return redirect('/contact')
            
#=========================================================
 
def enter2(request):
    cap=request.POST.get("captha")
                                  
                        
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =auth.authenticate(username=username,password=password)          
        if  str(cap)!=str_num :
            return HttpResponse("<h4>Error captha</h4>") 
        if user is not None:
            auth.login(request,user) 
            return redirect('/userhome') 
        else:  
            messages.info(request,'Invalid credentials') 
            #return render(request,'login.html') 
            return redirect('/login')
            
                
                
    else:  
        messages.info(request,'Invalid credentials') 
        return render(request,'/login')            
                        
#=========================================================
def home(request):
        #return render(request,'home.html')
        #return HttpResponse('Hello Bangladesh')
    data={ 
           'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022', 
           'title' :'Home Page, Welcome To todo page.' ,
           'bdata':'I am a full stack developer.',
           'sublist':['Bangla','English','Mathematics','Science'],
           'number':[10,20,30,40,50,60,70],
         
           }   
    return render(request,'home.html',data)
             
#=========================================================  
def homework(request):
         return render(request,'homework.html')
#=========================================================

def homeworksave(request):
        try: 
            if request.method=="POST":
                    name=request.POST['name']
                    clas=request.POST['clas']
                    roll=request.POST['roll']
                    
                    desc=request.POST['desc'] 
                    values=Homework(name=name, clas=clas, roll=roll,desc=desc,)
                    values.save();  
                    messages.info(request,'Your homework is saved and added to database. ')
        except:
            pass    
        return redirect('/homework')
 
#=========================================================
    
def login(request):
    num=random.randrange(11212,98998)
    global str_num
    str_num=str(num)
    return render(request,"login.html",{"img":str_num})
    #return render(request,'login.html')  
 #========================================================= 
          
def logout(request):
            
  return render(request,'logout.html') 


#=========================================================

def login_page(request):
    return render(request,'logout.html')  

#=========================================================  
def notice(request):
        n= Notice.objects.all()
        dict={'notice':n,'skul':'Barishal Zilla School',
            'exam':'Annual Examination 2022',}
               
        return render(request,'notice.html',context=dict)
            
        
    
    
    
    
#=========================================================
def notice_PDF(request):
     buf = io.BytesIO()
     c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
     textob=c.beginText()
     textob.setTextOrigin(inch,inch)
     textob.setFont("Helvetica",14)
     #lines = ["line 1",
             # "line 2",
             # "line 3",]
     r= Notice.objects.all()
     lines =[]
     for notice in r:
         lines.append("=============  ")
         lines.append('Title')
         lines.append(notice.title) 
         lines.append("Date")      
         lines.append(notice.date)
         lines.append('Description')   
         lines.append(notice.desc) 
          
                                     
     for line in lines:
           textob.textLine(line)
           
     c.drawText(textob)
     c.showPage()
     c.save()
     buf.seek(0)
           
     return FileResponse(buf,as_attachment=True,filename='Notice.pdf')

#=========================================================


 #=========================================================
  
def Print_PDF(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        p = canvas.Canvas(response)

        p.drawString(200, 100, "Some text in first page.")
        p.showPage()

        p.drawString(300, 100, "Some text in second page.")
        p.showPage()

        p.drawString(600, 100, "Some text in third page")
        p.showPage()

        p.save()
        return response 
  
#=========================================================
                 

def register(request):
    if request.method =='POST':
          username = request.POST['username']
          email = request.POST['email']   
          password1 = request.POST['password1']
          password2 = request.POST['password2']  
          
          if password1==password2:
                if User.objects.filter(username=username).exists():
                      messages.info(request,'Username taken')
                      return redirect('/register')
                elif User.objects.filter(email=email).exists():
                     messages.info(request,'Email taken')
                     return redirect('/register')
                else:     
                    user = User.objects.create_user(username=username,password=password1,email=email)
                    user.save();
                    messages.info(request,'user created')
                    return redirect('/login')
          else:
                messages.info(request,'Password not matching')
                return redirect('/register')
                #return redirect('/')
    else:            
          return render(request,'register.html') 
  
#=========================================================

def register2(request):
            
    return render(request,'register.html')   
 #=========================================================   
 
 #=========================================================
   
def result(request):
    student_list=stu.objects.all()
    name=(request.POST.get('name'))
    roll=(request.POST.get('roll'))
    s_class=(request.POST.get('s_class')) 
        
    b1=(request.POST.get('b'))
    e1=(request.POST.get('e'))
    m1=(request.POST.get('m'))
    s1=(request.POST.get('s'))
    #tm=(request.POST.get('tm'))
    tm=0
    #tm=b1+e1+m1+s1
    val=tm
    grade='A'
    try:
        if request.method=="POST":
            name=(request.POST.get('name'))
            roll=(request.POST.get('roll'))
            s_class=(request.POST.get('s_class'))  
            b1=(request.POST.get('b'))
            e1=(request.POST.get('e'))
            m1=(request.POST.get('m'))
            s1=(request.POST.get('s'))
            tm=b1+e1+m1+s1
            val=tm
            grade='A'
    except:
      pass   
    
    
            
    dict={'st':student_list,'skul':'Barishal Zilla School',
            'exam':'Annual Examination 2022','b':b1,'e':e1,'s':s1,'m':m1,'name':name,'roll':roll,'s_class':s_class,'tm':val,'grade':grade,}
    
    #student_list=students.objects.order_by(name)  
    return render(request,'result.html',context=dict,)
  #=========================================================
def report_pdf(request):
     buf = io.BytesIO()
     c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
     textob=c.beginText()
     textob.setTextOrigin(inch,inch)
     textob.setFont("Helvetica",14)
     #lines = ["line 1",
            ##V  "line 2",
            #  "line 3",]
     r= stu.objects.all()
     lines =[]
     for admit in r:
         lines.append("=============  ")
         lines.append('Admit Card')
         lines.append("Class:")      
         lines.append(admit.c)
         lines.append('Name')   
         lines.append(admit.n) 
         lines.append("Roll:")
         lines.append(admit.r)  
                                     
     for line in lines:
           textob.textLine(line)
           
     c.drawText(textob)
     c.showPage()
     c.save()
     buf.seek(0)
           
     return FileResponse(buf,as_attachment=True,filename='Admit.pdf')

#=========================================================

def rscw(request):
            
    return render(request,'rscw.html') 
  
#=========================================================
def stlcw(request):
            
    return render(request,'stlcw.html') 
  
#=========================================================
#=========================================================
def studentlist_pdf(request):
     buf = io.BytesIO()
     c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
     textob=c.beginText()
     textob.setTextOrigin(inch,inch)
     textob.setFont("Helvetica",14)
     #lines = ["line 1",
            ##V  "line 2",
            #  "line 3",]
     r= stu.objects.all()
     lines =[]
     for admit in r:
         lines.append("--------------------------  ")
         #lines.append('Admit Card')
         #lines.append("Class:")      
         #lines.append(admit.c)
         #lines.append('Name')   
         lines.append(admit.n) 
         #lines.append("Roll:")
         #lines.append(admit.r)  
                                     
     for line in lines:
           textob.textLine(line)
           
     c.drawText(textob)
     c.showPage()
     c.save()
     buf.seek(0)
           
     return FileResponse(buf,as_attachment=True,filename='Student List.pdf')

#=========================================================

def studentlist_pdf(request):
     buf = io.BytesIO()
     c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
     textob=c.beginText()
     textob.setTextOrigin(inch,inch)
     textob.setFont("Helvetica",14)
     #lines = ["line 1",
            ##V  "line 2",
            #  "line 3",]
     r= stu.objects.all()
     lines =[]
     for admit in r:
         lines.append("--------------------------  ")
         #lines.append('Admit Card')
         #lines.append("Class:")      
         #lines.append(admit.c)
         #lines.append('Name')   
         lines.append(admit.n) 
         #lines.append("Roll:")
         #lines.append(admit.r)  
                                     
     for line in lines:
           textob.textLine(line)
           
     c.drawText(textob)
     c.showPage()
     c.save()
     buf.seek(0)
           
     return FileResponse(buf,as_attachment=True,filename='Student List.pdf')

#=========================================================

  
def stulist(request):
    r= stu.objects.all()
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
    return render (request,'studentList.html',context=dict)

#=========================================================
 
def stulist2(request):
        r= stu.objects.all().order_by('c')
        dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
        return render (request,'studentlist2.html',context=dict) 


#=========================================================
def studentlist2_pdf(request,student_id):
        buf = io.BytesIO()
        c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
        textobj=c.beginText()
        textobj.setTextOrigin(inch,inch)
        textobj.setFont("Helvetica",14)
     #lines = ["line 1",
            ##V  "line 2",
            #  "line 3",]
        r= stu.objects.get(pk=student_id)
        lines =[]
        for admit in r:
            lines.append("--------------------------  ")
            #lines.append('Admit Card')
            lines.append("Class:")      
            lines.append(admit.c)
            lines.append('Name')   
            lines.append(admit.n) 
            lines.append("Roll:")
            lines.append(admit.r)  
            lines.append("Bangla:")      
            lines.append(admit.b)
            lines.append('Engllish')   
            lines.append(admit.e) 
            lines.append("Science:")
            lines.append(admit.s)
            lines.append("Mathematics:")
            lines.append(admit.m)     
                                      
        for line in lines:
              textobj.textLine(line)
            
        c.drawText(textobj)
        c.showPage()
        c.save()
        buf.seek(0)
            
        return FileResponse(buf,as_attachment=True,filename='Student List.pdf')
 #=========================================================

#=========================================================


# Class wise student  list  class six
def stlc6(request,):
    r= stu.objects.all().filter(c='Six')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Six',}
    # dictionary={'student_info':stu}
    return render (request,'stl6.html',context=dict)
#=========================================================
# Class wise student list class  seven
def stlc7(request,):
    r= stu.objects.all().filter(c='Seven')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Seven',}
    # dictionary={'student_info':stu}
    return render (request,'stl7.html',context=dict)
#=========================================================
# Class wise student list class  eight
def stlc8(request,):
    r= stu.objects.all().filter(c='Eight')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Eight',}
    # dictionary={'student_info':stu}
    return render (request,'stl8.html',context=dict)
#=========================================================
# Class wise student list class  nine
def stlc9(request,):
    r= stu.objects.all().filter(c='Nine')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Nine',}
    # dictionary={'student_info':stu}
    return render (request,'stl9.html',context=dict)

#=========================================================
#=========================================================
# Class wise student list class  ten
def stlc10(request,):
    r= stu.objects.all().filter(c='Ten')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Ten',}
    # dictionary={'student_info':stu}
    return render (request,'stl10.html',context=dict)

#========================================================

def stlc61(request,r,):
    
    r= stu.objects.all().filter(c='Six').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Six',}
    # dictionary={'student_info':stu}
    return render (request,'askstp6.html',context=dict)

#=========================================================   
def stlc71(request,r,):
        
    r= stu.objects.all().filter(c='Seven').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Seven',}
    # dictionary={'student_info':stu}
    return render (request,'askstp7.html',context=dict)

#=========================================================     
def stlc81(request,r,):
        
    r= stu.objects.all().filter(c='Eight').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Eight',}
    # dictionary={'student_info':stu}
    return render (request,'askstp8.html',context=dict)

#=========================================================   
def stlc91(request,r,):
        
    r= stu.objects.all().filter(c='Nine').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Nine',}
    # dictionary={'student_info':stu}
    return render (request,'askstp9.html',context=dict)

#=========================================================  
def stlc101(request,r,):
        
    r= stu.objects.all().filter(c='Ten').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Ten',}
    # dictionary={'student_info':stu}
    return render (request,'askstp10.html',context=dict)

#========================================================= 


def studentinfo(request,student_id):
    r= stu.objects.get(pk=student_id)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
    return render (request,'studentinfo.html',context=dict)
  
#=========================================================  
def seatplan(request):
        r= stu.objects.all()
        dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
        return render (request,'seatplan.html',context=dict)



#=========================================================
def seatplan_pdf(request):
     buf = io.BytesIO()
     c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
     textob=c.beginText()
     textob.setTextOrigin(inch,inch)
     textob.setFont("Helvetica",14)
     #lines = ["line 1",
            ##V  "line 2",
            #  "line 3",]
     r= stu.objects.all()
     lines =[]
     for admit in r:
         lines.append("=============  ")
         lines.append('Seat Plan')
         lines.append("Class:")      
         lines.append(admit.c)
         lines.append('Name')   
         lines.append(admit.n) 
         lines.append("Roll:")
         lines.append(admit.r)  
                                     
     for line in lines:
           textob.textLine(line)
           
     c.drawText(textob)
     c.showPage()
     c.save()
     buf.seek(0)
           
     return FileResponse(buf,as_attachment=True,filename='Seat Plan.pdf')

#=========================================================
def tr(request,student_id,):
    r= stu.objects.get(pk=student_id)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
    return render (request,'asktranscript.html',context=dict)


#=========================================================




def trc10(request,):
    r= stu.objects.all().filter(c='Ten')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Ten',}
    # dictionary={'student_info':stu}
    return render (request,'asktr10.html',context=dict)

#=========================================================
def trc9(request,):
    r= stu.objects.all().filter(c='Nine')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Nine',}
    # dictionary={'student_info':stu}
    return render (request,'asktr9.html',context=dict)

#=========================================================
def trc8(request,):
    r= stu.objects.all().filter(c='Eight')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Eight',}
    # dictionary={'student_info':stu}
    return render (request,'asktr8.html',context=dict)

#=========================================================
def trc7(request,):
    r= stu.objects.all().filter(c='Seven')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Seven',}
    # dictionary={'student_info':stu}
    return render (request,'asktr7.html',context=dict)

#=========================================================
def trc6(request,):
    r= stu.objects.all().filter(c='Six')
    
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Six',}
    # dictionary={'student_info':stu}
    return render (request,'asktr6.html',context=dict)

#=========================================================
def tr61(request,r,):
    
    r= stu.objects.all().filter(c='Six').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Six',}
    # dictionary={'student_info':stu}
    return render (request,'trc6.html',context=dict)

#=========================================================
def tr71(request,r,):
    
    r= stu.objects.all().filter(c='Seven').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Seven',}
    # dictionary={'student_info':stu}
    return render (request,'trc7.html',context=dict)

#=========================================================
def tr81(request,r,):
    
    r= stu.objects.all().filter(c='Eight').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Eight',}
    # dictionary={'student_info':stu}
    return render (request,'trc8.html',context=dict)

#=========================================================
def tr91(request,r,):
    
    r= stu.objects.all().filter(c='Nine').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Nine',}
    # dictionary={'student_info':stu}
    return render (request,'trc9.html',context=dict)

#=========================================================
def tr101(request,r,):
    
    r= stu.objects.all().filter(c='Ten').get(r=r)
    dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022','x':'Ten',}
    # dictionary={'student_info':stu}
    return render (request,'trc10.html',context=dict)

#=========================================================
"""def transcript_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf,pagesize=A4,bottomup=0)
        textobj=c.beginText()
        textobj.setTextOrigin(inch,inch)
        textobj.setFont("Helvetica",14)
        #lines = ["line 1",
                ##V  "line 2",
                #  "line 3",]
        r= stu.objects.all() 
        x= stu.objects.get(pk=id)  
        y=int(x)    
       
        lines =[]
        for admit in r:
            
            lines.append("--------------------------  ")
            #lines.append('Admit Card')
            lines.append("Class:")      
            lines.append(admit.c)
            lines.append('Name')   
            lines.append(admit.n) 
            lines.append("Roll:")
            lines.append(admit.r)  
            lines.append("Bangla:")      
            lines.append(admit.b)
            lines.append('Engllish')   
            lines.append(admit.e) 
            lines.append("Science:")
            lines.append(admit.s)
            lines.append("Mathematics:")
            lines.append(admit.m)     
                                            
        for line in lines:
           textobj.textLine(line)
            
        c.drawText(textobj)
        c.showPage()
        c.save()
        buf.seek(0)
            
        return FileResponse(buf,as_attachment=True,filename='Transcript.pdf')"""

#=========================================================

                 
#=========================================================
def userhome(request):
         r= stu.objects.all()
         dict={'student':r,'skul':'Barishal Zilla School',
           'exam':'Annual Examination 2022',}
    # dictionary={'student_info':stu}
      
         return render(request,'userhome.html',context=dict) 
 #=========================================================  

#=========================================================
#=========================================================  



