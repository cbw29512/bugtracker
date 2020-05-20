from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, unique=True)


class Ticket(models.Model): 
    # docs.djangoproject.com   
    NEW = 'NEW'
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'
    INVALID = 'INVALID'
    STATUS_CHOICES = [
        (NEW, 'NEW'),
        (IN_PROGRESS, 'IN PROGRESS'),
        (DONE, 'DONE'),
        (INVALID, 'INVALID'),
    ]

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    filed_user = models.ForeignKey(
        get_user_model(),
        related_name = 'filed_user',
        on_delete=models.CASCADE,
    )
    ticket_status = models.CharField(max_length=20, choices = STATUS_CHOICES, default =NEW)
    assigned_user = models.ForeignKey(
        get_user_model(),
        related_name = 'ticket_user',
        on_delete=models.CASCADE,
    )
    completed_user = models.ForeignKey(
        get_user_model(),
        related_name = 'completed_user',
        on_delete=models.CASCADE,
    )

    
def __str__(self):
    return self.title
