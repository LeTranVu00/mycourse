from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('search/', views.search_courses, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('checkout-direct/<int:course_id>/', views.checkout_direct, name='checkout_direct'),
    path('generate-qr/<int:course_id>/', views.generate_qr_code, name='generate_qr'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('my-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('forum/', views.forum_list, name='forum_list'),
    path('forum/create/', views.forum_create, name='forum_create'),
    path('forum/<int:post_id>/', views.forum_detail, name='forum_detail'),
    path('forum/<int:post_id>/edit/', views.forum_edit, name='forum_edit'),
    path('forum/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path('forum/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('remove-from-cart/<int:course_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('course/<int:course_id>/learning-path/', views.learning_path, name='learning_path'),
    path('toggle-task/<int:task_id>/', views.toggle_task_completion, name='toggle_task_completion'),
]