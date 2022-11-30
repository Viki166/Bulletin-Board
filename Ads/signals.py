# from django.core.mail import mail_managers
# from .models import Comment

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# @receiver(post_save, sender=Comment)
# def send_mail(sender,instance,created,**kwargs):
#     if created:
#         subject = 'Comment message is created!'
#     else:
#         subject = 'Change comment message, look!'

#     mail_managers(
#         subject=subject,
#         message="hello!"
#     )


# send_mail(
#                 subject='viktoria',
#                 message="Вам прислали комментарий",
#                 from_email='bobby.loner27@gmail.com',
#                 recipient_list=['vika49661@mail.ru']
#             )