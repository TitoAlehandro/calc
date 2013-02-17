#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse,  HttpResponseRedirect
from calc.book.tr import *
from calc.book.models import *
from math import trunc

import datetime
from django.core.exceptions import ObjectDoesNotExist
from forms import RegForm
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST 

#def index(request):



def add(request):
    template = loader.get_template("prods.html")
    
    bk = Book()  
    try:
        bk.price = float(request.POST['book_pr'])
    except:
        template = loader.get_template("error.html")
        context = RequestContext(request, {
                "error" : "Неверно введена цена товара.\n Попробуйте ввести без пробелов.",
                })
        
        return HttpResponse(template.render(context))
    
    
    dt = request.POST['book_dt']
    if len(dt) > 6:
        bk.date = dt
    else:
        bk.date = datetime.datetime.now()
    
    try:
        pl = Place.objects.get(name=request.POST['pl-menu'])
    except ObjectDoesNotExist:
        pl = Place()
        pl.name = request.POST['pl-menu']
        pl.user_id = request.user
        pl.save()

    try:
        pr = Product.objects.get(name=request.POST['nm-menu'])
    except ObjectDoesNotExist:
        pr = Product()
        pr.name = name=request.POST['nm-menu']
        pr.user_id = request.user
        pr.save()

    try:
        br = Branch.objects.get(name=request.POST['br-menu'])
    except ObjectDoesNotExist:
        br = Branch()
        br.name = name=request.POST['br-menu']
        br.user_id = request.user
        br.save()    
        
    bk.place_id = pl
    bk.product_id = pr
    bk.branch_id = br
    
    bk.user_id = request.user
    
    bk.save()
    
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


def delrow(request):
    template = loader.get_template("prods.html")

    # get row 
    id_ = request.POST['book_id']
    row = Book.objects.get(id=id_)   
    # delete row
    row.delete()

    # get all list
    bk_lst = Book.objects.filter(user_id=request.user).order_by('-date') ;
    pl_lst = Place.objects.filter(user_id=request.user).order_by('name') ;
    pr_lst = Product.objects.filter(user_id=request.user).order_by('name') ;
    br_lst = Branch.objects.filter(user_id=request.user).order_by('name') ;

    br_lst = calc_stat(request.user)
    
    
    context = RequestContext(request, {
            "rows": bk_lst,
            "branchs" : br_lst,
            "places" : pl_lst,
            "products" : pr_lst,
            
            })
    return HttpResponse(template.render(context))
def calc_stat(id_user):
    bk_lst = Book.objects.filter(user_id=id_user).order_by('-date')
    #pl_lst = Place.objects.filter(user_id=id_user).order_by('name')
    pr_lst = Product.objects.filter(user_id=id_user).order_by('name')
    br_lst = Branch.objects.filter(user_id=id_user).order_by('name')

    tot = 0
    for pr in bk_lst: tot = tot + pr.price
    for br in br_lst:
        br.stat = 0
        br.stat_money = 0
        for pr in bk_lst:
            if pr.branch_id == br:
                br.stat = br.stat + pr.price
        br.stat_money = br.stat
        br.stat_currency = 'руб.'
        if tot == 0:
            br.stat=100
        else:
            br.stat=trunc((br.stat / tot)*100)
    return br_lst



