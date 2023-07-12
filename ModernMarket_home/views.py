from genericpath import exists
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Wishlist, Order, Wallet


# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):

    if request.method=='POST':
        ifname=request.POST['fname']
        ilname=request.POST['lname']
        iemail=request.POST['email']
        iusername=request.POST['username']
        ipassword=request.POST['password']
        ire_password=request.POST['re_password']

        if ipassword==ire_password:
            if User.objects.filter(username=iusername).exists():
                    #username already exists
                    messages.error(request, "username already exists")
                    return render(request, 'signup.html')
            elif User.objects.filter(email=iemail).exists():
                # email already exists
                messages.error(request, "email already exists")
                return render(request, 'signup.html')
            
            iuser = User.objects.create_user(username=iusername, email=iemail, password=ipassword, first_name=ifname, last_name=ilname)
            iuser.save()
            iwallet=Wallet(user=iuser)
            iwallet.save()
            messages.success(request,"Registered Successfully! Login to continue");
            return redirect('login')

        else:
            messages.error(request, "both passwords should match!!")    
            return render(request,'signup.html')

    return render(request,'signup.html')


def login(request):     
    if request.method == 'POST':
        iusername = request.POST['username']
        ipassword = request.POST['password']
        iuser = auth.authenticate(username=iusername, password=ipassword)
        if iuser is not None:
            auth.login(request, iuser)
            messages.success(request,"Logged in Successfully!");
            return redirect('home')
        
        messages.error(request, "invalid username/password")
        return redirect('login')
    return render(request,'login.html')






def logout(request):
    auth.logout(request)
    messages.success(request,"Logged out Successfully!");
    return redirect('home')



def productpage(request):
    
    if request.method == 'POST':
        isearched_items=request.POST.get('searched_item')
        imin_price=request.POST.get('min_price',False)
        imax_price=request.POST.get('max_price',False)
        if imin_price ==False:
            imin_price=0
        if imax_price ==False:
            imax_price=1000000000
        if imin_price=='':
            imin_price=0
        if imax_price=='':
            imax_price=1000000000

        all_products1=Product.objects.filter(p_category__icontains=isearched_items).union( Product.objects.filter(p_name__icontains=isearched_items)).union( Product.objects.filter(p_description__icontains=isearched_items))
        all_products2=Product.objects.filter(p_price__range=(imin_price,imax_price))
        all_products1=all_products1.intersection(all_products2)
        context={
            'products':all_products1,
            'yousearched':isearched_items
        }
        return render(request,'productpage.html',context)
    else:
        all_products = Product.objects.all()
        context={
            'products':all_products,
        }
        return render(request,'productpage.html',context)

def productdetails(request,pk):
    thisproduct=Product.objects.get(id=pk)
    context={
        'product':thisproduct,
    }
    return render(request,'productdetails.html',context)

def cart(request):
    if request.method == 'POST':
        item_id=request.POST['item_id']
        #remove item
        entry= Cart.objects.get(id= item_id)
        entry.delete()

    cart_items = Cart.objects.filter(user=request.user)

    context={
        'cart_items':cart_items
    }
    return render(request,'cart.html',context)

@login_required(login_url="/login/")
def wishlist(request):

    if request.method == 'POST':
        item_id=request.POST['item_id']
        #remove item
        entry= Wishlist.objects.get(id = item_id)
        entry.delete()


    wishlist_items = Wishlist.objects.filter(user=request.user)

    context={
        'wishlist_items':wishlist_items
    }
    return render(request,'wishlist.html',context)

@login_required(login_url="/login/")
def addtocart(request):
    if request.method=='POST':
        product_id=request.POST['product_id']
        thisproduct=Product.objects.get(id=product_id)

        if Cart.objects.filter(user=request.user,product=thisproduct).exists():
            cart_item=Cart.objects.get(user=request.user,product=thisproduct)
            cart_item.quantity=1+cart_item.quantity
            cart_item.save()
        else: 
            new_item= Cart(user=request.user, product=thisproduct,quantity=1)
            new_item.save()
    return redirect(f'/productpage/{product_id}/')

@login_required(login_url="/login/")
def addtowishlist(request):
    if request.method =='POST':
        product_id=request.POST['product_id']
        thisproduct=Product.objects.get(id=product_id)

        if Wishlist.objects.filter(user=request.user,product=thisproduct).exists():
            pass
        else: 
            new_item= Wishlist(user=request.user, product=thisproduct)
            new_item.save()
    return redirect(f'/productpage/{product_id}/')

@login_required(login_url="/login/")
def orderlist(request):
    all_orders=Order.objects.filter(user=request.user)
    all_orders=all_orders[::-1]
    context={
        'orders':all_orders
    }
    return render(request,'orderlist.html',context)

@login_required(login_url="/login/")
def checkout(request):
    
    if request.method =='POST':
        product_id=request.POST['product_id']
        thisproduct=Product.objects.get(id=product_id)
        products=[thisproduct]
    else:    
        cart_items=Cart.objects.filter(user=request.user)
        products = [c.product for c in cart_items]
    total_cost=0
    for p in products:
        total_cost+=p.p_price
    wallet=Wallet.objects.filter(user=request.user)
    wallet=wallet[0]
    balance=wallet.balance
    if balance>=total_cost:
        possible=True
    else:
        possible=False

    context={
        'products':products,
        'total_cost':total_cost,
        'possible':possible
    }
    return render(request,'checkout.html',context)


@login_required(login_url="/login/")
def placeorder(request):
    if request.method=='POST':
        product_ids=request.POST.getlist('product_ids')
        products = Product.objects.filter(id__in=product_ids)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        addr = request.POST.get('address')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        wallet=Wallet.objects.filter(user=request.user)
        wallet=wallet[0]
        for p in products:
            order = Order(
                fname=fname,
                lname=lname,
                price=p.p_price,
                email=email,
                product=p,
                addr1=addr,
                phoneNum=phoneno,
                user=request.user
            )
            wallet.balance-=p.p_price
            order.save()
        wallet.save()
            
    return redirect('orderlist')
        
@login_required(login_url="/login/")
def orderdetails(request,pk):
    thisorder=Order.objects.filter(id=pk,user=request.user)
    
    context={
        'order':thisorder[0]
    }
    return render(request,'orderdetails.html',context)


@login_required(login_url="/login/")
def modifyrating(request):
    if request.method=='POST':
        rating_value=request.POST.get('rating_value')
        order_id=request.POST.get('order_id')
        order_item=Order.objects.filter(id=order_id)
        order_item=order_item[0]
        order_item.rated=rating_value
        product=order_item.product
        sum=product.p_ratecount*product.p_rating
        product.p_ratecount+=1
        product.p_rating=(float(sum)+float(rating_value))/product.p_ratecount
        product.save()
        order_item.save()

    return redirect(f'/orderlist/{order_id}/')

def myprofile(request):
    wallet=Wallet.objects.filter(user=request.user)
    wallet=wallet[0]
    context={
        'wallet':wallet
    }
    print(wallet.balance)
    return render(request,'myprofile.html',context)
