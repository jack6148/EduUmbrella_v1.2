from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from random import randint
import smtplib
from email.message import EmailMessage

# <Send Mail, Return True/False>
def send_email(toEmail, subject, mailBody):
    email_address = "redondevit@gmail.com" #SMTP_v1
    email_password = "nbip lbbu gzqx htca"

    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = toEmail
    msg.set_content(mailBody)

    msgFlag = False
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

        msgFlag = True        

    except Exception as ex:
         print ("Something went wrong….",ex)
         msgFlag = False
    
    return msgFlag

def test(request):
    context = {}
    return render(request, 'test.html', context)

def index(request):
    # value = randint(0, 10)

    universities = University.objects.all().order_by('id')
    range_value = len(universities)
    random1 = randint(1, range_value)
    random2 = randint(1, range_value)
    random3 = randint(1, range_value)
    context = {
        'university1': universities[random1 - 1],
        'university2': universities[random2 - 1],
        'university3': universities[random3 - 1]
        
    }
    return render(request, 'index.html', context)

def notification(request, id):

    title = ""
    message = ""
    if id == '1':
        title = "Submission Received"
        message = "Thank you for submitting your information. We will get in touch with you shortly via email or WhatsApp."
    elif id == '2':
        title = "Thnak You"
        message = "We have received your query and will contact you shortly via email."

    context = {
        'title': title,
        'message': message
    }
    return render(request, 'notification.html', context)

def universities(request):
    universities = University.objects.all().order_by('id')
    context = {
        'universities': universities
    }
    return render(request, 'universities.html', context)

def profile(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        whatsapp = request.POST.get('whatsapp')
        program = request.POST.get('program')
        study = request.POST.get('study')
        qualifications = request.POST.get('qualifications')

        program_name = "Bachelor" if program == '1' else "Master's" if program == '2' else "Ph.D"
        # Send Mail 
        subject = "[Education Umbrella] Submission of New Profile Entry"
        msgBody = '''
        Dear Admin,

        We would like to inform you about a new profile entry. The details are as follows:
        
        Name: {0}
        E-Mail: {1}
        Phone: {2}
        Whatsapp: {3}
        Program: {4}
        Study Area: {5}
        Qualification: {6}


        Note: Kindly respond at your earliest convenience.


        Kind Regards,
        Education Umbrella Team
        [System]

        Education Umbrella is a project of Redondev IT.
        '''.format(name, email, phone, whatsapp, program_name, study, qualifications)

        mail_status = send_email('jack6148@gmail.com', subject, msgBody)
        # Send Mail

        profile = Client_Profile()
        profile.name = name
        profile.email = email
        profile.phone = phone
        profile.whatsapp = whatsapp
        profile.program = program
        profile.study = study
        profile.qualifications = qualifications
        profile.created_by = 1
        profile.created_date = timezone.now()

        profile.save()
        response = redirect('/notification/1')
        return response
    else:
        context = {}
        return render(request, 'submit_profile.html', context)

def additional(request):
    context = {}
    return render(request, 'additional.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send Mail 
        subject = "[Education Umbrella] Submission of New Message Entry"
        msgBody = '''
        Dear Admin,

        We would like to inform you about a new Message entry. The details are as follows:
        
        Name: {0}
        E-Mail: {1}
        Subject: {2}
        Message: {3}


        Note: Kindly respond at your earliest convenience.


        Kind Regards,
        Education Umbrella Team
        [System]

        Education Umbrella is a project of Redondev IT.
        '''.format(name, email, subject, message)

        mail_status = send_email('jack6148@gmail.com', subject, msgBody)
        # Send Mail

        query = Client_Query()
        query.name = name
        query.email = email
        query.subject = subject
        query.message = message
        query.created_by = 1
        query.created_date = timezone.now()

        query.save()
        response = redirect('/notification/2')
        return response

    else:
        context = {}
        return render(request, 'contact.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def courses(request):
    context = {}
    return render(request, 'courses.html', context)

def admission(request, category):
    
    if category == 'Bachelor':
        para01 = "A bachelor’s degree is the foundation for building a successful career and gaining essential skills in your chosen field. At EduUmbrella, we connect you with top universities offering a wide range of undergraduate programs designed to match your interests and goals."
        para02 = "From selecting the right course to guiding you through the application process, our team ensures you have the support needed to make confident decisions. Whether your passion lies in engineering, business, arts, or sciences, we are here to help you take the first step toward a bright future."
        para03 = "Start your academic journey with Education Umbrella today!"
    elif category == 'Master':
        para01 = "Pursuing a master’s degree is a significant step toward advancing your career and deepening your knowledge in your chosen field. At EduUmbrella, we help you explore top universities worldwide that offer diverse master’s programs tailored to your academic background and career aspirations."
        para02 = "Our team provides expert guidance throughout the application process, ensuring you make informed decisions and present a strong application. Whether you’re looking to specialize in business, technology, healthcare, or any other field, we’re here to support you every step of the way in achieving your academic goals."
        para03 = "Take the next step in your education journey with Education Umbrella!"
    elif category == 'Doctoral':
        para01 = "A doctoral degree is the pinnacle of academic achievement, opening doors to advanced research, teaching, and specialized career opportunities. At EduUmbrella, we guide you in finding top universities offering doctoral programs across a wide range of fields."
        para02 = "Whether you're looking to pursue a PhD in science, humanities, engineering, or any other discipline, we provide expert support throughout the application process, from selecting the right program to submitting your application. Our goal is to help you advance your academic career and make a lasting impact in your field."
        para03 = "Take the next step towards your doctoral journey with Education Umbrella today!"
    else:
        para01 = "Learn Portuguese with specialized courses designed to enhance your language skills. At EduUmbrella, we connect you with top institutions offering comprehensive Portuguese language programs, whether you're a beginner or looking to advance your proficiency."
        para02 = "Our team will guide you in selecting the perfect course to meet your goals, whether for academic, professional, or personal growth. With tailored support, we ensure you have the tools to succeed in mastering the Portuguese language."
        para03 = "Start your language learning journey with Education Umbrella today!"

    context = {
        'category': category,
        'para01': para01,
        'para02': para02,
        'para03': para03
    }
    
    return render(request, 'admission.html', context)

def login(request):
    context = {}
    return render(request, 'user/login.html', context)