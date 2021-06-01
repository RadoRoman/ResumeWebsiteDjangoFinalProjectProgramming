from django.shortcuts import render
from django.core.mail import send_mail
from resumesite.models import Contact


# def home(request):
#     return render(request, 'index.html', {})


def home(request):  # method catching post request if email was sent
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        ins = Contact(name=message_name, email=message_email, message=message)
        ins.save()  # creating an email instance for django admin database

        # send an email
        send_mail(
            f'{message_name} is trying to contact you',  # subject
            message,  # message
            message_email,  # from Email
            ['emai@email.sk'],  # to Email
        )
        return render(request, 'index.html', {'message_name': message_name})

    else:
        return render(request, 'index.html', {})  # if there's no post request, display the page




