from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
import math, random
from django.contrib.auth.models import User

def index(request):
    return render(request, "land.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        requested_profile = Profile.objects.filter(user=user).first()
        if user is None:
            context = {'message': 'User not found', 'class': 'danger'}
            return render(request, 'login.html', context)

        if password == requested_profile.password:
            context = {'email': email}
            return redirect('profile')

        return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        check_user = User.objects.filter(email=email).first()
        check_profile = Profile.objects.filter(mobile=mobile).first()
        # if not email.split('@')[1]=='iitb.ac.in':
        #     context = {'message': 'Login using your ldap id', 'class':'danger'}
        #     return render(request, 'register.html', context)
        if check_user or check_profile:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'register.html', context)

        #user = User(email=email, username=name)
        #user.save()
        #otp = str(random.randint(1000, 9999))
        #profile = Profile(user=user, mobile=mobile, otp=otp)
        #profile.save()
        #email_success, mobile_success = send_otp(email, mobile, otp)
        request.session['mobile'] = mobile
        request.session['email'] = email
        request.session['otp'] = otp
        request.session['name'] = name
        request.session['password'] = password
        #if not email_success and not mobile_success:
            #context = {'message': 'OTP failed to generate', 'class': 'danger'}
            #return render(request, 'regiser.html', context)
        #return redirect('otp')
    return render(request, 'register.html')


# def generateOTP():
#     digits = "0123456789"
#     OTP = ""
#     for i in range(4) :
#         OTP += digits[math.floor(random.random() * 10)]
#     return OTP



# def send_otp(request):
#      email=request.GET.get("email")
#      print(email)
#      o=generateOTP()
#      htmlgen = '<p>Your OTP is <strong>o</strong></p>'
#      send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
#      return HttpResponse(o)


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.register)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.register.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.register)
#         p_form = ProfileUpdateForm(instance=request.register.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(request, 'register/profile.html', context)
