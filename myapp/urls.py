from django.urls import path
from myapp import views

urlpatterns = [
    path('last_30_days_cached_locks',
         views.last_30_days_page_cached_locks,
         name='last_30_days_cached_locks'),
    path('last_30_days_cached', views.last_30_days_page_cached, name='last_30_days_cached'),
    path('last_30_days', views.last_30_days_page, name='last_30_days'),

]
