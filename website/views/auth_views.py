from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.contrib import messages


from website.forms import UserForm, ProfileForm
from website.models import Profile

def register(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    registered = False


    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print("valid")

            form_data = request.POST
            state = form_data["state"]
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = Profile.objects.create(state=state, user=user)
            profile.save()

            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = ProfileForm()
        template_name = 'register.html'
        context = {'user_form': user_form, 'next': request.GET.get('next', '/'), 'profile_form': profile_form}
        return render(request, template_name, context)


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    context = {'next': request.GET.get('next', '/')}

    if request.method == 'POST':

        username=request.POST['username']
        password=request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            if request.POST.get('next') == '/':
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(request.POST.get('next', '/'))

        else:
            messages.error(request, "Login failed. Your username or password is incorrect.")

    return render(request, 'login.html', context)


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')