from django.urls import path
from .views import  PricingView,subscriptions_and_billing


urlpatterns = [
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('subscription&billing/', subscriptions_and_billing, name='subscriptions-and-billing'),
]
