import arrow
import factory
from myapp import models


class PageViewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PageView

    created_dt = factory.Faker(
        'date_between_dates',
        date_start=arrow.now().shift(days=-60).datetime,
        date_end=arrow.now().datetime
    )
    url = factory.Faker('uri_path', deep=3)
    response_time_ms = factory.Faker('pyint', min_value=20, max_value=40000)
