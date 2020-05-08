from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wishes/', views.wishes_index, name='wishes_index'),
    path('wishes/<int:wish_id>/', views.wishes_detail, name='wishes_detail'),
    path('wishes/create/', views.WishCreate.as_view(), name='wishes_create'),
    path('wishes/<int:pk>/update/', views.WishUpdate.as_view(), name='wishes_update'),
    path('wishes/<int:pk>/delete/', views.WishDelete.as_view(), name='wishes_delete'),
]

