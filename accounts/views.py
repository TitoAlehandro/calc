# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse
from calc.book.tr import *

@login_required
def profile(request):
    template = loader.get_template("welcome.html")
    context = RequestContext(request, {
        "name": request.user.username,
        "date": request.user.date_joined,
    })
    return HttpResponse(template.render(context))
    #return HttpResponseRedirect(request.user.get_absolute_url())
