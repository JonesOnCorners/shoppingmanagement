from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import *
from shop.forms import SupplierForm
from shop.forms import PaymentForm
from shop.filters import PaymentFilter
from shop.decorators import unauthenticated_users, allowed_users, admin_only

# Create your views here.

@login_required(login_url='login')
def home(request):
    payment = Payment.objects.all()
    supplier = Supplier.objects.all()

    total_suppliers = supplier.count()
    total_customers = supplier.count()

    completed_payments = payment.filter(status='Completed').count()
    pending_payments = payment.filter(status='Pending').count()
    partial_payments = payment.filter(status='Partial').count()
    advance_payments = payment.filter(status='Advance').count()
    overdue_payments = payment.filter(status='Overdue').count()

    print("completed_payments-->" ,completed_payments)
    print("pending_payments-->" ,pending_payments)

    context = {'payments':payment, 
               'suppliers': supplier,
               'pending_payments' : pending_payments,
               'partial_payments' : partial_payments,
               'completed_payments': completed_payments,
               'advance_payments': advance_payments,
               'overdue_payments' : overdue_payments,
               'total_suppliers': total_suppliers}
    return render(request,'shop/dashboard.html', context)



"""
LOGIN-LOGOUT VIEWS
"""
@unauthenticated_users
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Kindly Register First.')
            return redirect('login')
    context = {}
    return render(request, 'shop/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')



"""
SUPPLIER VIEWS
"""
@login_required(login_url='login')
def createSupplier(request):
    
    form = None
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Supplier Details Created Successfully!!!')
            return redirect('home')

    else:
        form = SupplierForm()

    context = {'form' : form}
    return render(request, 'shop/suppliercreateform.html', context)

@login_required(login_url='login')
def viewSupplier(request,pk):
    supplier = Supplier.objects.get(id=pk)
    payments = supplier.payment_set.all()
    
    total_payment = 0    

    myFilter = PaymentFilter(request.GET, queryset=payments)
    payments = myFilter.qs

    for payment in payments:
        if payment.transaction_type == 'Credit':
            total_payment -= payment.payment_done
        else:
            total_payment += payment.payment_done

    total_payment = "%.2f"%(total_payment)

    context = { 'supplier'  : supplier
                ,'payments' : payments
                ,'total_payment' : total_payment
                , 'myFilter' : myFilter}
    return render(request,'shop/supplier.html',context)

@login_required(login_url='login')
def addTransaction(request,pk):
    orderFormSet = inlineformset_factory(Supplier, Payment, fields=('bill_number','payment_done','transaction_type','status'), extra= 1)
    supplier = Supplier.objects.get(id=pk)
    formset = orderFormSet(queryset=Payment.objects.none(),instance=supplier)
  
    if request.method == 'POST':
        print(request.POST)
        formset = orderFormSet(request.POST,instance=supplier)
        if formset.is_valid():            
            formset.save()
            messages.success(request,'Transaction added!!!')
            params = int(pk)
            return redirect('view-supplier' , params)
    
    context ={ 'formset' : formset,
               'supplier' : supplier}
    return render(request,'shop/transactionform.html',context)