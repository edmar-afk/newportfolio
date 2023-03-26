from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Counter, CounterHeart, CounterHaha, CounterWow, CounterSad, CounterAngry, VisitorCount

# Create your views here.


def main(request):
    num_likes = Counter.objects.all().count()
    num_heart = CounterHeart.objects.all().count()
    num_haha = CounterHaha.objects.all().count()
    num_wow = CounterWow.objects.all().count()
    num_sad = CounterSad.objects.all().count()
    num_angry = CounterAngry.objects.all().count()
    
    # Retrieve the visitor count object, or create a new one if it doesn't exist yet
    visitor_count, created = VisitorCount.objects.get_or_create(pk=1)

    if created:
        visitor_count.count = 1
        visitor_count.save()
   
    
    total = num_likes + num_heart + num_haha + num_wow + num_sad + num_angry
    context = {
        'num_likes': num_likes,
        'num_heart': num_heart,
        'num_haha': num_haha,
        'num_wow': num_wow,
        'num_sad': num_sad,
        'num_angry': num_angry,
        'total': total,
        'visitor_count': visitor_count.count,
    }
    return render(request, 'base.html', context)



def skills(request):
    return render(request, 'skills.html')


def about(request):
    return render(request, 'about.html')


def works(request):
    return render(request, 'works.html')

def comments(request):
    return render(request, 'comments.html')


@login_required
def counter(request):
  
    counter, created = Counter.objects.get_or_create(user=request.user)
    if created:
        counter.count = 1
        counter.save()
        
    else:
        counter.count = 0 
        
    if counter.count == 0:
        counter.delete()
        
    
   
    data = {'count': counter.count}
    return JsonResponse(data)





@login_required
def counterheart(request):
    counterheart, created = CounterHeart.objects.get_or_create(user=request.user)
    if created:
        counterheart.count = 1
        counterheart.save()    
    else:
        counterheart.count = 0    
    if counterheart.count == 0:
        counterheart.delete()
    data = {'count': counterheart.count}
    return JsonResponse(data)

@login_required
def counterhaha(request):
    counterhaha, created = CounterHaha.objects.get_or_create(user=request.user)
    if created:
        counterhaha.count = 1
        counterhaha.save()    
    else:
        counterhaha.count = 0    
    if counterhaha.count == 0:
        counterhaha.delete()
    data = {'count': counterhaha.count}
    return JsonResponse(data)


@login_required
def counterwow(request):
    counterwow, created = CounterWow.objects.get_or_create(user=request.user)
    if created:
        counterwow.count = 1
        counterwow.save()    
    else:
        counterwow.count = 0    
    if counterwow.count == 0:
        counterwow.delete()
    data = {'count': counterwow.count}
    return JsonResponse(data)


@login_required
def countersad(request):
    countersad, created = CounterSad.objects.get_or_create(user=request.user)
    if created:
        countersad.count = 1
        countersad.save()    
    else:
        countersad.count = 0    
    if countersad.count == 0:
        countersad.delete()
    data = {'count': countersad.count}
    return JsonResponse(data)


@login_required
def counterangry(request):
    counterangry, created = CounterAngry.objects.get_or_create(user=request.user)
    if created:
        counterangry.count = 1
        counterangry.save()    
    else:
        counterangry.count = 0    
    if counterangry.count == 0:
        counterangry.delete()
    data = {'count': counterangry.count}
    return JsonResponse(data)