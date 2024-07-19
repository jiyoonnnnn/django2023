from django.db import models
from django.contrib.auth.models import User


class Comwrite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Sale(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Find(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    CATEGORY_CHOICES = (
        ('technology', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
    )

    def __str__(self):
        return self.subject
class Comcomment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comwrite = models.ForeignKey(Comwrite, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)