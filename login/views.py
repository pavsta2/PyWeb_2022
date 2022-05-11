from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse


class LoginVeiw(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'login/index.html')

    def post(self, request):
        return JsonResponse(request.post, json_dumps_params={'indent': 4})
