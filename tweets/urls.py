from django.urls import path
from . import views

urlpatterns = [
    path("", views.TweetListView.as_view()),
    path("<int:pk>/", views.TweetDetailView.as_view()),
]
