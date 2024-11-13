from django.db import models
class PaymentCycleChoices(models.TextChoices):
    MONTHLY = 'mly', 'Monthly'
    YEARLY = 'yky', 'Yearly'
    OFFER = 'ofr', 'Custom Offer'

class PaymentMethodChoices(models.TextChoices):
    CREDIT_CARD = 'CC', 'Credit Card'
    PAYPAL = 'PP', 'PayPal'
    BANK_TRANSFER = 'BT', 'Bank Transfer'
    CRYPTOCURRENCY = 'CR', 'Cryptocurrency'