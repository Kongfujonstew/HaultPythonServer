# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        

class Profiles(models.Model):
    first = models.CharField(max_length=100, blank=True, null=True)
    last = models.CharField(max_length=100, blank=True, null=True)
    display = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profiles'


class Pageviews(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=500)
    time_open = models.DateTimeField()
    time_closed = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    profile = models.ForeignKey('Profiles', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pageviews'


