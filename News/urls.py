from django.urls import path
from .views import *


urlpatterns = [
    path("", PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', NwCreate.as_view(), name='nw_create'),
    path('articles/create/', ArCreate.as_view(), name='ar_create'),
    path('news/<int:pk>/edit/', NwUpdate.as_view(), name='nw_edit'),
    path('articles/<int:pk>/edit/', ArUpdate.as_view(), name='ar_edit'),
    path('news/<int:pk>/delete/', NwDelete.as_view(), name='nw_delete'),
    path('articles/<int:pk>/delete/', ArDelete.as_view(), name='ar_delete'),
]