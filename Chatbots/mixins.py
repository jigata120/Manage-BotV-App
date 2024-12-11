from django.db.models import Sum


class UserDataOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user

        allowed_groups = ['Administrators', 'Support']
        if user.is_staff or user.is_superuser or user.groups.filter(name__in=allowed_groups).exists():
            return super().dispatch(request, *args, **kwargs)

        chatbots = user.chatbots.all()
        user_pks = [
                       str(bot.id) for bot in chatbots
                   ] + [
                       str(bot.settings.id )for bot in chatbots
                   ] + [
                       str(bot.settings.context_data.id) for bot in chatbots
                   ]
        user_pks.append(user.id)
        print(user_pks)
        if str(self.kwargs.get('pk', 0)) not in user_pks:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("You do not have permission to access this object.")
        return super().dispatch(request, *args, **kwargs)

class ChatbotsContextsMixin:
    def get_context_data(self, **kwargs):
        kwargs.setdefault("view", self)
        kwargs = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            bots = self.request.user.chatbots
            bots_count = bots.count()
            active_bots_count = bots.filter(status=True).count()
            latest_bots = bots.filter(usage__isnull=False).order_by('-usage__updated_at')
            total_interactions_today = latest_bots.aggregate(
                total=Sum('usage__daily_interactions')
            )['total']
            total_tokens_usage_today = latest_bots.aggregate(
                total=Sum('usage__daily_tokens_usage')
            )['total']
            latest_4_bots = latest_bots[:2]
            latest_bot = latest_bots.first()
            if latest_bot:
                latest_usage = [latest_bot.usage]
            else:
                latest_usage = []
            kwargs['latest_bots'] = latest_bots
            kwargs['latest_4_bots'] = latest_4_bots
            kwargs['bots_count'] = bots_count
            kwargs['active_bots_count'] = active_bots_count
            kwargs['latest_bot'] = latest_bot
            kwargs['usages'] = latest_usage
            kwargs['total_interactions_today'] = total_interactions_today
            kwargs['total_tokens_usage_today'] = total_tokens_usage_today
        return kwargs

