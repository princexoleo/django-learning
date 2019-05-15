from django.urls import path,include
from . import views

app_name='snippets'
urlpatterns = [
    path('',views.snippets_list, name='list'),
    path('<int:id>/', views.snippets_details, name='details'),
]
