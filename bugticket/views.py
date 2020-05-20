from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from bugticket.models import CustomUser, Ticket
from django.contrib.auth.decorators import login_required
from bugticket.forms import TicketForm

@login_required
def index(request):
    html = 'home.html'
    user_data = CustomUser.objects.all()
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, html, {'user_data':user_data, 'form':form})


@login_required
def signupView(request):
    html= 'signup.html'
    form=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password1'],
                
                )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, html, {'form': form}) 


def loginview(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user= authenticate(
                request, username = data['username'], 
                password= data['password']
                )
            if user:
                login(request, user)
                
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def ticket_details(request, id):
    html = 'ticketdetail.html'
    ticket = Ticket.objects.get(id=id)
    return render(request, html, {'ticket': ticket})

