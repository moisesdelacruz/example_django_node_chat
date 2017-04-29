from __future__ import unicode_literals

from django.db import models
# user
from users.models import User
from themes.models import Theme
import uuid
# Create your models here.

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(Theme)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.theme.text
