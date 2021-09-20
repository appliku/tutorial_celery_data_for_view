from django.db import models


class PageView(models.Model):
    url = models.CharField(max_length=255)
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    response_time_ms = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Page View'
        verbose_name_plural = 'Page Views'
        ordering = ('-pk',)

    def __str__(self):
        return self.url
