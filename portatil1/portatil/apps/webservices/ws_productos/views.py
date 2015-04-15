# Create your views here.
from django.http import HttpResponse
from portatil.apps.ventas.models import Portatil
from django.core import serializers


def ws_productos_view(request):
	data = serializers.serialize("json", Portatil.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')
	