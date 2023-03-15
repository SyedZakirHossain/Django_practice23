
from django.urls import path
from skul import views

app_name="skul"


urlpatterns = [
        path('',views.home,name="home"),
        path('about/',views.about,name="about"),
        #path('about2/', views.about2, name="about2"),
        path('add/', views.add,name='add'),
        path('add/addsave', views.addsave,name='addsave'), 
        
        path('admit', views.admit, name="admit"),
        path('contact/', views.contact,name="contact"),
        path('contact/contactsave', views.contactsave,name="contactsave"), 
        path('enter2/', views.enter2, name="enter2"),
        
        path('homework/', views.homework,name="homework"), 
        path('homework/homeworksave', views.homeworksave,name="homeworksave"), 
       
        
        path('login/', views.login, name="login"),   
        path('logout/', views.logout, name="logout"),  
        
         
        path('login_page/', views.login_page, name="login_page"), 
        path('login/enter2', views.enter2, name="enter2"), 
        
        path('notice/', views.notice,name='notice'),
        path('notice_PDF', views.notice_PDF, name="notice_PDF"),
        #path('notice_PDF/<int:pk>/', views.notice_PDF, name="notice_PDF"),
        
        
        
        path('Print_PDF', views.Print_PDF, name="Print_PDF"),
        
        path('rscw/', views.rscw,name="rscw"),
        path('register', views.register, name="register"),
        path('report_pdf', views.report_pdf, name="report_pdf"),
        path('register2/register', views.register, name="register"),
        path('register2/', views.register2, name="register2"),
        path('result', views.result,name="result"),
        path('stulist', views.stulist,name="stulist"), 
        path('stulist2', views.stulist2,name="stulist2"), 
        path('studentlist2_pdf', views.studentlist2_pdf,name="studentlist2_pdf"), 
        path('studentlist_pdf', views.studentlist_pdf,name="studentlist_pdf"),
        path('seatplan/', views.seatplan, name="seatplan"),
        path('seatplan_pdf', views.seatplan_pdf,name="seatplan_pdf"),
        
        path('studentinfo/<int:student_id>', views.studentinfo,name="studentinfo"),
            
               
        path('stlcw/', views.stlcw,name="stlcw"),
        
        path('stl6/', views.stlc6,name="stlc6"),
        path('stl7/', views.stlc7,name="stlc7"),
        path('stl8/', views.stlc8,name="stlc8"),
        path('stl9/', views.stlc9,name="stlc9"),
        path('stl10/', views.stlc10,name="stlc10"),
        
        path('stp6/<int:r>/', views.stlc61,name="stlc61"),
        path('stp7/<int:r>/', views.stlc71,name="stlc71"),
        path('stp8/<int:r>/', views.stlc81,name="stlc81"),
        path('stp9/<int:r>/', views.stlc91,name="stlc91"),
        path('stp10/<int:r>/', views.stlc101,name="stlc101"),
        
        path('tr/<int:student_id>/', views.tr,name="tr"),
                    
              
        path('trc6/', views.trc6,name="trc6"),
        path('trc7/', views.trc7,name="trc7"),
        path('trc8/', views.trc8,name="trc8"),
        path('trc9/', views.trc9,name="trc9"),
        path('trc10/', views.trc10,name="trc10"),
        
        
        path('tr6/<int:r>/', views.tr61,name="tr61"),
        path('tr7/<int:r>/', views.tr71,name="tr71"),
        path('tr8/<int:r>/', views.tr81,name="tr81"),
        path('tr9/<int:r>/', views.tr91,name="tr91"),
        path('tr10/<int:r>/', views.tr101,name="tr101"),
                 
        
        path('userhome/', views.userhome, name="userhome"),

   ]



