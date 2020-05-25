from django.db import models

# Create your models here.

class table1(models.Model):
    fullname = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    ps = models.CharField(max_length=40)
    re_pass = models.CharField(max_length=40)
    file = models.CharField(max_length=40)
    agree_term = models.CharField(max_length=40)

class table2(models.Model):
    fullname = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    ps = models.CharField(max_length=40)
    re_pass = models.CharField(max_length=40)
    file = models.CharField(max_length=40)
    agree_term = models.CharField(max_length=40)


class img_table(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)


#def __str__(self):
 #   return self.username + '==>' + self.email +'==>' + self.password