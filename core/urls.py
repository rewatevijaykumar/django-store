from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('product/<slug:slug>',ItemDetailView.as_view(),name='product'),
    path('add-to-cart/<slug:slug>',add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug:slug>',remove_from_cart, name="remove-from-cart"),
    path('remove-item-from-cart/<slug:slug>',remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('payment/<payment_option>/',PaymentView.as_view(),name='payment')
]
