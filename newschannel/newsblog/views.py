from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
# Create your views here.
def index(request):

    item = News.objects.filter(label="Top").order_by('-held_date')

    sensitive_post = News.objects.filter(label='Sensitive').order_by('-held_date')

    latest_post = News.objects.filter(label='New').order_by('-held_date')

    top_post = News.objects.filter(label='Old').order_by('-held_date')

    context ={'item':item,'sensitive_post':sensitive_post,'latest_post':latest_post,'top_post':top_post}
    return render(request,'ren.html',context)
    # return render(request,'index1.html')

def by_category(request,cat):

    print(cat)
    print(cat.capitalize())
    cat1 = cat.lower()
    cat1 = cat1.capitalize()
    items=News.objects.filter(category=cat.capitalize()).order_by('-held_date')
    trending_post = News.objects.filter(label='Trending').order_by('-held_date')
    latest_post = News.objects.filter(label='New').order_by('-held_date')
    if items:
        context={'items':items,'cat':cat.upper(),'cat1':cat1,'trending_post':trending_post,'latest_post':latest_post}
        return render(request,'dispcat.html',context)
    elif cat=='news':
        items = News.objects.filter(label='Sensitive').order_by('-held_date')
        context={'items':items,'cat':cat.upper(),'trending_post':trending_post,'latest_post':latest_post}
        return render(request,'dispcat.html',context)
    elif cat=='index1.html':
        return render(request, 'index1.html')
    elif cat=='aboutus.html':
        return render(request, 'know.html')
    elif cat=='advertise':
        return render(request, 'index1.html')
    elif cat=='contact':
        return render(request, 'pages/contactus.html')
    elif cat=='writeforus':
        return render(request, 'index1.html')
    else:
        return render(request,'notfound.html')

def post(request,bycat,catty,id):

    item = News.objects.get(id=id)
    noshow = id
    related_post=News.objects.filter(category=bycat).order_by('-held_date')
    trending_post = News.objects.filter(label='Trending').order_by('-held_date')
    latest_post =News.objects.filter(label='New').order_by('-held_date')
    context={'item': item,'related_post':related_post,'noshow':noshow,'trending_post':trending_post,'latest_post':latest_post}
    return render(request, 'detail.html',context)


def by_search(request):
    give_search = request.GET.get('search')
    print(give_search)
    give_search= give_search.lower()
    give_search = give_search.capitalize()
    give_search_other=give_search.lower()
    items = News.objects.filter(category=give_search).order_by('-held_date')
    trending_post = News.objects.filter(label='Trending').order_by('-held_date')
    latest_post = News.objects.filter(label='New').order_by('-held_date')

    if items:
        context = {'items': items, 'cat': give_search.upper(), 'trending_post': trending_post,
                   'latest_post': latest_post,'value':give_search.capitalize()}
        return render(request, 'dispcat.html', context)
    elif give_search_other == 'news':

        items = News.objects.filter(label='Sensitive').order_by('-held_date')

        context = {'items': items, 'cat': give_search.upper(), 'trending_post': trending_post, 'latest_post': latest_post,'value':give_search_other.capitalize()}

        return render(request, 'dispcat.html', context)

    else:

        return render(request, 'notfound.html')






