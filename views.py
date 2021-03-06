#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse
from book.models import *
from book.forms import RegForm
from django.shortcuts import render_to_response
from django.http import HttpResponse,  HttpResponseRedirect
from calc.book.tr import *
from django.core.mail import send_mail

from calc.book.views import calc_stat

def articles(request):
    template = loader.get_template("articles.html")
    context = RequestContext(request, {
    "tpanel_partn": "index",
    })
    return HttpResponse(template.render(context))
def news(request):
    news = InfoNews.objects.all().order_by('-date')

    template = loader.get_template("news.html")
    context = RequestContext(request, {
    "tpanel_partn": "index",
    "news" : news
    })
    return HttpResponse(template.render(context))
def blog(request):
    template = loader.get_template("blog.html")
    context = RequestContext(request, {
        "tpanel_partn": "index",
        })
    return HttpResponse(template.render(context))
def about(request):
    template = loader.get_template("about.html")
    context = RequestContext(request, {
    "tpanel_partn": "index",
    })
    return HttpResponse(template.render(context))

def index(request):
    if request.method == 'POST':
        form = RegForm(request.POST)

        try:
            user = User.objects.get(username=form.data.get('email', None))
        except User.DoesNotExist:
            if form.is_valid():
                template = loader.get_template("activate.html")
                try:
                    send_mail('Активация аккаунта', 'Перейдите по ссылке http://www.calbook.tk/ и введите логин и пароль.', 'calculationbook@gmail.com',[form.data.get('email', None),])
                except:
                    template = loader.get_template("error.html")
                    context = RequestContext(request, {
                    "error" : "Неизвестная ошибка.\n Мы уже работаем над этим. \n Попробуйте чуть позже.",
                    })
                    return HttpResponse(template.render(context))

                try:
                    user = User.objects.create_user(form.data.get('email', None), form.data.get('email', None), form.data.get('password', None))
                    user.save()
                    template = loader.get_template("error.html")
                    context = RequestContext(request, {
                        "error" : "Вам отправлено письмо с инструкцией по активации",
                        })
                    return HttpResponse(template.render(context))
                except:
                    user.delete()
                    template = loader.get_template("error.html")
                    context = RequestContext(request, {
                    "error" : "Пользователь не создан.\n Попробуйте ввести снова.",
                    })
                    return HttpResponse(template.render(context))
            else:
                if not request.user.is_anonymous():
                    if not request.user.is_active():
                        form = RegForm()
                        return render_to_response('activate.html',
                                                  {'form': form},
                                                  context_instance=RequestContext(request))
        template = loader.get_template("error.html")
        context = RequestContext(request, {
            "error" : "Пользователь с таким именем уже существует.\n Попробуйте другой.",
            })
        return HttpResponse(template.render(context))

    if not request.user.is_anonymous():
        template = loader.get_template("prods.html")
        bk_lst = Book.objects.filter(user_id=request.user).order_by('-date')
        pl_lst = Place.objects.filter(user_id=request.user).order_by('name')
        pr_lst = Product.objects.filter(user_id=request.user).order_by('name')
        #br_lst = Branch.objects.all().order_by('name')

        br_lst = calc_stat(request.user)



        context = RequestContext(request, {
        "rows": bk_lst,
        "branchs" : br_lst,
        "places" : pl_lst,
        "products" : pr_lst,
        "user" : request.user.username,

        })
        return HttpResponse(template.render(context))
    else:
        form = RegForm()
        return render_to_response('activate.html', {'form': form}, context_instance=RequestContext(request))