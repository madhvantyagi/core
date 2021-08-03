from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import auth
from .models import Profile

# Create your views here.

# When Login Successful set online = True
def profiles_login(request):

    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        print(user + " - " + password)
        
        user_User = auth.authenticate(username=user, password=password)
        if user_User is not None:
            auth.login(request, user_User)
            
            user_Profile = Profile.objects.filter(pk=user_User.id)
            user_Profile.update(is_online=True)
            
            print('Login Successful')
            
            return redirect('profiles-home')
        else:
            print('Invalid Creds')
    
    context = {}
    return render(request, 'login.html', context)

# When Logout, online = False
def profiles_logout(request):
    if request.user.is_authenticated:
        user_Profile = Profile.objects.filter(pk=request.user.pk)
        user_Profile.update(is_online=False)
        auth.logout(request)
        return HttpResponse('User Logged Out Successfully')
    else:
        return HttpResponse('No User was logged-in')
    
# Home Page where Logged In users are shown
def profiles_home(request):
    loggedin_users = Profile.objects.filter(is_online=True)
        
    context = {'loggedin_users' : loggedin_users}
    return render(request ,'profiles.html', context)