import json

from django.http import JsonResponse
from django.shortcuts import render
from .BaseCtl import BaseCtl


class ErrorCtl(BaseCtl):

    def display(self, request, params={}):
        res = {"result": {}, "success": True}
        res["success"] = False
        res["result"]["message"] = "DB Down"
        print(">>>>>>>>>>>>> DB is not available")
        return JsonResponse(res)

    def get_service(self):
        pass
