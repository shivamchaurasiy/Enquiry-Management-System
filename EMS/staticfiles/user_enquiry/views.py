from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import UserSignUp, UserQuery
from django.contrib import messages

def user(req):
    return render(req, 'user_enquiry/user.html')

def user_signup(req):
    if req.method=='POST':
        nm=req.POST.get('fn')
        email=req.POST.get('email')
        cn=req.POST.get('cn')
        pwd=req.POST.get('pwd')
        cpwd=req.POST.get('cpwd')
        user = UserSignUp.objects.filter(email=email)
        if user:
            messages.add_message(req, messages.SUCCESS, 'User Already Exist')
            return redirect('/usersignup/')
        else:
            if pwd==cpwd:
                newuser=UserSignUp.objects.create(name=nm, email=email, contact=cn, password=pwd, confirm_password=cpwd)
                messages.add_message(req, messages.SUCCESS, 'User Registration Successfully')
                return redirect('/usersignup/')
            else:
                messages.add_message(req, messages.ERROR, "Password and Confirm Password doesn't match")
                return redirect('/usersignup/')
    return render(req, 'user_enquiry/usersignup.html')  # return for get request


def user_login(req):
    return render(req, 'user_enquiry/userlogin.html')

def user_dashboard(req):
    if req.method=='POST':
        email=req.POST['email']  # email, pwd is name of input attributes
        password=req.POST['pwd']
        try:
            user=UserSignUp.objects.get(email=email)
            if user.password==password:
                req.session['name']=user.name
                req.session['email']=user.email
                return render(req, 'user_enquiry/userdashboard.html')
            else:
                messages.add_message(req, messages.ERROR, 'Invalid Password')
                return render(req,'user_enquiry/userlogin.html')
            
        except UserSignUp.DoesNotExist:
            messages.add_message(req, messages.WARNING, 'Email does not exist')
            return redirect('/userlogin/')
                
    else:
        # msg="user dose not exist"
        return render(req,'user_enquiry/userdashboard.html')   
    
def user_enquiry(req):
    return render(req, 'user_enquiry/userenquiry.html')

def query_submit(req):
    if req.method=="POST":
        sn = req.POST.get('sn')
        cn = req.POST.get('cn')
        email = req.POST.get('email')
        query = req.POST.get('query')
        data = UserQuery.objects.create(stu_name=sn, contact=cn, email=email, query=query)
        messages.add_message(req, messages.SUCCESS, 'Your query successfully submitted')
    return render(req, 'user_enquiry/userenquiry.html')

