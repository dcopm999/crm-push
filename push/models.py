# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Option(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    value = models.BooleanField(verbose_name=_("Value"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('push:option-update', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")


class Push(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    text = models.TextField(verbose_name=_("Text"))
    created = models.DateField(auto_now_add=True, editable=False, verbose_name=_("Created date"))
    push_date = models.DateField(verbose_name=_("Push date"))
    pushed = models.BooleanField(verbose_name=_("Pushed"))
    count = models.PositiveSmallIntegerField(verbose_name=_("Push count"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('push:push-update', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("Push")
        verbose_name_plural = _("Pushes")
