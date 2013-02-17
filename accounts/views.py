#!/usr/bin/python
# -*- coding: utf-8 -*-

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse
from calc.book.tr import *
from calc.book.models import *
from calc.book.views import calc_stat

from calc.book.forms import RegForm
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.core.mail import send_mail
from django.http import Http404
from django.core.exceptions import ValidationError


from django.core.mail import send_mail

from django.contrib.auth.views import login, logout

@login_required
def profile(request):
    #template = loader.get_template("welcome.html")
    template = loader.get_template("prods.html")

    # get all list
    bk_lst = Book.objects.filter(user_id=request.user).order_by('-date')
    pl_lst = Place.objects.filter(user_id=request.user).order_by('name')
    pr_lst = Product.objects.filter(user_id=request.user).order_by('name')
    br_lst = Branch.objects.filter(user_id=request.user).order_by('name')

    br_lst = calc_stat(request.user)
    #calc_stat(br_lst)


    context = RequestContext(request, {
            "rows": bk_lst,
            "branchs" : br_lst,
            "places" : pl_lst,
            "products" : pr_lst,

            })
    return HttpResponse(template.render(context))


    #context = RequestContext(request, {
    #    "name": request.user.username,
    #    "date": request.user.date_joined,
    #})
    #return HttpResponse(template.render(context))
    #return HttpResponseRedirect(request.user.get_absolute_url())

def registrate(request):
    template = loader.get_template("activate.html")
    
    try:
        tr()
        send_mail('Активация аккаунта', 'Перейдите по ссылке http://www.calbook.tk/.', 'calculationbook@gmail.com',
                  [request.POST.get('username')], fail_silently=False)

    except:
        template = loader.get_template("error.html")
        context = RequestContext(request, {
                "error" : "Неверный email.\n Попробуйте ввести снова.",
                })
        #raise ValidationError(u'%s is not an even number' % request.POST['username'])
        #raise Http404("Wrong order")
        return HttpResponse(template.render(context))

    user = User.objects.create_user(request.POST['username'], request.POST['username'], request.POST['reg_pass'])
    try:        
        user.save()
    except:
        user.delete()
        template = loader.get_template("error.html")
        context = RequestContext(request, {
                "error" : "Пользователь не создан.\n Попробуйте ввести снова.",
                })
        return HttpResponse(template.render(context))
        
    
    
    request.user = user
    #login(request)
    
    #return HttpResponseRedirect(request.user.get_absolute_url())

  
    context = RequestContext(request, {
        "name": user.username,
        "date": user.date_joined,
    })
    return HttpResponse(template.render(context))

    # {'template_name': 'logout.html'}
    logout(request)
    #return HttpResponse(template.render(context))
    #return HttpResponseRedirect(request.user.get_absolute_url())


