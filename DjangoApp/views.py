from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django import forms
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic.edit import UpdateView
# from rest_framework.views import APIView

from .models import table1
from .models import viewnotes
from DjangoApp.forms import NotesForm, SignUpForm

def signupuser(request):
    if request.method == "GET":
        return render(request,'DjangoApp/signupuser.html',{'form':SignUpForm()})
    else:
        #Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return render(request,'DjangoApp/signupuser.html',{'form':SignUpForm(), 'error':'Registered Successfully'})
            except IntegrityError:
                return render(request,'DjangoApp/signupuser.html',{'form':SignUpForm(), 'error':'That username has already been taken. Please choose a new username'})

        else:
            # Tell the user the password did'nt match
            return render(request,'DjangoApp/signupuser.html',{'form':SignUpForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == "GET":
        return render(request,'DjangoApp/login_form.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'DjangoApp/login_form.html',{'form':AuthenticationForm(), 'error':'Username and Password did not match.'})
        else:
            login(request,user)
            return redirect('index')

def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        # return HttpResponse("You're logged out.")
        return redirect('loginuser')

def detail(request, field1):
    return HttpResponse("User Id: %s." % field1)

def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'DjangoApp/index.html')

def list(request):
    latest_list = table1.objects.order_by('-field2')[:3]
    num_list = table1.objects.all().count()
    context = {
        'num_list': num_list,
        'latest_list': latest_list
    }
    return render(request, 'notes/list.html', context)

class ListView(generic.ListView):
    model = table1
    template_name = 'notes/list-view.html'  # Specify your own template name/location
    # paginate_by = 2
    def get_context_data(self, **kwargs):
        my_list = table1.objects.all()
        # Call the base implementation first to get the context
        context = super(ListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context = {
            'my_list' : my_list
        } 
        return context

    def get_queryset(self):
        return table1.objects.all()

class FormView(generic.FormView):
    form_class = NotesForm
    template_name = 'DjangoApp/addnotes.html'
    
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['add'] = 1
        if request.GET:
            notevalue = request.GET['notes']
            n1 = viewnotes.objects.create(user = request.user, notes=notevalue)
            context['add'] = 1 
            return render (request, 'DjangoApp/addnotes.html',context)
        else:
            context['add'] = 0
            return render (request, 'DjangoApp/addnotes.html',context)
        return render (request, 'DjangoApp/addnotes.html',context)

# def add_notes(request):
#     context = {} 
#     context['form'] = NotesForm()
#     if request.GET: 
#         notevalue = request.GET['notes']
#         n1 = viewnotes.objects.create(notes=notevalue)  
#         return render (request, 'DjangoApp/add.html',context)
#     else:
#         return render (request, 'DjangoApp/addnotes.html',context)
#     return render (request, 'DjangoApp/login_form.html',context)

def view_notes(request):
    latest_list = viewnotes.objects.filter(user=request.user)
    num_list = viewnotes.objects.filter(user=request.user).count()
    context = {
        'num_list': num_list,
        'latest_list': latest_list
    }
    return render(request, 'DjangoApp/viewnotes.html', context)

def delete_notes(request,noteid):
    context = {}
    context['form'] = NotesForm()
    obj = get_object_or_404(viewnotes, noteid = noteid)
    context['obj'] = obj 
    obj.delete() 
    context["latest_list"] = viewnotes.objects.all() 
    context["num_list" ] = viewnotes.objects.all().count() 
    return render (request, 'DjangoApp/viewnotes.html',context)

def edit_notes(request,noteid):
    context = {}
    obj = get_object_or_404(viewnotes, noteid = noteid)
    context['obj'] = obj 
    if request.method == 'GET':
        context['form'] = NotesForm(instance=obj)
        return render (request, 'DjangoApp/editnotes.html',context)
    else:
        form = NotesForm(request.POST,instance=obj)
        form.save()
        return redirect ('view_notes')





















# # Get a session value by its key (e.g. 'my_car'), raising a KeyError if the key is not present
# my_car = request.session['my_car']

# # Get a session value, setting a default if it is not present ('mini')
# my_car = request.session.get('my_car', 'mini')

# # Set a session value
# request.session['my_car'] = 'mini'

# # Delete a session value
# del request.session['my_car']

