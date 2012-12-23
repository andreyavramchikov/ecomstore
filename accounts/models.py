from django.db import models
from django.contrib.auth.models import User

class UserProfile():
    user = models.ForeignKey(User,unique=True)

    def __unicode__(self):
        return 'User Profile for : ' + self.user.username