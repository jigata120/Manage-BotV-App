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

@register.filter
def format_to_k(value):
    """
    924 -> 924
    1334 -> 1.3k
    1334214 -> 1,334k
    """
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value

    if value < 1000:
        return f"{value}"
    elif value < 1_000_000:
        return f"{value / 1000:.1f}K".replace('.0K', 'K')
    else:
        thousands = value / 1000
        return f"{thousands:,.1f}K".replace('.0K', 'K')


@register.filter(name='attr')
def attr(field, css):
    attr_name, value = css.split(':')
    return field.as_widget(attrs={attr_name: value})