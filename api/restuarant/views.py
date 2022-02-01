import coreapi
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView

from restuarant.models import Restuarant
from .serializers import RestuarantSerializer

from rest_framework.filters import BaseFilterBackend


class NameFilterBackend(BaseFilterBackend):
	def get_schema_fields(self, view):
		return [coreapi.Field(
			name='name',
			location='query',
			required=False,
			type='string'
		)]

	def filter_queryset(self, request, queryset, view):
		name_param = request.query_params.get('name')
		if not name_param:
			return queryset

		return queryset.filter(name=name_param)


class RestuarantsView(ListCreateAPIView):
	filter_backends = (NameFilterBackend, )
	queryset = Restuarant.objects.all()
	serializer_class = RestuarantSerializer


class DeleteRestuarantView(UpdateAPIView, DestroyAPIView):
	lookup_field = 'name'
	queryset = Restuarant.objects.all()
	serializer_class = RestuarantSerializer
