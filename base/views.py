from django.shortcuts import render, redirect
from .forms import ReminderForm
from .models import Reminder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
    reminders = Reminder.objects.all()
    return render(request, 'home.html', {'reminders': reminders})



def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = ReminderForm()
    return render(request, 'registration/create_reminder.html', {'form': form})



def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})


 def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            messages.success(request, '✅ Reminder created successfully!')
            return redirect('base:home')
    else:
        form = ReminderForm()
    return render(request, 'create_reminder.html', {'form': form})
