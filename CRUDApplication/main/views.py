from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView


# Create your views here.


def index(request):
    return render(request, 'mainApp/base.html', {})


class UsersList(ListView):
    context_object_name = 'users'
    model = models.CreateUser
    template_name = 'main/allUsers.html'


class Create(CreateView):
    fields = ('name', 'age', 'email', 'gender')
    model = models.CreateUser


class Details(DetailView):
    context_object_name = 'user_details'
    model = models.CreateUser
    template_name = 'main/detail_form.html'


class Update(UpdateView):
    fields = ('age', 'email')
    model = models.CreateUser


class Delete(DeleteView):
    model = models.CreateUser
    success_url = reverse_lazy('main:allUsers')