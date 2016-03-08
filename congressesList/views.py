from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Congress
from .forms import CongressForm
# Create your views here.


def congresses_list(request):
    congresses = Congress.objects.order_by("start_date")
    return render(request, 'congressesList/liste.html', {"congresses": congresses})


def congress_detail(request, congress_id):
    congress = get_object_or_404(Congress, pk=congress_id)
    return render(request, 'congressesList/details.html', {'congress': congress})


def new_congress(request):
    if request.method == "POST":
        form = CongressForm(request.POST)
        if form.is_valid():
            congre = form.save(commit=False)
            congre.author = request.user
            congre.created_date = timezone.now()
            congre.save()
            return redirect("congressesList.views.congresses_list")
    else:
        form = CongressForm()
    return render(request, "congressesList/new_congress.html", {"form": form})


def edit_congress(request, congress_id):
    congress = get_object_or_404(Congress, pk=congre_id)
    if request.method == "POST":
        form = CongressForm(request.POST, instance=congress)
        if form.is_valid():
            congress = form.save(commit=False)
            congress.author = request.user
            congress.created_date = timezone.now()
            congress.save()
            return redirect('congressesList.views.congresses_list')
    else:
        form = CongressForm(instance=congre)
    return render(request, 'congressesList/new_congress.html', {'form': form})