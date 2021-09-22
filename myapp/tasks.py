from celery import shared_task
from django.core.cache import cache

from myapp.helpers import calculate_last_30_days


@shared_task(name="generate_last_30_days_views")
def generate_last_30_days_views():
    cache.set("last_30_days", calculate_last_30_days(), 60)


@shared_task(name="generate_last_30_days_views_locks")
def generate_last_30_days_views_locks():
    with cache.lock("30_days_report", timeout=60, blocking_timeout=1):
        cache.set("last_30_days", calculate_last_30_days(), 60)


@shared_task(name="generate_last_30_days_v3")
def generate_last_30_days_days_v3():
    with cache.lock("30_days_report_locks_cache", timeout=60, blocking_timeout=1):
        cache.set("last_30_days_working", 1, 60)
        cache.set("last_30_days", calculate_last_30_days(), 60)
        cache.delete("last_30_days_working")


@shared_task(name="generate_last_30_days_v4")
def generate_last_30_days_v4():
    with cache.lock("30_days_report_locks_cache", timeout=60, blocking_timeout=1):
        cache.delete("last_30_days_task_sent")
        cache.set("last_30_days_working", 1, 60)
        cache.set("last_30_days", calculate_last_30_days(), 60)
        cache.delete("last_30_days_working")
