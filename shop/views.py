from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from . models import Category, Item, Cart, CartItem, Order, OrderItem
from . forms import OrderForm, OrderStateForm, ProductForm, CategoryForm
from django.db.models import Avg, Count

def is_admin(user):
    return user.is_superuser

def categories_view(request):
    categories = Category.objects.all()
    form = CategoryForm() if request.user.is_superuser else None

    if request.method == "POST" and request.user.is_superuser:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")

    return render(request, "shop/categories.html", {
        "categories": categories,
        "form": form
    })

def items_view(request):
    items = Item.objects.all()
    form = ProductForm() if request.user.is_superuser else None

    if request.method == 'POST' and request.user.is_superuser:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items')

    return render(request, 'shop/items.html', {
        'items': items,
        'form': form,
    })

def home_view(request):
    categories = Category.objects.all()
    items_per_category = []
    for cat in categories:
        items = Item.objects.filter(category=cat).annotate(avg_stars=Avg('orderitem__review_star'),n_review=Count('orderitem__review_star'))
        items_per_category.append((cat, list(items)))
    return render(request, "shop/home.html", {"items_per_category": items_per_category})

def item_detail_view(request, item_id):
    item = get_object_or_404(Item.objects.annotate(avg_stars=Avg('orderitem__review_star'),n_review=Count('orderitem__review_star')), id=item_id)
    return render(request, "shop/item_detail.html", {"item": item})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.item.price * item.quantity for item in items)
    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, item__id=item_id)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for cart_item in cart_items:
                OrderItem.objects.create(
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    order=order
                )
            cart_items.delete()
            return redirect('orders_view')
    else:
        form = OrderForm()

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
    })

@login_required
def orders_view(request):
    if request.user.is_superuser:
        orders = Order.objects.all().select_related('user').prefetch_related('orderitem_set__item')
    else:
        orders = Order.objects.filter(user=request.user).prefetch_related('orderitem_set__item')

    for order in orders:
        order.total_price = sum(
            item.item.price * item.quantity for item in order.orderitem_set.all()
        )

    return render(request, 'shop/orders.html', {'orders': orders})

@user_passes_test(lambda u: u.is_superuser)
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderStateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
    return redirect('orders_view')

@login_required
def add_review(request, item_id):
    if request.method == "POST":
        review_text = request.POST.get("review_text")
        review_star = request.POST.get("review_star")
        order_item = get_object_or_404(OrderItem, item__id=item_id, order__user=request.user)

        if not order_item.review_text and not order_item.review_star:
            order_item.review_text = review_text
            order_item.review_star = int(review_star)
            order_item.save()

        return redirect("orders_view")
