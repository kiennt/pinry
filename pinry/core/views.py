from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.conf import settings
from pinry.core.models import Member


def home(request):
    return HttpResponseRedirect(reverse('pins:recent-pins'))


def private(request):
    return TemplateResponse(request, 'core/private.html', None)


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('pins:recent-pins'))

    if not settings.ALLOW_NEW_REGISTRATIONS:
        messages.error(request, "The admin of this service is not "
                                "allowing new registrations.")
        return HttpResponseRedirect(reverse('pins:recent-pins'))

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member.objects.create(user=user)

            messages.success(request, 'Thank you for registering, you can now '
                                      'login.')
            return HttpResponseRedirect(reverse('core:login'))
    else:
        form = UserCreationForm()

    return TemplateResponse(request, 'core/register.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:home'))

    message = ""
    next_page = request.GET.get('next', reverse('core:home'))
    form = AuthenticationForm(None, request.POST or None)

    if form.is_valid():
        user = form.get_user()
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(next_page)
        else:
            message = "Your account is not active. Please contact the admin"
    else:
        message = "Your username and/or password were incorrect"

    return TemplateResponse(request, 'core/login.html', {
                'form': form, 'message': message
            })

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect(reverse('core:home'))
