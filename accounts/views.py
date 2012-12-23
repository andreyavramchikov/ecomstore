from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            user_name = postdata.get('username','')
            password = postdata.get('password1','')
            new_user = authenticate(username=user_name,password=password)
            if new_user and new_user.is_active:
                login(request,new_user)
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
            
    else:
        form = UserCreationForm()
    
    page_title = "User Registration"
    return render_to_response(template_name,locals(),context_instance=RequestContext(request))


from django.contrib.auth.decorators import login_required
@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    name = request.user.username
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))
