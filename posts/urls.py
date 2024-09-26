from django.urls import path
from .views import PostListView, PostDetailView , CommentListView , CommentDetailView

urlpatterns = [
    path('',PostListView.as_view()),
    path('<int:pk>/',PostDetailView.as_view()),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]