from recipes.views import home, contato, sobre
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]