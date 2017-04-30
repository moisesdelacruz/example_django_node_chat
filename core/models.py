from __future__ import unicode_literals

from django.db import models
# user
from users.models import User
from publishings.models import Publishing
import uuid
# Create your models here.

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publishing = models.ForeignKey(Publishing)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.publishing.text
