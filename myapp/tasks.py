from celery import shared_task
from django.core.cache import cache

from myapp.helpers import calculate_last_30_days


@shared_task(name="generate_last_30_days_views")
def generate_last_30_days_views():
    cache.set("last_30_days", calculate_last_30_days(), 60)


@shared_task(name="generate_last_30_days_views_locks")
def generate_last_30_days_views():
    with cache.lock("30_days_report", timeout=60, blocking_timeout=1):
        cache.set("last_30_days", calculate_last_30_days(), 60)
