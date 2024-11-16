from django import template

register = template.Library()

@register.filter
def exists(queryset):
    return queryset.exists()


@register.filter
def multiply(value, multiplier):
    try:
        return f'{int(value) * multiplier :.2f}'
    except (TypeError, ValueError):
         return value


@register.filter
def addTax(value, tax_percentage):
    try:
        tax =  int(value) * tax_percentage
        return f'{int(value) + tax :.2f}'
    except (TypeError, ValueError):
        return value