from django.shortcuts import render, redirect
from shoes.forms import ShoesForm, PersonsForms
from shoes.models import Shoes, Persons
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
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


# def checkouttest(request):
#     if request.method == 'POST':
#         form = PersonsForms(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = PersonsForms()
#     return render(request, 'checkout.html', {'form': form})

def check_out(request, id):
    shoes = Shoes.objects.get(id=id)
    persons = Persons.objects.get(id=id)
    return render(request, 'checkout.html', {'persons': persons}, {'shoes': shoes})
def checkout(request, id):
    shoes = Shoes.objects.get(id=id)
    # persons = Persons.objects.get(id=id)
    form = ShoesForm(request.POST, instance=shoes)
    # cl = MpesaClient()
    # phone_number = '{}'.format(persons['phoneNumber'])
    # amount = '{}'.format(shoes['shoes_price'])
    # account_reference = 'SELL SHOES'
    # transaction_desc = 'paying shoes'
    # callback_url = 'https://api.darajambili.com/express-payment'
    # response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    if form.is_valid():
        form.save()
        return redirect("/mpesa")
    return render(request, 'checkout.html', {'shoes': shoes})

# def m_pesa(request, id):
#     shoes = Shoes.objects.get(id=id)
#     persons = Persons.objects.get(id=id)
#     # cl = MpesaClient()
#     # phone_number = '{}'.format(persons['phonenumber'])
#     # amount = '{}'.format(shoes["shoes_name"])
#     return render({'persons': persons}, {'shoes': shoes})

def mpesa(request):
    # shoes = Shoes.objects.get(id=id)
    # persons = Persons.objects.get(id=id)
    cl = MpesaClient()
    phone_number = '0701228521'
    amount = 1
    account_reference = 'SELL SHOES'
    transaction_desc = 'paying shoes'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def destory(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')
