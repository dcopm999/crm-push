# -*- coding: utf-8 -*-
from django.contrib import admin

from push import models


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Push)
class PushAdmin(admin.ModelAdmin):
    pass
