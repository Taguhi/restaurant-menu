from django.conf.urls import url
from django.urls import include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Restuarant API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'restuarant/', include('api.restuarant.urls')),
]
