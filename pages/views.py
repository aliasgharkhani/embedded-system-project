from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import json
from .serializers import ModuleLogSerializer
from .models import ModuleLog
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from datetime import datetime

# class ModuleLogViewSet(viewsets.ModelViewSet):
#     # return render(request, 'D:\\education\\98-99-2\\embeded system\\project\\server\\server\\pages\\index.html')
#     # try:
#     queryset = ModuleLog.objects.all().order_by('module_id')
#     serializer_class = ModuleLogSerializer
#
#
#     # def get(self, request, *args, **kwargs):
#     #     data = ModuleLogSerializer([]).data
#     #     # if request.accepted_renderer.format == 'html':
#     #     #     return Response(data, template_name='blah.html')
#     #
#     #     return HttpResponse("<h1>MyClub Event Calendar={}</h1>".format(13))
#     # height = json.loads(request.body)
#     # weight = str(height * 10)
#     # return HttpResponse("<h1>MyClub Event Calendar={}</h1>".format(weight))
#     # except ValueError as e:
#     # return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(('GET','POST'))
def my(request):
    """Renders the contact page."""
    if request.method == 'POST':
        s = ModuleLogSerializer(data=request.POST)
        if s.is_valid():
            s.save()
            return Response(status=201)
    else:
        queryset = ModuleLog.objects.all()
        serializer_class = ModuleLogSerializer(queryset,many=True)

        return render(
            request,
            'index.html',
            {
                'data':serializer_class.data,
            }
        )


