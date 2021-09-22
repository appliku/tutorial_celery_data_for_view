from django.urls import path
from myapp import views

urlpatterns = [
    path('last_30_days_v4',
         views.last_30_days_page_v4,
         name='last_30_days_v4'),
    path('last_30_days_v3',
         views.last_30_days_page_v3,
         name='last_30_days_v3'),
    path('last_30_days_cached_locks',
         views.last_30_days_page_cached_locks,
         name='last_30_days_cached_locks'),
    path('last_30_days_cached', views.last_30_days_page_cached, name='last_30_days_cached'),
    path('last_30_days', views.last_30_days_page, name='last_30_days'),

]
