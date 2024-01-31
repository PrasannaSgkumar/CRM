from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import Orderform, Customerform, Productform, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def home(request):
    return render(request, 'home.html')
def dashboard(request):
    order=Orders.objects.all()
    custo=Customer.objects.all()

    total_customers=Customer.objects.all().count()

    total_orders=Orders.objects.all().count()

    delivered=order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context={'order':order, 'custo':custo,'total_customers':total_customers,
                                                       'total_orders':total_orders, 'pending':pending,
                                                        'delivered':delivered}
    return render(request, 'dashboard.html', context)

def register(request):
    form=CreateUserForm()

    if request.method== "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request, 'register.html', context)


def loginPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        print(user)


    context = {}
    return render(request, 'login.html', context)

def products(request):
    product=Products.objects.all()
    return render(request, 'products.html.', {'pro':product})

def customers(request, pk):

    customer=Customer.objects.get(id=pk)
    orders=customer.orders_set.all()
    count=orders.count()
    context={'customer':customer, 'orders':orders, 'count':count}
    return render(request, 'customers.html', context)
# Create your views here.



def create_order(request, pk):
    customer=Customer.objects.get(id=pk)
    form = Orderform(initial={'customer':customer})
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'order_form.html', context)

def update_order(request, pk):
    order=Orders.objects.get(id=pk)
    form=Orderform(instance=order)

    if request.method == 'POST':
        form=Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order_form.html', context)

def delete_order(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)

def create_customer(request):
    form = Customerform()
    if request.method == 'POST':
        form=Customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'customer_form.html', context)

def product_create(request):
    form = Productform()
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'product_create.html', context)

def delete_product(request, pk):
    order = Products.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'product_delete.html', context)