import arrow
from celery import current_app
from django.shortcuts import render
from myapp import models
from django.core.cache import cache


def last_30_days_page(request, *args, **kwargs):
    threshold_dt = arrow.now().shift(days=-30).datetime
    qs = models.PageView.objects.all()
    slow_views = 0
    page_view: models.PageView
    for page_view in qs.iterator():
        if page_view.response_time_ms < 1000:
            continue
        if page_view.created_dt < threshold_dt:
            continue
        if page_view.url.find('blog') == -1:
            continue
        slow_views += 1

    return render(
        request,
        template_name="myapp/last_30_days_report.html",
        context={
            "slow_views": slow_views
        })


def last_30_days_page_cached(request, *args, **kwargs):
    slow_views = cache.get("last_30_days")
    if slow_views is None:
        current_app.send_task("generate_last_30_days_views", queue="default", ignore_result=True)
    return render(
        request,
        template_name="myapp/last_30_days_report_cached.html",
        context={
            "slow_views": slow_views
        })


def last_30_days_page_cached_locks(request, *args, **kwargs):
    slow_views = cache.get("last_30_days")
    if slow_views is None:
        current_app.send_task(
            "generate_last_30_days_views_locks",
            queue="default",
            ignore_result=True)
    return render(
        request,
        template_name="myapp/last_30_days_report_cached.html",
        context={
            "slow_views": slow_views
        })


def last_30_days_page_v3(request, *args, **kwargs):
    slow_views = cache.get("last_30_days")
    last_30_days_working = cache.get("last_30_days_working")
    if slow_views is None and not last_30_days_working:
        current_app.send_task(
            "generate_last_30_days_v3",
            queue="default",
            ignore_result=True)
    return render(
        request,
        template_name="myapp/last_30_days_report_cached.html",
        context={
            "slow_views": slow_views
        })


def last_30_days_page_v4(request, *args, **kwargs):
    slow_views = cache.get("last_30_days")
    last_30_days_task_sent = cache.get("last_30_days_task_sent")
    last_30_days_working = cache.get("last_30_days_working")
    if slow_views is None and not last_30_days_working and not last_30_days_task_sent:
        cache.set("last_30_days_task_sent", 1, 60)
        current_app.send_task(
            "generate_last_30_days_v4",
            queue="default",
            ignore_result=True)
    return render(
        request,
        template_name="myapp/last_30_days_report_cached.html",
        context={
            "slow_views": slow_views
        })
