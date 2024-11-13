from django.utils import timezone


def is_day_gone(last_updated):
    today = timezone.now().date()
    return last_updated.date() < today

def is_month_gone(last_updated):
    today = timezone.now()
    first_day_of_this_month = today.replace(day=1)
    return last_updated.date() < first_day_of_this_month.date()

def reset_usage_if_needed():
    today = timezone.now().date()
    reset_applied = False
    from .models import Usage
    for usage in Usage.objects.all():
        if is_day_gone(usage.updated_at):
            usage.daily_interactions = 0
            usage.daily_tokens_usage = 0
            reset_applied = True

        if today.day == 1 and is_month_gone(usage.updated_at):
            usage.monthly_interactions = 0
            usage.monthly_tokens_usage = 0
            reset_applied = True

        if reset_applied:
            usage.save()

    return reset_applied


