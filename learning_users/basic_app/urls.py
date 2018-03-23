from django.conf.urls import url
from basic_app import views as ba_views

# TEMPLATES URLs
app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', ba_views.register, name='register_view'),
    url(r'^user_login/$', ba_views.user_login, name='user_login_view'),
]
