from . import views
from django.urls import path

app_name = 'StoreApp'

urlpatterns = [
    path("store/", views.Store, name="index"),
    path("categories/<str:category>/<slug:slug>/", views.detail_stores, name='store_detail'),
    path("categories/<str:category>/<slug:slug>/share/", views.share_post, name='store_share_post'),
    path("categories/<str:category>/<slug:slug>/share/send/", views.send_post, name='store_send_post'),
    # path("store categories/", views.categories_toys, name='categories'),
    path("new_post/", views.create_new_post, name='new_post'),
]
