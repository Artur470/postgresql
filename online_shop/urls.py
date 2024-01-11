from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('shop.urls')),
    path('orders/', include('orders.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)