from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from src.api_places import STATUS_CHOICES
# Create your models here.



class Middlepoint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    point_1 = models.CharField(max_length = 200)
    point_2 = models.CharField(max_length = 200)
    type_of_point = models.CharField(max_length = 200,choices=STATUS_CHOICES)
    middle_points = models.CharField(max_length = 200, null = True)
    infomarti = models.TextField(null = True )


class MyUsers(User):
    localitation = models.CharField(max_length = 200)

class Friends(models.Model):
    users = models.ManyToManyField (User ,related_name='friend_set')
    current_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name= 'owner',null = True  )

    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(
            current_user =  current_user
        )
        friend.users.add(new_friend)
    
    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(
            current_user =  current_user
        )
        friend.users.remove(new_friend)