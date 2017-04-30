from __future__ import unicode_literals
from django.db import models
# user
from users.models import User
from datetime import datetime
import uuid

# Funciones:
# funcion para almacenamiento de imagenes
def content_file_name(instance, filename):
    return '/'.join(['publishings', datetime.now().strftime('%Y-%m-%d'), filename])


# Create your models here.
class Publishing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to=content_file_name)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
