from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/', views.profile, name='profile'),                 # 변화 가능한 스트링이 url 처음에 온다면 path가 작성 된 위치는 맨 뒤로 가야 된다. urls 실행 시 위에서 부터 검색하는데 login 등 다른 url 주소가 먼저 걸리기 때문이다. 
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
