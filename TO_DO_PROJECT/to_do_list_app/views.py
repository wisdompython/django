from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from to_do_list_app.models import Task
from django.urls import reverse_lazy

# Create your views here.
def SignUp(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}')
            return redirect ('tasks')
            
        else:
            form = UserRegisterForm()

    return render (request, "users/signup.html", {'form':form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'to_do_list_app/tasklist.html'

    def get_context_data(self, **kwargs): # makes sure a user only sees his own data
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(author=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']= context['tasks'].filter(Title__icontains=search_input)

        context['search_input'] = search_input

        return context

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'to_do_list_app/addtask.html'
    success_url = reverse_lazy('tasks') # redirects to the task page
 
    fields = ['Title', 'Description']

    def form_valid(self, form): # this line of code ensures the author is the currrent logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'to_do_list_app/edit_task.html'

    fields = ['Title', 'Description','complete']

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'to_do_list_app/delete.html'
