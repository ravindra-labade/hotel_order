from django.shortcuts import render, redirect
from .forms import HotelForm
from .models import Hotel



def add_hotel(request):
    template_name = 'hotel/add.html'
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_hotel(request):
    template_name = 'hotel/show.html'
    orders = Hotel.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


def update_hotel(request, pk):
    template_name = 'hotel/add.html'
    obj = Hotel.objects.get(id=pk)
    form = HotelForm(instance=obj)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def cancel_hotel(request, pk):
    obj = Hotel.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'hotel/confirm.html')