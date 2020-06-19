from django import forms

from push import models


class PushForm(forms.ModelForm):
    class Meta:
        model = models.Push
        fields = '__all__'


class OptionForm(forms.ModelForm):
    class Meta:
        model = models.Option
        fields = '__all__'
