from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import AdminSignUp
from django.contrib import messages
# from user_enquiry.models import UserSignUp
from user_enquiry.models import UserQuery


def home(req):
    return render(req, 'admin_enquiry/home.html')

def admin_user(req):
    return render(req, 'admin_enquiry/adminuser.html')

def admin_signup(req):
    return render(req, 'admin_enquiry/adminsignup.html')

def adminsignup_submit(req):
    if req.method=="POST":   
        fn = req.POST.get('fn')
        email = req.POST.get('email')
        pwd = req.POST.get('pwd')
        cpwd = req.POST.get('cpwd')
        user = AdminSignUp.objects.filter(email=email)
        if  user:
            messages.add_message(req, messages.WARNING, 'Admin Already Exist')
            return render(req, 'admin_enquiry/adminsignup.html')
        else:
            if pwd == cpwd:
                newuser = AdminSignUp.objects.create(name=fn, email=email, password=pwd, confirm_password=cpwd)
                newuser.save()
                messages.add_message(req, messages.SUCCESS, "Admin registration successfully")
                return render(req, 'admin_enquiry/adminsignup.html')
            else:
                messages.add_message(req, messages.ERROR, "Password doesn't match")
        return render(req, 'admin_enquiry/adminsignup.html')
    
    
def admin_login(req):
    return render(req, 'admin_enquiry/adminlogin.html')


def admin_dashboard(req):
    if req.method=='POST':
        email=req.POST['email']
        password=req.POST['pwd']
        try:
            user=AdminSignUp.objects.get(email=email)
            if user.password==password:
                req.session['name']=user.name
                req.session['email']=user.email
                return render(req,'admin_enquiry/admindashboard.html')
            else:
                messages.add_message(req, messages.WARNING, 'Invalid Password')
                return render(req,'admin_enquiry/adminlogin.html')
            
        except AdminSignUp.DoesNotExist:
            messages.add_message(req, messages.WARNING, 'Email doesn,t exists')
            return redirect('/adminlogin/')
    else:
        return render(req, 'admin_enquiry/admindashboard.html')         
    
    
    
# ********************************CRUD QUERY ********************************
    
def show_enquiry(req):
    allquery=UserQuery.objects.all()
    return render(req, 'admin_enquiry/showenquiry.html', {'allquery':allquery})

def delete(req, id):
    id = UserQuery.objects.get(id=id)
    id.delete()
    return redirect('/showenquiry/')



 
# def update(req, id):
#     if req.method=='POST':
#         sn = req.POST.get('sn')
#         cn = req.POST.get('cn')
#         email = req.POST.get('email')
#         query = req.POST.get('query')
#         data = UserQuery(id=id, stu_name=sn, contact=cn, email=email, query=query )
#         data.save()
#         return redirect('/showenquiry/')
#     else:
#         id = UserQuery.objects.get(id=id)  
#         return render(req, 'admin_enquiry/updatedata.html', {'id':id})