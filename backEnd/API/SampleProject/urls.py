
from django.conf.urls import url
from django.contrib import admin
from MyApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gamepredictions', views.gamePredictions)
]