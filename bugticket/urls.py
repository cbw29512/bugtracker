from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('ticket_detail/<int:id>', views.ticket_details, name='ticket_detail'),
    path('create_ticket/<int:user_id>', views.create_ticket, name='create_ticket'),
    path('inprogressticket/edit/<int:ticket_id>', views.inprogress_ticket, name='inprogress_ticket'),
    path('complete/edit/<int:ticket_id>', views.complete_ticket, name='complete_ticket'),
    path('invalidticket/edit/<int:ticket_id>', views.invalid_ticket, name='invalid_ticket'),
    path('edit_ticket/edit/<int:ticket_id>', views.edit_ticket, name='edit_ticket'),
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),
]
