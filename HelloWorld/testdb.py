# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    # test1 = Test(name='w3cschool.cn')
    # test1.save()
    # return HttpResponse("<p>添加数据成功</p>")

    response = ""
    response1 = ""

    list = Test.objects.all()

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    response4 = Test.objects.order_by('name')[0:2]

    response5 = Test.objects.order_by('id')

    response6 = Test.objects.filter(name="w3cschool.cn").order_by('id')

    for var in list:
        response1 += var.name + " "

    response = response1

    return HttpResponse("<p>" + response + "</p>")
