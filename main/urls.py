from django.urls import path


from .views import index
from .views import SHLoginView
from .views import profile
from .views import SHLogoutView
from .views import RegisterDoneView, RegisterUserView

app_name = 'main'
urlpatterns = [
    path('accounts/login/', SHLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', SHLogoutView.as_view(), name='logout'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
]
