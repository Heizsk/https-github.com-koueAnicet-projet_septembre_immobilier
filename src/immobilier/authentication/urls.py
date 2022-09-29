from django.contrib.auth import views as auth_views
from django.urls import path
from authentication import views


urlpatterns = [
    
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    #path('submit-property/', views.submit_property, name='submit-property'),
    path('submit-property/', views.SubmitProperty.as_view(), name='submit-property'),
    path('user-properties/', views.UserProperty.as_view(), name='user-properties'),
    path('properties/', views.AllPropertiesView.as_view(), name='properties'),
    path('user-logout/', views.logout_user_auth, name='user-logout'),
    path('user-profiles/', views.user_profiles, name='user-profiles'),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name="authentication/pages/password-reset.html"), 
        name='reset-password'),
    path('reset-password-send/', auth_views.PasswordResetDoneView.as_view(
        template_name="authentication/pages/password-reset-sent.html"), 
        name='password-reset-done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="authentication/pages/change-password.html"), 
        name='password-reset-confirm'
        ),
    path('reset-password-complet/', auth_views.PasswordResetCompleteView.as_view(
        template_name="authentication/pages/password-reset-done.html"), 
        name='password-reset-complete'),
    
]
