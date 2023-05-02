"""WasteNot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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


from django.conf import settings
from  MainApp import views
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LandingPage,name='landing'),
    
    path('signup/',views.SignupPage,name='signup'),
    path('sellerhome/',views.SellerHomePage,name='sellerhome'),
    path('vendorhome/',views.VendorHomePage,name='vednorhome'),
    path('orghome/',views.OrgHomePage,name='orghome'),
    path('sellerorder/',views.SellerOrderPage,name='sellerorder'),
    path('sellheadphone/',views.SellHeadphonePage,name='sellheadphone'),
    path('sellphone/',views.SellPhonePage,name='sellphone'),
    path('selltv/',views.SellTvPage,name='selltv'),
    path('sellwatch/',views.SellWatchPage,name='sellwatch'),
    path('sellspeaker/',views.SellSpeakerPage,name='sellspekaer'),
    path('sellmouse/',views.SellMousePage,name='sellmouse'),
    path('sellkeyboard/',views.SellKeyboardPage,name='sellkeyboard'),
    path('selllaptop/',views.SellLaptopPage,name='selllaptop'),
    path('vendororder/',views.VendorOrderPage,name='vendororder'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
