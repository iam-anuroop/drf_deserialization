from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import Studentserializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def student_createview(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = Studentserializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

# Create your views here.
