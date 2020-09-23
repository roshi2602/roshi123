from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
from appatt.forms import UserForm

def index(request):
    return HttpResponseRedirect(reverse('employee_list'))

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


@login_required(login_url="/login/")
def employee_list(request):

    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    return render(request, 'appatt/index.html', context)  #in empployee app

@login_required(login_url="/login/")
def employee_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'appatt/details.html', context)  #in employee app

@login_required(login_url="/login/")
def employee_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()    
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'appatt/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'appatt/add.html', context)  #in employee app

@login_required(login_url="/login/")
def employee_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()    
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'appatt/edit.html', {"user_form": user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'appatt/edit.html', {"user_form": user_form})

@login_required(login_url="/login/")
def employee_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'appatt/delete.html', context) #in employee app


class ProfileUpdate(UpdateView):
    fields = ['designation', 'signin_time', 'signout_time']
    template_name = 'auth/profile_update.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user



class MyProfile(DetailView):
    template_name = 'auth/profile.html'

    def get_object(self):
        return self.request.user


