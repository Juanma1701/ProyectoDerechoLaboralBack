from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'register', views.register)

urlpatterns = [
    path('',include(router.urls)),
    path('registrar_usuario/', views.RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('login_usuario/', views.LoginUsuario.as_view(), name='login_usuario'),
    path('deleteUser/<int:id>',views.DeleteUser.as_view(),name="deleteUser")
    
]