from django.shortcuts import render, redirect
from django.contrib import messages
from shoes.forms import ShoesForm
from shoes.models import Shoes, Adminshoe
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
# Create your templates here.
def shoes(request):
    if request.method == 'POST':
        form = ShoesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Shoe added successfully")
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
        messages.info(request, "shoe edited successfully")
        return redirect('/show')
    return redirect(request, 'edit.html', {'shoes': shoes})


def check_out(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'checkout.html', {'shoes': shoes})

def mpesa(request,id):
    shoes = Shoes.objects.get(id=id)
    if request.method == 'POST':
        amount = shoes.shoes_price
        phoneNumber = request.POST.get('phonenumber')
        if not phoneNumber or not phoneNumber.isdigit:
            return HttpResponse('invalid phone number')
        if not amount or not amount.isdigit:
            return HttpResponse('invalid price')
        cl = MpesaClient()
        phone_number = int(phoneNumber)
        amount = int(amount)
        account_reference = 'SELL SHOES'
        transaction_desc = 'paying shoes'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "checkout.html", {"shoes": shoes})

def diplay(request):
    adminshoes = Adminshoe.objects.all()
    return render(request, 'displayforadmin.html', {'adminshoes': adminshoes})

def checkout(request, id):
    adminshoes = Adminshoe.objects.get(id=id)
    return render(request, "checkoutforadmin.html", {"adminshoes": adminshoes})


def checkoutpay(request, id):
    adminshoes = Adminshoe.objects.get(id=id)
    if request.method == 'POST':
        amount = adminshoes.shoesprice
        phoneNumber = request.POST.get('contact')
        if not phoneNumber or not phoneNumber.isdigit:
            return HttpResponse('invalid phone number')
        if not amount or not amount.isdigit:
            return HttpResponse('invalid price')
        cl = MpesaClient()
        phone_number = int(phoneNumber)
        amount = int(amount)
        account_reference = 'SELL SHOES'
        transaction_desc = 'paying shoes'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "checkoutforadmin.html", {"shoes": shoes})



def destory(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    messages.warning(request, "Shoe deleted successfully")
    return redirect('/show')
