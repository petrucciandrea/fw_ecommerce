from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from . models import Category, Item, Cart, CartItem
from . forms import ProductForm, CategoryForm

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

def category_items_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)
    return render(request, "shop/items.html", {"items": items})

def item_detail_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
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
    return render(request, 'shop/cart.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, item__id=item_id)
    cart_item.delete()
    return redirect('cart_view')