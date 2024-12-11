from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .forms import SubscriptionForm
from .models import Plan, Subscription
from datetime import datetime, timedelta


class PricingView(ListView):
    template_name = 'subscriptions/pricing-page.html'
    model = Plan
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.all().order_by('price')


class PurchaseView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = SubscriptionForm
    template_name = 'subscriptions/purchase-page.html'
    model = Subscription
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        self.plan = get_object_or_404(Plan, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["plan"] = self.plan
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = self.request.user
        subscription = form.save(commit=False)
        subscription.plan = self.plan
        subscription.user = user
        subscription.end_date = datetime.now() + timedelta(days=30)
        subscription.save()
        self.object = subscription
        user.subscription = subscription
        user.save()
        return super().form_valid(form)


@login_required
def subscriptions_and_billing(request):
    return render(request, 'subscriptions/subscriptions-and-billing-page.html')


class CancelSubscription(DeleteView):
    template_name = 'subscriptions/pricing-page.html'
    model = Subscription
    success_url = reverse_lazy('pricing')
