from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Table(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    time_stamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
