from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy ---old django
from django.urls import reverse_lazy
from django.views.generic import CreateView


from . import forms # create the forms.py and connect login and logout
# to actual view.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
