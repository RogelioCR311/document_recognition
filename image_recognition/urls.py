from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('upload_docs/', views.upload_documents, name='upload_docs'),
    path('upload_id/', views.upload_id, name='upload_id'),
    path('upload_curp/', views.upload_curp, name='upload_curp'),
    path('upload_rfc/', views.upload_rfc, name='upload_rfc'),
    path('upload_acta/', views.upload_acta, name='upload_acta'),
    path('upload_seguro/', views.upload_seguro, name='upload_seguro'),
]