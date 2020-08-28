# from django.db.models.signals import post_save,post_delete
# from django.contrib.auth.models import User
# from .models import profile
# from django.dispatch import receiver


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		user=instance

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
# 	instance.objects.save

# @receiver(post_delete, sender=User)
# def delete_profile(sender, instance, deleted, **kwargs):
# 	if deleted:
# 		profile.objects.delete(user=instance)