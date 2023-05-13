from django.db import models
from django.contrib.auth.models import User

class Left(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    referal = models.CharField(max_length=100, default='NA')
    package = models.CharField(max_length=100,default='')
    date_created =( models.DateTimeField(auto_now_add=True))
    # any other fields you want to add
    def __str__(self):
        return self.firstname
class Right(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    referal = models.CharField(max_length=100, default='NA') 
    package = models.CharField(max_length=100,default='') 
    date_created =( models.DateTimeField(auto_now_add=True))
    # any other fields you want to add
    def __str__(self):
        return self.firstname
class Parent(models.Model):
    left = models.ForeignKey(Left, on_delete=models.CASCADE)
    right = models.ForeignKey(Right, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.left} - {self.right}'
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # left = models.OneToOneField(Left, on_delete=models.CASCADE, null=True, blank=True)
    # right = models.OneToOneField(Right, on_delete=models.CASCADE, null=True, blank=True)
    # any additional fields you want to add to the user profile
    def __str__(self):
        return self.username

class CommonTotal(models.Model):
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Common Total: {self.total}"
        
    def calculate_commission(self):
        commission_rate = 0.075  # 7.5% commission rate
        commission = self.total * commission_rate
        return f"Commission: {commission:.2f}"
    
# class Kyc(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)