from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import math, random
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail

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
            return render(request, 'login_ritwik.html', context)

        if password == requested_profile.password:
            context = {'email': email}
            return redirect('profile')

        return redirect('profile')
    return render(request, 'login_ritwik.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        check_user = User.objects.filter(email=email).first()
        # if not email.split('@')[1]=='iitb.ac.in':
        #     context = {'message': 'Login using your ldap id', 'class':'danger'}
        #     return render(request, 'register.html', context)
        if check_user:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'register.html', context)

        #user = User(email=email, username=name)
        #user.save()
        #otp = str(random.randint(1000, 9999))
        #profile = Profile(user=user, mobile=mobile, otp=otp)
        #profile.save()
        #email_success, mobile_success = send_otp(email, mobile, otp)
        request.session['email'] = email
        request.session['name'] = name
        request.session['password'] = password
        otp = generateOTP()
        send_otp(email, otp)
        return redirect('otp')

        #if not email_success and not mobile_success:
            #context = {'message': 'OTP failed to generate', 'class': 'danger'}
            #return render(request, 'regiser.html', context)
        #return redirect('otp')
    return render(request, 'register.html')


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP



def send_otp(email, otp_generated):
    subject = "OTP request"
    message = 'Hi, your otp is '+ str(otp_generated) 
    email_from = settings.EMAIL_HOST_USER
    recipient = [email,]
    send_mail(subject, message, email_from, recipient, fail_silently = True)
    return None

def otp(request):
    # mobile = request.session['mobile']
    # email = request.session['email']
    # otp_to_check = request.session['otp']
    # name = request.session['name']
    # password = request.session['password']
    # context = {'mobile': mobile, 'email': email}
    # print(otp_to_check)
    # if request.method == 'POST':
    #     otp = request.POST.get('otp')
    #     if otp == otp_to_check:
    #         user = User(email=email, username=name)
    #         profile = Profile(user=user, mobile=mobile, password=password)
    #         user.save()
    #         profile.save()
    #         return redirect('login')
    #     else:
    #         print('Wrong')

    #         context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile, 'email': email}
    #         return render(request, 'otp.html', context)
    return render(request, 'otp.html'   )





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
