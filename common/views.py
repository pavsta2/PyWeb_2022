from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class HelloWorldView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        hw = """<h1>Hello, World</h1>"""
        return HttpResponse(hw)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'common/index.html')
