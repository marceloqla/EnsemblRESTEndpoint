"""gene_suggest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from restservice import views

urlpatterns = [
	#Since this is a simple exercise, only one path is allowed, the geneautocomplete path for testing
	#In a real production more paths would be added as needed.
	#For example user login or other queries
    re_path(r'^geneautocomplete/$', views.SuggestionList.as_view()),
]
