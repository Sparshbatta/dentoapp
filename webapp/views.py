from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
	return render(request,'index.html',{})

def contact(request):
	if request.method=='POST':
		message_email = request.POST['message-email']
		message_name = request.POST['message-name']
		message = request.POST['message']
		print(message_name)
		send_mail(

			message_name, # subject
			message, # message
			message_email, # from email
			[settings.EMAIL_HOST_USER] # to email (is a list of emails)
			)

		return render(request,'contact.html',{'message_name':message_name})
	else:
		return render(request,'contact.html',{})


def about(request):
	return render(request,'about.html',{})

def pricing(request):
	return render(request,'pricing.html',{})

def service(request):
	return render(request,'service.html',{})

def appointment(request):
	if request.method=='POST':
		your_name=request.POST['your-name']
		your_phone=request.POST['your-phone']
		your_email=request.POST['your-email']
		your_address=request.POST['your-address']
		your_schedule=request.POST['your-schedule']
		your_day=request.POST['your-day']
		your_message=request.POST['your-message']

		appointment="Name: " + your_name + " " + "\nYour Phone: " + your_phone + " " + "\nYour Email: " + your_email + " " + "\nYour Address: " + your_address + " " + "\nSchedule: " + your_schedule + " " + "\nDay: " + your_day + " " + "\nMessage: " + your_message
		#send an email
		send_mail(

			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			[settings.EMAIL_HOST_USER] # to email (is a list of emails)
			)


		return render(request,'appointment.html',
			{'your_name':your_name,
			'your_phone':your_phone,
			'your_email':your_email,
			'your_address':your_address,
			'your_schedule':your_schedule,
			'your_day':your_day,
			'your_message':your_message})

	else:
		return render(request,'appointment.html',{'your_name':[],
			'your_phone':[],
			'your_email':[],
			'your_address':[],
			'your_schedule':[],
			'your_day':[],
			'your_message':[]})
