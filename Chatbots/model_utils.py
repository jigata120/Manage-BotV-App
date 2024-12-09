from django.utils import timezone
from django.utils.timezone import now

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


def custom_timesince(updated_at):
    """
    Mimics Django's timesince functionality for a human-readable difference.
    """
    time_difference = now() - updated_at


    if time_difference.days > 0:
        if time_difference.days == 1:
            return "1 day ago"
        return f"{time_difference.days} days ago"


    hours = time_difference.seconds // 3600
    if hours > 0:
        if hours == 1:
            return "1 hour ago"
        return f"{hours} hours ago"


    minutes = (time_difference.seconds % 3600) // 60
    if minutes > 0:
        if minutes == 1:
            return "1 minute ago"
        return f"{minutes} minutes ago"


    seconds = time_difference.seconds % 60
    if seconds == 1:
        return "1 second ago"
    return f"{seconds} seconds ago"