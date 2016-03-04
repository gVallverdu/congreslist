from django.shortcuts import render

# Create your views here.


def congres_list(request):
    return render(request, 'congresList/congres_list.html', {})
