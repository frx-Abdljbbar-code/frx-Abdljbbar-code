from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import ProfileForm, UserForm
from django.http import JsonResponse, HttpResponseRedirect
from store.models import *

# Create your views here.
def profile(request, slug):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, slug=slug)

        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        #order length
        context = {
            'order': order,
            'items': items,
            'cartItems': cartItems,
            'profile': profile,
        }
        return render(request, 'prof/profile.html', context)
    else:
        profile = get_object_or_404(Profile, slug=slug)
        context = {
            'profile': profile,
        }
        return render(request, 'prof/profile.html', context)
def edit_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
          #  return redirect('http://127.0.0.1:8000/profile/%s' % slug)
            return redirect('/profile/%s' % slug)
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
    }
    return render(request, 'prof/edit_profile.html', context)
