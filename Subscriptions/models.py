from random import choices

from django.db import models

from .choices import PaymentMethodChoices, PaymentCycleChoices


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey('Users.Profile', on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey('Plan',on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.plan.plan_name} Subscription for {self.user.username}"


class Plan(models.Model):
    plan_name = models.CharField(max_length=20)
    popular = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    benefits = models.ManyToManyField('PlanFAS', blank=True)

    def __str__(self):
        return f"{self.plan_name}"

class PlanFAS(models.Model):
    fas = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fas}"

class Payment(models.Model):
    cycle = models.CharField(
        max_length=3,
        choices=PaymentCycleChoices.choices,
        default=PaymentCycleChoices.MONTHLY
    )
    method = models.CharField(
        max_length=2,
        choices=PaymentMethodChoices.choices,
        default = PaymentMethodChoices.CREDIT_CARD
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.price} - {self.date}"