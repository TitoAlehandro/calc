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

def index(request):
	if request.method == 'POST':
		form = RegForm(request.POST)
		
		if form.is_valid():
			template = loader.get_template("activate.html")

			try:
				
				send_mail('Активация аккаунта', 'Перейдите по ссылке http://www.calbook.tk/.', 'calculationbook@gmail.com',[form.data.get('email', None),])

			except:
				template = loader.get_template("error.html")
				context = RequestContext(request, {
						"error" : "Неизвестная ошибка.\n Мы уже работаем над этим. \n Попробуйте чуть позже.",
						})
		      #raise ValidationError(u'%s is not an even number' % request.POST['username'])
		      #raise Http404("Wrong order")
				return HttpResponse(template.render(context))
			user = User.objects.create_user(form.data.get('email', None), form.data.get('email', None), form.data.get('password', None))
			try:        
				user.save()
			except:
				user.delete()
				template = loader.get_template("error.html")
				context = RequestContext(request, {
						"error" : "Пользователь не создан.\n Попробуйте ввести снова.",
                })
				return HttpResponse(template.render(context))
    

			# user = User.objects.create_user(request.POST['username'], request.POST['username'], request.
                        
			#return HttpResponseRedirect('accounts/registrate/')
		else:
			if not request.user.is_anonymous():
				if not request.user.is_active():
					form = RegForm()
					return render_to_response('activate.html', 
								  {'form': form}, 
								  context_instance=RequestContext(request))
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

def about(request):
	template = loader.get_template("about.html")
	context = RequestContext(request, {
			"tpanel_partn": "index",
			})
	return HttpResponse(template.render(context))
