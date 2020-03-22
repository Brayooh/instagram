from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/',include("django.contrib.auth.urls")),
    path('register/', views.registration, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.post, name='posts'),
    path('post_create/', views.post_create, name="createpost"),
    path('commenting/<post_id>', views.commenting, name="commenting"),
    path('comment/<post_id>/', views.comment, name="comment"),
    path('search/', views.search_user, name="search"),
    path('likes/<post_id>', views.likes, name="likes"),
    # re_path(r'^follow/(?P<operation>.+)/(?P<pk>\d+)/$', views.follow, name="follow" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
