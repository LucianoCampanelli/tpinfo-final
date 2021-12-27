from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListarPosts.as_view(), name='lista'),
    path('<slug:pk>', views.DetallePost.as_view(), name='detalle'),
    path('<slug:pk>/update', views.UpdatePost.as_view(), name='update'),
	path('<slug:pk>/crear', views.CrearPost.as_view(), name='crear'),
    path('^$', views.index, name='index'),
]