from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.categories_view, name="categories"),
    path("categories/<int:category_id>/", views.category_items_view, name="category_items"),
    path("items/", views.items_view, name="items"),
    path("item/<int:item_id>/", views.item_detail_view, name="item_detail"),
    path("cart/", views.cart_view, name="cart_view"),
    path("cart/add/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
]
