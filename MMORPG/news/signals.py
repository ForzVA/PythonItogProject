from cgitb import html
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, post_init, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from news.models import Comment, Post

@receiver(post_save, sender=Comment)
def send_mail(sender, instance, created, **kwargs):
    if created:
        user = instance.post_comment.author 

        html = render_to_string(
                'MMORPG/mail_messages/new_comment.html',
                {'comment': instance, 'user': user }
            )

        msg = EmailMultiAlternatives(
            subject=f"У вас новый отклик!",
            from_email='ma1ltest.mail@yandex.by',
            to = [user.email],
        )

        msg.attach_alternative(html, 'text/html')
        msg.send()
    else:
        user = instance.user_comment

        html = render_to_string(
                'MMORPG/mail_messages/status_comment.html',
                {'comment': instance, 'user': user }
            )

        msg = EmailMultiAlternatives(
            subject=f"У вас новый отклик!",
            to = [user.email],
        )

        msg.attach_alternative(html, 'text/html')
        msg.send()
        