from django.urls import path
from.import views
from .views import like_post, posts_view

app_name = 'posts'

urlpatterns=[
    path('book/',views.ListBookView.as_view(),name='list-book'),
    path('book/<int:pk>/detail/',views.DetailBookView.as_view()),
    path('book/toukou/',views.Toukou.as_view(), name='create'),
    path('book/<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    path('book/<int:pk>/update/', views.Update.as_view(), name='update'),
    path('like/', like_post, name='like-post'),
    path('', posts_view, name='post-list'),
]
