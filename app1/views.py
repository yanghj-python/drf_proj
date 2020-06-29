from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import settings
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from app1.models import User
@csrf_exempt
def user(request):
    if request.method == "GET":
        print("GET SUCCESS  查询")
        return HttpResponse("GET SUCCESS")

    elif request.method == "POST":
        print("POST SUCCESS  添加")
        return HttpResponse("POST SUCCESS")

    elif request.method == "PUT":
        print("PUT SUCCESS  修改")
        return HttpResponse("PUT SUCCESS")

    elif request.method == "DELETE":
        print("DELETE SUCCESS  删除")
        return HttpResponse("DELETE SUCCESS")


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        if user_id:
            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user_val:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user_val
                })
        else:
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })

        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })

    def put(self, request, *args, **kwargs):
        print("PUT SUCCESS  修改")
        return HttpResponse("PUT SUCCESS")

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        try:
            User.objects.get(pk=user_id).delete()
            user_list = User.objects.all().values("username", "password", "gender")
            return JsonResponse({
                "status": 201,
                "message": "删除用户成功",
                "results": list(user_list)
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "删除用户失败",
            })


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print(request._request.GET)
        print(request.GET)
        print(request.query_params)
        user_id = kwargs.get("id")
        if user_id:
            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user_val:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user_val
                })
        else:
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })

        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })

    def post(self, request, *args, **kwargs):
        print(request._request.POST)
        print(request.POST)
        print(request.data)
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })
class StudentAPIView(APIView):

    def post(self, request, *args, **kwargs):
        print("POST方法")
        print(request.data)
        return Response("POST方法访问成功")
