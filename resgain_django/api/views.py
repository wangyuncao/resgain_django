from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from rest_framework.views import APIView

import json
from api import models


# Create your views here.


def resgain(request):
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
        sexual = models.Sexual.objects.all()
        paginator = Paginator(sexual, 30)
        sexual_page = paginator.page(page_num)

        return render(request, 'sexual.html', {'sexual': sexual_page})


def complete(request):
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
        sexual_id = int(request.GET.get('sexual_id', 1))
        sexual = models.CompleteInformation.objects.filter(sexual_id=sexual_id)
        paginator = Paginator(sexual, 10)
        sexual_page = paginator.page(page_num)

        return render(request, 'complete.html', {'sexual': sexual_page, 'sexual_id': sexual_id})


class Resgain(APIView):

    def get(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'msg': 'xxx',
        }

        sexual = models.Sexual.objects.all()
        sexual_dict = [i.__dict__ for i in sexual]
        for sexual in sexual_dict:
            sexual.pop('_state')
        ret['msg'] = sexual_dict
        return HttpResponse(json.dumps(ret, ensure_ascii=False))


class Complete(APIView):

    def get(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'msg': 'xxx',
        }

        sexual_id = int(request._request.GET.get('sexual_id', 1))
        sexual = models.CompleteInformation.objects.filter(sexual_id=sexual_id)
        sexual_dict = [i.__dict__ for i in sexual]
        for sexual in sexual_dict:
            sexual.pop('_state')
        ret['msg'] = sexual_dict
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
