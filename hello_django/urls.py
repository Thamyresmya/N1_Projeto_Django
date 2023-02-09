from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>/', views.hello),
    path('soma/<int:a>/<int:b>/', views.soma),
    path('subtracao/<int:a>/<int:b>/', views.subtracao),
    path('divisao/<int:a>/<int:b>/', views.divisao),
    path('multiplicacao/<int:a>/<int:b>/', views.multiplicacao),

]
