from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserList.as_view()),
]
