from django.db import models

# Create your models here.

class TodoList(models.Model):

    class StatusChoices(models.TextChoices):
        NEW = "new", "Yangi"
        IN_PROGRESS = "in_progress", "Jarayonda"
        COMPLATED = "complated", "Bajarilgan"

    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=40, choices=StatusChoices.choices, default=StatusChoices.NEW)

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    brend = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Telefon(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    brend = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name