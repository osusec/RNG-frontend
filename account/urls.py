#
# Account urls.py
#

from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

'''django.contrib.auth.urls
login/ [name='login']
logout/ [name='logout']
password_change/ [name='password_change']
password_change/done/ [name='password_change_done']
password_reset/ [name='password_reset']
password_reset/done/ [name='password_reset_done']
reset/<uidb64>/<token>/ [name='password_reset_confirm']
reset/done/ [name='password_reset_complete']
'''

urlpatterns = [
    path ('', login_required(ProfilePage), name='profile-home'),
    path ('register/', SignUpView.as_view(), name='profile-signup')
]
