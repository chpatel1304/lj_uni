from django.shortcuts import render,redirect
from .models import User,Doctor_Profile
import requests
import random
# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	return render(request,'contact.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'login.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						usertype=request.POST['usertype'],
						gender=request.POST['gender'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_picture=request.FILES['profile_picture']
					)
				msg="User Sign Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="Patient":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_picture']=user.profile_picture.url
					return render(request,'index.html')
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['mobile']=user.mobile
					request.session['profile_picture']=user.profile_picture.url
					return render(request,'doctor-index.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'login.html')

def blog_single(request):
	return render(request,'blog-single.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_picture']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.gender=request.POST['gender']
		try:
			user.profile_picture=request.FILES['profile_picture']
		except:
			pass
		user.save()
		request.session['profile_picture']=user.profile_picture.url
		msg="Profile Upadated Successfully"
		if user.usertype=="Patient":
			return render(request,'profile.html',{'msg':msg,'user':user})
		else:
			return render(request,'doctor-profile.html',{'msg':msg,'user':user})
	else:
		if user.usertype=="Patient":
			return render(request,'profile.html',{'user':user})
		else:
			return render(request,'doctor-profile.html',{'user':user})

def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		
		if user.password==request.POST['opassword']:
			if request.POST['npassword']==request.POST['cnpassword']:
				user.password=request.POST['npassword']
				user.save()
				return redirect('logout')
			else:
				msg="New Password & Confirm New Password Does Not Matched"
				if user.usertype=="Patient":
					return render(request,'change-password.html',{'msg':msg})
				else:
					return render(request,'doctor-change-password.html',{'msg':msg})
		else:
			msg="Old Password Does Not Matched"
			if user.usertype=="Patient":
				return render(request,'change-password.html',{'msg':msg})
			else:
				return render(request,'doctor-change-password.html',{'msg':msg})		
	else:
		if user.usertype=="Patient":
			return render(request,'change-password.html')
		else:
			return render(request,'doctor-change-password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			otp=random.randint(1000,9999)
			mobile=request.POST['mobile']
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"DwF5Auzh16qo3fXC2JMSTcOiyBEZmWH0eR8GIg4NbQrpUnKsjvhz0YwyOCGvHJEFuXRrTc7feDVaM1NA","variables_values":str(otp),"route":"otp","numbers":mobile}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			return render(request,'otp.html',{'otp':otp,'mobile':mobile})
		except:
			msg="Mobile Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	otp=int(request.POST['otp'])
	uotp=int(request.POST['uotp'])
	mobile=request.POST['mobile']

	if otp==uotp:
		return render(request,'new-password.html',{'mobile':mobile})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'otp':otp,'mobile':mobile,'msg':msg})

def new_password(request):
	mobile=request.POST['mobile']
	np=request.POST['npassword']
	cnp=request.POST['cnpassword']

	if np==cnp:
		user=User.objects.get(mobile=mobile)
		user.password=np
		user.save()
		msg="Password Updated Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password & Confirm New Password Does Not Matched"
		return render(request,'new-password.html',{'mobile':mobile,'msg':msg})

def doctor_detail(request):
	doctor_profile=Doctor_Profile()
	doctor=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		doctor_profile=Doctor_Profile.objects.create(
				doctor=doctor,
				qualification=request.POST['qualification'],
				specialization=request.POST['specialization'],
				experience_in_years=request.POST['experience_in_years'],
				clinic_address=request.POST['clinic_address'],
				time=request.POST['time'],
			)
		msg="Doctor Details Updated Successfully"
		return render(request,'doctor-detail.html',{'doctor_profile':doctor_profile,'msg':msg})
	else:
		try:
			doctor_profile=Doctor_Profile.objects.get(doctor=doctor)
		except:
			pass
		return render(request,'doctor-detail.html',{'doctor_profile':doctor_profile})