from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegistrationForm, ContactUsForm
from django.contrib.auth import login, authenticate
from .models import HomeContent
from prof.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from store.models import Order
def about(request):
    return render(request, 'home/about.html')

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        prof = Profile.objects.all()
        contenthome = HomeContent.objects.all()

        context = {
           'cartItems': cartItems,
           'items': items,
           'order': order,
           'prof': prof,
           'contenthome': contenthome
        }
        return render(request, 'home/home.html', context)
    else:
        print('You Not Login...')
        prof = Profile.objects.all()
        contenthome = HomeContent.objects.all()
        context = {
       	    'prof': prof,
            'contenthome': contenthome
        }
        return render(request, 'home/home.html', context)
@login_required
def Contact(request):
    form = ContactUsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return HttpResponseRedirect('/')
        else:
            form = ContactUsForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'home/contact.html', context)

def signup(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            id = form.cleaned_data.get('id')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print(request, user, id)
            return HttpResponseRedirect('/')

        else:
            print("Your Form is Not Valid!\n")
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)
