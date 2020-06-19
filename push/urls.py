# -*- coding: utf-8 -*-
from django.urls import path

from push import views

app_name = 'push'

urlpatterns = [
    # PUSH
    path('push/', views.PushListView.as_view(), name="push-list"),
    path('push/create/', views.PushCreateView.as_view(), name="push-create"),
    path('push/update/<int:pk>', views.PushUpdateView.as_view(), name="push-update"),
    path('push/delete/<int:pk>', views.PushDeleteView.as_view(), name="push-delete"),
    # OPTION
    path('option/', views.OptionListView.as_view(), name="option-list"),
    path('option/create/', views.OptionCreateView.as_view(), name="option-create"),
    path('option/update/<int:pk>', views.OptionUpdateView.as_view(), name="option-update"),
    path('option/delete/<int:pk>', views.OptionDeleteView.as_view(), name="option-delete"),
]
