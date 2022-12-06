from django.shortcuts import render
from datetime import datetime

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

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        # context["news_title"] = "Громкий новостной заголовок"
        # context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context['datetime'] = datetime.now()
        context['news'] = [
            {'news_title': f'Громкий новостной заголовок номер {i}',
             'news_preview': 'Предварительное описание, которое заинтересует каждого'}
            for i in range(1, 6)]
        context['page_range'] = range(1, 5)
        return context

class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        # context["news_object"] = get_object_or_404(News, pk=pk)
        context["news_object"] = {'title': 'Красноречивый заголовок карточки', 'body':'Увлекательное содержание'}
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context