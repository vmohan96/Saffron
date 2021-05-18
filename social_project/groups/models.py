from django.db import models
from django.utils.text import slugify

# Create your models here.
# GROUPS MODELS.PY

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unqiue=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManytoManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_self(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta():
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        self.user.username

    class Meta():
        unique_together = ('group', 'user')
