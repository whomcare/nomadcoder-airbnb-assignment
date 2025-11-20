from django.urls import path
from . import views

urlpatterns = [
    path("", views.TinyUserInfoViews.as_view()),
    path("<int:pk>/", views.UserDetailViews.as_view()),
    path("<int:pk>/tweets/", views.UserTweetsView.as_view()),
]
