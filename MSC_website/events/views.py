from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import Register

# Create your views here.

#for the main events page -- /events/
def home(request):
    return render(request,'events/home.html')


# for the registeration page -- /events/register/
def register(request):
    #Template for the form
    template = 'events/register.html'
    # request method POST
    if request.method == 'POST':
        # creating the form
        form = Register(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif User.objects.filter(roll_number=form.cleaned_data['roll_number']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Roll Number already exists.'
                })
            else:
        # Creating the user
                user = User.objects.create_user(
                    form.cleaned_data['email'],
                    form.cleaned_data['roll_number']
                )
                user.name = form.cleaned_data['name']
                user.branch = form.cleaned_data['branch']
                user.year = form.cleaned_data['year']
                user.college = form.cleaned_data['college']
                user.save()
                # redirect to successful registration page
                return HttpResponseRedirect('events/success.html')

    else:
        form = Register

    return render(request,template,{'form' : form})

