from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import edit
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from push import (models, forms)


@method_decorator(login_required, name='dispatch')
class PushListView(generic.ListView):
    model = models.Push


@method_decorator(login_required, name='dispatch')
class PushCreateView(edit.CreateView):
    model = models.Push
    form_class = forms.PushForm
    success_url = reverse_lazy('push:push-list')


@method_decorator(login_required, name='dispatch')
class PushUpdateView(edit.UpdateView):
    model = models.Push
    form_class = forms.PushForm
    success_url = reverse_lazy('push:push-list')


@method_decorator(login_required, name='dispatch')
class PushDeleteView(edit.DeleteView):
    model = models.Push
    success_url = reverse_lazy('push:push-list')


@method_decorator(login_required, name='dispatch')
class OptionListView(generic.ListView):
    model = models.Option


@method_decorator(login_required, name='dispatch')
class OptionCreateView(edit.CreateView):
    model = models.Option
    form_class = forms.OptionForm
    success_url = reverse_lazy('push:option-list')


@method_decorator(login_required, name='dispatch')
class OptionUpdateView(edit.UpdateView):
    model = models.Option
    form_class = forms.OptionForm
    success_url = reverse_lazy('push:option-list')


@method_decorator(login_required, name='dispatch')
class OptionDeleteView(edit.DeleteView):
    model = models.Option
    success_url = reverse_lazy('push:option-list')
