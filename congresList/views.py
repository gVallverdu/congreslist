from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Congre
from .forms import CongreForm
# Create your views here.


def congres_list(request):
    congres = Congre.objects.order_by("start_date")
    return render(request, 'congresList/first.html', {"congres": congres})


def new_congre(request):
    if request.method == "POST":
        form = CongreForm(request.POST)
        if form.is_valid():
            congre = form.save(commit=False)
            congre.author = request.user
            congre.created_date = timezone.now()
            congre.save()
            return redirect("congresList.views.congres_list")
    else:
        form = CongreForm()
    return render(request, "congresList/new_congre.html", {"form": form})


def edit_congre(request, pk):
    congre = get_object_or_404(Congre, pk=pk)
    if request.method == "POST":
        form = CongreForm(request.POST, instance=congre)
        if form.is_valid():
            congre = form.save(commit=False)
            congre.author = request.user
            congre.created_date = timezone.now()
            congre.save()
            return redirect('congresList.views.congres_list')
    else:
        form = CongreForm(instance=congre)
    return render(request, 'congresList/new_congre.html', {'form': form})
