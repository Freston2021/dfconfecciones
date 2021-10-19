"""URLs for bitmazk-contact-form application."""
from django.conf.urls import url

from .views import ContactFormView


from django.urls import path, re_path, reverse_lazy
from django.views.generic import RedirectView


app_name = 'contact_form'
urlpatterns = [
    url(r'^', ContactFormView.as_view(), name='contact_form'),
    ]
