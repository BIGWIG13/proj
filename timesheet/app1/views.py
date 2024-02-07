from django.shortcuts import render,redirect
from app1.models import tbl_emp,project,Assigned_project,report
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        a=request.POST['fname']
        b=request.POST['lname']
        c=request.POST['dsgn']
        d=request.POST['salary']
        e=request.POST['dptmt']
        f=request.POST['place']
        g=request.POST['phn']
        h=request.POST['email']
        i=request.POST['uname']
        j=request.POST['pswd']
        x=tbl_emp(firstname=a,lastname=b,designation=c,salary=d,department=e,place=f,phone=g,email=h,username=i,password=j)
        y=User(username=i)
        y.set_password(j)
        y.save()
        x.save()
        return HttpResponse('<script>alert("success"),window.location="/index";</script>')
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        u=request.POST["uname"]
        p=request.POST['pswd']
        au=authenticate(username=u,password=p)
        request.session['user_id']=u
        if au is not None and au.is_superuser==0:
            return render(request,'user.html')
        elif au is not None and au.is_superuser==1:
            return render(request,'admin.html')
    return render(request,"login.html")

def viewemp(request):
    d=tbl_emp.objects.all()
    return render(request,"view_emp.html",{'z':d})



def reportview(request):
    d=report.objects.all()
    return render(request,"report_view.html",{'y':d})
def user(request):
    return render(request,"user.html")
def admin(request):
    return render(request,"admin.html")

def viewassign(request):
    uid=request.session['user_id']
    q=User.objects.get(username=uid)
    eid=q.id
    print(eid)

    d=Assigned_project.objects.filter(employee_id=eid)

    return render(request,"view_assign.html",{'z':d})

def Addreport(request):
    uid=request.session['user_id']
    if request.method=="POST":
        a=request.POST['prjctid']
        b=request.POST['tym']
        c=request.POST['status']
        g=report(project_id=a,employee_id=uid,report_time=b,status=c)
        g.save()
        return HttpResponse('<script>alert("success"),window.location="/user";</script>')
    return render(request,"Add_report.html")


def assignproj(request,id):
    emp_id=id
    x=tbl_emp.objects.get(id=emp_id)
    u=x.username
    z=User.objects.get(username=u)
    emp=z.id
    q=project.objects.all()
    
    if request.method=="POST":
        a=request.POST['pname']
        b=request.POST['stime']
        c=request.POST['etime']

        q=Assigned_project(project_id=a,employee_id=emp,start_time=b ,end_time=c,status="Pending")
        q.save()
        return HttpResponse('<script>alert("Assigned Successfully"),window.location="/Admin";</script>')
    c=Assigned_project.objects.all()
    return render(request,"assign_proj_emp.html",{'p':q,'z':c})



def addproject(request):
     a=project.objects.all()
     if request.method=='POST':
         a=request.POST['pname']
         b=request.POST['topic']
         c=request.POST['cmnts']
         h=project(project_name=a,topic=b,comments=c)
         h.save()
         return HttpResponse('<script>alert("success"),window.location="/addproj";</script>')
     return render(request,"addproj.html",{'z':a})

def update(request,id):
    d=Assigned_project.objects.get(id=id)
    if request.method=='POST':
        d.status=request.POST['status']
        d.save()
        return HttpResponse('<script>alert("Updated"),window.location="/view_assign";</script>')
    return render(request,"viewassignupdt2.html",{'z':d})

def delete(request,id):
    b=project.objects.get(id=id)
    b.delete()
    return HttpResponse('<script>alert("Deleted"),window.location="/addproj";</script>')

def updt(request,id):
    b=project.objects.get(id=id)
    if request.method=='POST':
        b.project_name=request.POST['pname']
        b.topic=request.POST['topic']
        b.comments=request.POST['cmnts']
        b.save()
        return HttpResponse('<script>alert("Updated"),window.location="/addproj";</script>')
    return render(request,"updtproj.html",{'z':b})


def lgt(request):
    logout(request)
    return redirect("/index/")



