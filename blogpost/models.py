from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class blogpost(models.Model):
    id=models.AutoField(primary_key='true')
    blogname=models.CharField(max_length=100)
    blogtitle=models.CharField(max_length=100)
    text=models.TextField( max_length=10000)
    image=models.ImageField( upload_to='pic')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blogtitle

class blogcomment(models.Model):
    srno=models.AutoField(primary_key='true')
    comment=models.CharField( max_length=1000)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost=models.ForeignKey(blogpost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE , null=True)
    date = models.DateTimeField(default=now)
    def __str__(self):
        return "commnet by "+self.userdetail.firstname

    

    

 