from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile, Relationship

# every time a new user is created, profile will created automatically for this user 
# User is send some information about user being created 
@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
  '''
  sender : model of user 
  instance : instance of particular user 
  created: boolean values 
  '''
  # print('sender', sender) # sender <class 'django.contrib.auth.models.User' > 
  # print('instance', instance) # name of user 
  if created: # if a user is created (new instance of user being created )
    Profile.objects.create(user=instance)


# when user accept add request friend, automatically add friend in user friends 
@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
  sender_ = instance.sender 
  receiver_ = instance.receiver 
  if instance.status == 'accepted': 
    sender_.friends.add(receiver_.user)
    receiver_.friends.add(sender_.user)
    sender_.save()
    receiver_.save()

  


@receiver(pre_delete, sender=Relationship)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
  sender = instance.sender # from model DB
  receiver = instance.receiver 
  sender.friends.remove(receiver.user)
  receiver.friends.remove(sender.user)
  sender.save()
  receiver.save()
