from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('<str:cat>/',views.by_category,name='by_category'),
    path('search/category/',views.by_search,name='by_search'),
    path('<str:bycat>/<str:catty>/<int:id>/',views.post,name='posts')
]