import arrow

from myapp import models


def calculate_last_30_days() -> int:
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
    return slow_views
