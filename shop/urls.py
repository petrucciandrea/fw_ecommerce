from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("categories/", views.categories_view, name="categories"),
    path("items/", views.items_view, name="items"),
    path("item/<int:item_id>/", views.item_detail_view, name="item_detail"),
    path("cart/", views.cart_view, name="cart_view"),
    path("cart/add/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path('checkout/', views.checkout_view, name='checkout'),
    path('orders/', views.orders_view, name='orders_view'),
    path('orders/complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
    path("add_review/<int:orderitem_id>/", views.add_review, name="add_review"),
]
