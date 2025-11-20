from django.db import models

class Tokens(models.Model):
    token = models.CharField(max_length=2000)
    refreshToken= models.CharField(max_length=2000)
    tokenUri= models.CharField(max_length=200)
    clientId= models.CharField(max_length=200)
    clientSecret= models.CharField(max_length=200)
    scopes= models.CharField(max_length=200)
    universeDomain= models.CharField(max_length=200)
    account= models.CharField(max_length=200,blank=True, null=True)
    expiry= models.CharField(max_length=200)
    