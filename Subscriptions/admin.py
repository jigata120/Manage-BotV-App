from django.contrib import admin
from .models import Subscription, Payment, PlanFAS, Plan

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('user__username', 'plan__plan_name')
    readonly_fields = ('start_date',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'price')
    list_filter = ('price',)
    search_fields = ('plan_name',)

@admin.register(PlanFAS)
class PlanFASAdmin(admin.ModelAdmin):
    list_display = ('fas',)
    search_fields = ('fas',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price', 'date', 'cycle', 'method')
    list_filter = ('cycle', 'method', 'date')
    search_fields = ('price',)
    readonly_fields = ('date',)
