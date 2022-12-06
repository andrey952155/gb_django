from django.urls import path
from mainapp.apps import MainappConfig

from mainapp import views

app_name = MainappConfig.name

urlpatterns = [
    # path('fpage', views.fpage, name='mainapp'),
    # path('<str:word>', views.durl),
    # path('ind', views.IndexPage.as_view()),
    path('', views.MainPageView.as_view(), name='main_page'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts'),
    path('courses_list/', views.CourseslistPageView.as_view(), name='courses'),
    path('doc_site/', views.DocSitePageView.as_view(), name='doc_site'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('news/', views.NewsPageView.as_view(), name='news'),
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
]
