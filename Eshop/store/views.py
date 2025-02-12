from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
import stripe
import json
from store.forms import ShippingForm
from django.contrib.auth.decorators import login_required

stripe.api_key = 'sk_test_51JKPAME9Zu8rS7a9XlPIVZy6EEMx39b4UeYQVxhhCqih8iLorshvhTmMEFVFHQWBUVfXQN14ZE3UP8lCNe8fXbrp001BLCzuIR'

def category(request, id):
    category = Product.objects.all()

    product = get_object_or_404(Product, category=id)
    id = product.category
#    category = Product.objects.get(category=id)
#    if category == id:
#        category.category = id
    context = {
        'id': id,
        'category': category,
    }
    return render(request, 'store/category.html', context)

def checkout(request):
    form = get_object_or_404(ShippingAddress, user=request.user)

    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)
def charge(request):
    if request.method == 'POST':
        try:
            print('Data:', request.POST)
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items

            form = get_object_or_404(ShippingAddress, user=request.user)
            price = float(order.get_cart_total)
            amount = int(price*100)
            number_phone = form.number_phone
            customer = stripe.Customer.create(
            phone=number_phone,
                email=request.user.email,
                name=form.user,
                source=request.POST['stripeToken']
            )

            charge = stripe.Charge.create(
                customer=customer,
                amount=amount,
                currency='usd',
                description="Shoping"
            )
            Order.objects.get_or_create(customer=customer, complete=True)
        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.error(self.request, f"{err.get('message')}")
            return redirect('store:menu')
        except stripe.error.APIConnectionError as e:
            messages.error(request, "Network Error")
            return redirect('store:menu')
        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            messages.error(request, "Not identified error")
            return redirect('store:menu')
    return redirect(reverse('store:success', args=[amount]))


def successMsg(request, args):
        '''sucess payment'''
        amount = args
        price = int(args/100)

        context = {
                'price': price,
        }
        return render(request, 'store/success.html', context)

def PaymentCompleted(request):
    body = json.loads(request.body)
    print("BODY: ",body)
    customer = request.user
#    product = Product.objects.get(id=body['productID'])
    Order.objects.create(
        customer=request.user,
        complete=True
    )
    return JsonResponse('Payment Completed', safe=False)

def shop(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = 0
        items = 0
        order = 0
#        data = json.loads(request.body)
#        action = data['action']
#        print('Action:', action)

    products = Product.objects.all()
    context = {
        'products': products,
	'cartItems': cartItems,
	'items': items,
	'order': order,
    }
    return render(request, 'store/menu.html', context)

@login_required
def cart(request):
    check = get_object_or_404(ShippingAddress, user=request.user)
    form = ShippingForm(request.POST or None, instance=check)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Some User Add Shipping Address ✔️')
            return redirect(reverse('store:checkout'))
        else:
            print('-------------------> Somthing Else :)')
            form = ShippingForm(request.POST or None)

    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    context = {
        'cartItems': cartItems,
        'items': items,
        'order': order,
        'form': form
    }
    return render(request, 'store/cart2.html', context)

def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        customer = request.user
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
                orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
                orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
                orderItem.delete()

        return JsonResponse('Item was added', safe=False)
def addToWishList(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)

    wishItem, created = WishItem.objects.get_or_create(customer=customer, product=productId)

    if action == 'add':
        wishItem.quantity = (wishItem.quantity + 1)
    elif action == 'remove':
        wishItem.quantity = (wishItem.quantity - 1)

    wishItem.save()

    if wishItem.quantity <= 0:
        wishItem.delete()

    return JsonResponse('Item was added To Wish List', safe=False)

def WishList(request):
    data = json.loads(request.body)
    productId = data['productId']
    product = Product.objects.get(id=productId)
    customer = request.user

    wishItem, created = WishItem.objects.get_or_create(customer=customer, product=product)
    items = wishItem.orderitem_set.all()
    cartItems = wishItem.get_total

    context = {
	'wishItem': wishItem,
	'items': items,
	'cartItems': cartItems
	}
    return render(request, 'store/wish.html', context)

def product(request, id):
    product = get_object_or_404(Product, id=id)
    photos = ProductImage.objects.filter(product=product)
    context = {
            'product': product,
            'photos': photos,
        }
    return render(request, 'store/product.html', context)

@login_required
def shipping(request):

    form = ShippingForm(request.POST or None, instance=check)

    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Some User Add Shipping Address ✔️')
            return redirect(reverse('store:checkout'))
        else:
            form = ShippingForm(request.POST or None)
    context = {
        'check': check,
        'form': form,
         'order': order
    }
    return render(request, 'store/checkout.html', context)
