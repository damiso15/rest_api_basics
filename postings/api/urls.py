"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import BlogPostRudView, BlogPostAPIView

app_name = 'postings.api'

urlpatterns = [
    # path('', BlogPostListView.as_view(), name='post-list'),
    path('', BlogPostAPIView.as_view(), name='post-listcreate'),
    path('<int:pk>/', BlogPostRudView.as_view(), name='post-rud'),
]

# (?P<pk>\d+)$
# It is a regular expression, which is matched against the actual URL
# Here r'' specifies that the string is a raw string. '^' signifies the start, and $ marks the end.
# Now 'pk' (when inside <>) stands for a primary key. A primary key can be anything eg. it can be a string, number etc.
# A primary key is used to differentiate different columns of a table.
# Here it is written
# <pk>\d+
# \d matches [0-9] and other digit characters.
# '+' signifies that there must be at least 1 or more digits in the number
# So,
# .../posts/1 is valid
# .../posts/1234 is valid
# .../posts/ is not valid since there must be at least 1 digit in the number
# Now this number is sent as an argument to BlogListView and you run you desired operations with this primary key
