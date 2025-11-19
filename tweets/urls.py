from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path("", views.TweetListView),
    path("<int:pk>/", views.TweetDetailView.as_view()),
]
