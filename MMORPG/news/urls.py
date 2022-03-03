from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate, CommentCreate, PostEdit

urlpatterns = [path('', PostList.as_view(), name='post_list'),
               path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
               path('create/', PostCreate.as_view(), name='post_create'),
               path('delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
               path('update/<int:pk>', PostUpdate.as_view(), name='post_update'),
               path('post_edit/', PostEdit.as_view(), name='post_edit'),

               path('<int:pk>/create_comment', CommentCreate.as_view(), name='comment_create')
               ]