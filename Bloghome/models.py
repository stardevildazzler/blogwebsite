from django.db import models



class quary(models.Model):
    id=models.AutoField(primary_key='true')
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=10)
    subject=models.CharField(max_length=100)
    quary1=models.CharField( max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    

class userdetail(models.Model):
    id=models.AutoField(primary_key='true')
    usrname=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    pass1=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + " ----- username is-----"+ self.usrname
