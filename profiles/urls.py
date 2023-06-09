from django.urls import path
from .views import (
    my_profile_view, 
    invites_received_view, 
    profiles_list_view, 
    invite_profiles_list_view,
    ProfileListView,
    ProfileDetailView,
    send_invatation,
    remove_from_friends,
    accept_invatation,
    reject_invatation,
  )

app_name = 'profiles'

urlpatterns = [
  
  path('', ProfileListView.as_view(), name='all-profiles-view'),
  path('myprofile/', my_profile_view, name='my-profile-view'),
  path('my-invites/', invites_received_view, name='my-invites-view'),
  # path('all-profiles/', profiles_list_view, name='all-profile-view'),
  
  
  path('send-invite/', send_invatation, name='send-invite'),
  path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
  path('remove-friend/', remove_from_friends, name='remove-friend'),
  # path('<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),
  path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
  
  path('my-invites/accept/', accept_invatation, name='accept-invite'),
  path('my-invites/reject/', reject_invatation, name='reject-invite'),
  
]
