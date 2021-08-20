from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def resume(request):
    return render(request, 'portfolio/index.html')


def sentEmail(request):
    print(request.method)
    if request.method == 'POST':
        print('Guess it works')
    else:
        print('Still Troubleshooting')
    return HttpResponse('Email sent in my mind')


def sendEmail(request):
    if request.method == 'POST':

        template = render_to_string("portfolio/email_template.html", {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['ukasoanyaf@gmail.com']
        )

        email.fail_silently = False
        email.send()
        print('Yroubleshooting')

    return render(request, 'portfolio/email_sent.html')

# def sendEmail(request):
#     email = EmailMessage('This is the Subject',
#                          'This is the Body',
#                          'Sender Email',
#                          ['ukasoanyaf@gmail.com'])
#
#     # email.fail_silently = False
#     # email.send()
#     # if request.method == 'POST':
#     print('Troubleshooting')
#
#     return HttpResponse('Thanks for contacting me')
