from django.urls import path
from . import views

urlpatterns = [
    path("", views.TinyUserInfoViews.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("<int:pk>/", views.UserDetailViews.as_view()),
    path("profile/", views.MyUserProfileViews.as_view()),
    path("@<str:username>/", views.UserDetailByUsernameViews.as_view()),
    path("password/", views.ChangePassword.as_view()),
    path("<int:pk>/tweets/", views.UserTweetsView.as_view()),
]
