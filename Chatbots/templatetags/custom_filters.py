from django import template

register = template.Library()

@register.filter
def format_number(value):
    """
    1000 -> "1,000"
    """
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value
