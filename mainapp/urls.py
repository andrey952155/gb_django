from django.urls import path
from mainapp.apps import MainappConfig

from mainapp import views

name = MainappConfig.name

urlpatterns = [
    path('fpage', views.fpage, name='mainapp'),
    # path('<str:word>', views.durl),
    path('ind', views.IndexPage.as_view()),
    path('', views.MainPageView.as_view()),
    path('contacts.html', views.ContactsPageView.as_view()),
    path('courses_list.html', views.CourseslistPageView.as_view()),
    path('doc_site.html', views.DocSitePageView.as_view()),
    path('login.html', views.LoginPageView.as_view()),
    path('news.html', views.NewsPageView.as_view()),
]
