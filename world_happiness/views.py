from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'active_page':'index'}
    return render(request, 'world_happiness/index.html', context)


def dashboard(request):
    context = {'active_page':'dashboard'}
    return render(request, 'world_happiness/dashboard.html', context)


def happiness(request):
    context = {'active_page':'happiness'}
    return render(request, 'world_happiness/happiness.html', context)


def economy(request):
    context = {'active_page':'economy'}
    return render(request, 'world_happiness/economy.html', context)


def family(request):
    context = {'active_page':'family'}
    return render(request, 'world_happiness/family.html', context)


def health(request):
    context = {'active_page':'health'}
    return render(request, 'world_happiness/health.html', context)


def freedom(request):
    context = {'active_page':'freedom'}
    return render(request, 'world_happiness/freedom.html', context)


def trust(request):
    context = {'active_page':'trust'}
    return render(request, 'world_happiness/trust.html', context)


def generosity(request):
    context = {'active_page':'generosity'}
    return render(request, 'world_happiness/generosity.html', context)


# bibliografia rapida
"""
https://www.coding2go.com/sidebar-menu
"""