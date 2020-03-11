from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', views.logout_view, name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('', views.post, name='posts'),
    path('post_create/', views.post_create, name="createpost"),
    path('commenting/<post_id>', views.commenting, name="commenting"),
    path('comment/<post_id>/', views.comment, name="comment"),
    path('search/', views.search_user, name="search"),
    path('likes/<post_id>', views.likes, name="likes"),
    re_path(r'^follow/(?P<operation>.+)/(?P<pk>\d+)/$', views.follow, name="follow" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
