from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchresult(request):
    products=None
    query=None
    count = int()
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        for i in products:
            count+=1

        return render(request,'search.html',{'query':query ,'products':products,'count':count})