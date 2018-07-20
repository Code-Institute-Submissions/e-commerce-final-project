"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views
# from checkout import views
from home.views import get_index
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url, include
from django.views.static import serve
from accounts import urls as accounts_urls
from products import urls as products_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from reviews import urls as reviews_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name='home'),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
     path('reviews/', include(reviews_urls)),
    path('cart/', include(cart_urls)),
    # path('buy_now/', views.buy_now, name='buy_now'),
    path('search/', views.search, name='search'),
    path('checkout/', include(checkout_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),

]