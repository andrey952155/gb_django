from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View, TemplateView


def fpage(request):
    return HttpResponse("Эта страница сформирована в функции")


# def durl(request, **kwargs):
#     return HttpResponse(f'Kwargs - {kwargs}<br>, request - {request}')


class IndexPage(View):
    @staticmethod
    def get(*args):
        return HttpResponse('Index page')


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CourseslistPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'
