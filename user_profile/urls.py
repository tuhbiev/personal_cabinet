from django.urls import path
from .views import ProfileView, user_list, UserEditView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', user_list, name='user-list'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
]
