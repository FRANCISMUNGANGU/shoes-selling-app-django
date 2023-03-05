from django.shortcuts import render, redirect
from shoes.forms import ShoesForm
from shoes.models import Shoes

# Create your templates here.
def shoes(request):
    if request.method == 'POST':
        form = ShoesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ShoesForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    shoes = Shoes.objects.all()
    return render(request, 'show.html', {'shoes': shoes})

def edit(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'edit.html', {'shoes': shoes})

def update(request, id):
    shoes = Shoes.objects.get(id=id)
    form = ShoesForm(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return redirect(request, 'edit.html', {'shoes': shoes})

def destory(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')
