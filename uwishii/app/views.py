from django.shortcuts import render
from .models import Order
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Status
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def menu(request):
    return render(request,'app/menu.html')

def about(request):
    return render(request,'app/about.html')

def jobs(request):
    return render(request,'app/jobs.html')

def contact(request):
    return render(request,'app/contact.html')


def shop(request):
    if request.method == "POST":
        current_user = request.user
        mainchoice = request.POST.get('set')
        rice = request.POST.get('rice')
        if rice == 'Plain Rice':
            cprice = 0
        else:
            cprice = 10
            

        if mainchoice == 'GOSET':
            order = Order(
                set = 'GOSET',
                user = current_user,
                rice = request.POST.get('rice'),
                price = 200 + cprice,
                main_dish = request.POST.get('main_dish'),
                side_dish = request.POST.get('side_dish'),
                second_side_dish = request.POST.get('second_side_dish'),
                dessert = request.POST.get('dessert')
            )
            order.save()
            messages.success(request, ("Added to cart successfully!"))
        elif mainchoice == 'SANSET':
            order = Order(
                set = 'SANSET',
                user = current_user,
                rice = request.POST.get('rice'),
                main_dish = request.POST.get('main_dish'),
                price = 150 + cprice,
                side_dish = request.POST.get('side_dish'),
                second_side_dish = 'None',
                dessert = 'None'
            )
            order.save()
            messages.success(request, ("Added to cart successfully!"))
        elif mainchoice =='YONSET':
            order = Order(
                set = 'YONSET',
                user = current_user,
                rice = request.POST.get('rice'),
                price = 175 + cprice,
                main_dish = request.POST.get('main_dish'),
                side_dish = request.POST.get('side_dish'),
                second_side_dish = request.POST.get('second_side_dish'),
                dessert = 'None'
            )
            order.save()
            messages.success(request, ("Added to cart successfully!"))
    return render(request, 'app/shop.html',{})


def add_status(request):
    if request.method == 'POST':
        orders = Order.objects.filter(user=request.user)
        for order in orders:
            set_value = order.set

            # Create a new Status object for each order and save it to the status database
            status = Status(
                user= request.user,
                address= 'NONE',
                contact= 'NONE',
                status='Pending',
                rice = order.rice,
                set = order.set,
                main_dish=order.main_dish,
                side_dish=order.side_dish,
                price=order.price,
            )

            if set_value == 'GOSET':
                status.second_side_dish = order.second_side_dish
                status.dessert = order.dessert

            elif set_value == 'YONSET':
                status.second_side_dish = order.second_side_dish

            # Save the status object
            status.save()
            messages.success(request, ("Your order has been placed!"))
        # Clear the content of Order.filter(user=request) by deleting the orders
        orders.delete()
            # Save the status object

    # Render your add_status template for the initial GET request
    return render(request, 'app/cart.html',{})

def orders(request):
    status = Status.objects.filter(user=request.user)
    return render(request,'app/orders.html', {'status': status})

def cart(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.price for order in orders)
    # Pass the orders data to the cart.html template
    return render(request, 'app/cart.html', {'orders': orders, 'total_price': total_price})
