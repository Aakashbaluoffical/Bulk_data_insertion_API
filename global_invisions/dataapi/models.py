from django.db import models 
from django.contrib.auth.hashers import make_password




class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile_tbl'
        ordering = ['-created_at']



    def __str__(self):
        return f"{self.first_name} {self.last_name}"    




class User(models.Model):
    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
       
    class Meta:
        db_table = 'user_tbl'



    #for password hashing
    def set_password(self, password):
        self.password = make_password(password)


    def __str__(self):
        return f'{self.username}'
