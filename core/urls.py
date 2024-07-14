
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index , name="index"),
    path('delete-recipe/<id>/', delete_recipe , name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe , name="update_recipe"),
    
    
    path('about/', about, name='about'),
    path('login/', login_page , name="login"),
    path('logout/', logout_page , name="logout"),
    
    path('students/', get_students , name="get_students"),
    
    
    
    path('register/', register_page , name="register"),
    
    
    path('contact/', contact , name="contact"),
    path('recipes/', recipes , name="recipes"),
    path('admin/', admin.site.urls),
]
    
    
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()    
    
    
    
    
    
    
   


