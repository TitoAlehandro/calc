from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse,  HttpResponseRedirect
from models import *
from calc.book.tr import *
import datetime
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    template = loader.get_template("index.html")
    

    bk_lst = Book.objects.filter(user_id=request.user).order_by('-date') ;
    pl_lst = Place.objects.all().order_by('name') ;
    pr_lst = Product.objects.all().order_by('name') ;
    br_lst = Branch.objects.all().order_by('name') ;

    
    context = RequestContext(request, {
            "rows": bk_lst,
            "branchs" : br_lst,
            "places" : pl_lst,
            "products" : pr_lst,
            "user" : request.user.username,
            
            })
    return HttpResponse(template.render(context))

def add(request):
    template = loader.get_template("index.html")
    
    bk = Book()    
    bk.price = request.POST['book_pr']
    
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
        pl.save()

    try:
        pr = Product.objects.get(name=request.POST['nm-menu'])
    except ObjectDoesNotExist:
        pr = Product()
        pr.name = name=request.POST['nm-menu']
        pr.save()

    try:
        br = Branch.objects.get(name=request.POST['br-menu'])
    except ObjectDoesNotExist:
        br = Branch()
        br.name = name=request.POST['br-menu']
        br.save()    
        
    bk.place_id = pl
    bk.product_id = pr
    bk.branch_id = br
    
    bk.user_id = request.user
    
    bk.save()
    
    bk_lst = Book.objects.filter(user_id=request.user).order_by('-date') ;
    pl_lst = Place.objects.all().order_by('name') ;
    pr_lst = Product.objects.all().order_by('name') ;
    br_lst = Branch.objects.all().order_by('name') ;

    
    
    context = RequestContext(request, {
            "rows": bk_lst,
            "branchs" : br_lst,
            "places" : pl_lst,
            "products" : pr_lst,
            
            })
  
    return HttpResponse(template.render(context))


def delrow(request):
    template = loader.get_template("index.html")

    # get row 
    id_ = request.POST['book_id']
    row = Book.objects.get(id=id_)   
    # delete row
    row.delete()

    # get all list
    bk_lst = Book.objects.filter(user_id=request.user).order_by('-date') ;
    pl_lst = Place.objects.all().order_by('name') ;
    pr_lst = Product.objects.all().order_by('name') ;
    br_lst = Branch.objects.all().order_by('name') ;

    
    
    context = RequestContext(request, {
            "rows": bk_lst,
            "branchs" : br_lst,
            "places" : pl_lst,
            "products" : pr_lst,
            
            })
    return HttpResponse(template.render(context))
