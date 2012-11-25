# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse
from calc.book.tr import *
<<<<<<< HEAD
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.core.mail import send_mail
=======
>>>>>>> aac6b884346dd56421712c0b014b825e17a5b894

@login_required
def profile(request):
    template = loader.get_template("welcome.html")
    context = RequestContext(request, {
        "name": request.user.username,
        "date": request.user.date_joined,
    })
    return HttpResponse(template.render(context))
    #return HttpResponseRedirect(request.user.get_absolute_url())
def registrate(request):
    template = loader.get_template("activate.html")
    
    user = User.objects.create_user(request.POST['username'], request.POST['username'], request.POST['reg_pass'])
    user.save()
    
    request.user = user
    #login(request)
    
    #return HttpResponseRedirect(request.user.get_absolute_url())

    send_mail('Subject here', 'Here is the message.', 'from@example.com',
    [request.POST['username']], fail_silently=False)

    context = RequestContext(request, {
        "name": user.username,
        "date": user.date_joined,
    })
    return HttpResponse(template.render(context))
