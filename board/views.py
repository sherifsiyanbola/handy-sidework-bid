from django.shortcuts import render, get_object_or_404, redirect
from .models import inNeedOfService, serviceProvider
from django.views.generic import ListView, DetailView
from django.db.models import Q #Help in multiple filtering
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.
def home(request):
    return render(request, 'index.html')


class handyDashView(ListView):
    template_name = 'dash.html'
    model = serviceProvider
    context_object_name = 'services'

    def get_queryset(self):
        services = super().get_queryset()
        # return projects.filter(manager=self.request.user)
        # return services.filter(type_of__contains="Request Service")
        return services.all()

class serviceView(DetailView):
    template_name = 'view.html'
    model = serviceProvider
    context_object_name = 'service'

class requestServiceView(CreateView):
    template_name = 'apply.html'
    model = inNeedOfService
    fields = ['service_name', 'mycost', 'render_name', 'render_email', 'location', 'available_from', 'avaulable_to']

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'You have succesfully applied for this job')
        return redirect('dash')

    def get_queryset(self):
        return super().get_queryset()
        return inNeedOfService.filter(manager=self.request.user)
    
class hireView(CreateView):
    model = serviceProvider
    template_name = "hire.html"
    fields = ['title', 'description', 'location']

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'You have succesfully posted a new job')
        return redirect('dash')

class notificationView(ListView):
    model = inNeedOfService
    template_name = "notification.html"
    context_object_name = "notifications"

    def get_queryset(self):
        notifications = super().get_queryset()
        # return projects.filter(manager=self.request.user)
    #     # return services.filter(type_of__contains="Request Service")
        return notifications.all()

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('dash')