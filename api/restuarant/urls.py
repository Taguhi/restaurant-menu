from django.conf.urls import url
from .views import RestuarantsView, DeleteRestuarantView


urlpatterns = [
    url(r'^$', RestuarantsView.as_view()),
    url(r'^(?P<name>[a-z,A-Z]+)/', DeleteRestuarantView.as_view()),
]
