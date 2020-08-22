from django.core.mail import send_mail, EmailMessage

def send_email(subject, message, from_email, to_email):
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)
    return