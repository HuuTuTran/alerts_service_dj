from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import alerts
from django.core.cache import cache

@receiver(post_save, sender=alerts)
@receiver(post_delete, sender=alerts)
def clear_alerts_cache(sender, **kwargs):
    cache.delete("alerts_list")
