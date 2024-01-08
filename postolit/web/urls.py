from django.contrib import admin
from django.urls import path
from .views import index, reg, index_2, login_view, logout_view, clickhouse_test

urlpatterns = [
   path('web/<int:id>', index_2), # http://127.0.0.1:8000/web/12, где 12 - ID
   path('web', index, name="web"),
   path('reg', reg, name="reg"),
   path('login', login_view, name="login"),
   path('logout', logout_view, name="logout"),
   path('click', clickhouse_test, name="click")
]