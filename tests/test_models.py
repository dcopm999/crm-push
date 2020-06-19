#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_crm-push
------------

Tests for `crm-push` models module.
"""

from django.test import TestCase
from django.urls import reverse

from push import models


class PushTestCase(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.entry = models.Push.objects.last()

    def test_push_str(self):
        self.assertEqual(self.entry.title, self.entry.__str__())

    def test_absolute_url(self):
        self.assertEqual(self.entry.get_absolute_url(), reverse('push:push-update', kwargs={'pk': self.entry.pk}))

    def tearDown(self):
        pass


class OptionTestCase(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.entry = models.Option.objects.last()

    def test_push_str(self):
        self.assertEqual(self.entry.name, self.entry.__str__())

    def test_absolute_url(self):
        self.assertEqual(self.entry.get_absolute_url(), reverse('push:option-update', kwargs={'pk': self.entry.pk}))

    def tearDown(self):
        pass
