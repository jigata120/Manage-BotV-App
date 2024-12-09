from django.urls import path
from .views import PricingView, subscriptions_and_billing, PurchaseView, CancelSubscription

urlpatterns = [
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('Purchase/<int:pk>', PurchaseView.as_view(), name='purchase'),
    path('subscription&billing/', subscriptions_and_billing, name='subscriptions-and-billing'),
    path('cancel/<int:pk>', CancelSubscription.as_view(), name='cancel-sub'),

]
