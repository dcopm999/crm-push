# -*- coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PushConfig(AppConfig):
    name = 'push'
    verbose_name = _("Push Notifications")
