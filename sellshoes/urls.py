from django.contrib import admin
from django.urls import path, include
from shoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shoes', views.shoes),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destory),
    path('check_out/<int:id>', views.check_out),
    path('mpesa/<int:id>', views.mpesa),
    path('display', views.diplay),
    path('checkout/<int:id>', views.checkout),
    path('checkoutpay/<int:id>', views.checkoutpay),

    path('', views.show)
]
