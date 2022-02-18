from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate

urlpatterns = [path('', PostList.as_view()),
               path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
               path('create/', PostCreate.as_view(), name='post_create'),
               path('delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
               path('update/<int:pk>', PostUpdate.as_view(), name='post_update')
               ]