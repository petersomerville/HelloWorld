from django.shortcuts import render, redirect
from django.contrib import messages
from apps.travel_app.models import User

def index(request):
    return render(request, 'travel_app/index.html')

def planes(request):
    return render(request, 'travel_app/planes.html')

def trains(request):
    return render(request, 'travel_app/trains.html')
    
def automobiles(request):
    return render(request, 'travel_app/automobiles.html')
    
def boats(request):
    return render(request, 'travel_app/boats.html')
    
def login(request):
    if 'user_id' in request.session:
        return redirect('travel_app:index')
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST['html_email'])
            if request.POST['html_password'] == user.password:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('travel_app:index')
            else:
                messages.error(request, 'Invalid login')
                return redirect('travel_app:login')
        except:
            messages.error(request, 'Invalid login')    
            return redirect('travel_app:login')

    return render(request, 'travel_app/login.html')

    
def logout(request):
    request.session.clear()
    return redirect('travel_app:index')

def register(request):
    if 'user_id' in request.session:
        return redirect('travel_app:index')
    if request.method == 'POST':
        if len(request.POST['html_email']) > 0 and request.POST['html_password'] == request.POST['html_confirm']:
            try:
                user = User.objects.create(email = request.POST['html_email'], password = request.POST['html_password'])
                request.session['user_id'] = user.id
                request.session['email'] = user.email
            except:
                messages.error(request,'Account already in use, Bitches')
                return redirect('travel_app:register')

        return redirect('travel_app:index')
    return render(request, 'travel_app/register.html')
    