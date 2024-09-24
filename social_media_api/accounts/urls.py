from django.urls import path
from .views import UserRegisterView, UserLoginView, FollowViewSet, FollowUserView, UnfollowUserView, ListUsersView

# Define the viewsets first
follow_viewset = FollowViewSet.as_view({
    'post': 'follow'
})

unfollow_viewset = FollowViewSet.as_view({
    'post': 'unfollow'
})

# Then use them in urlpatterns
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('users/', ListUsersView.as_view(), name='list_users'),
]
