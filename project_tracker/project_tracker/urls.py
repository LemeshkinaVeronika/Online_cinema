from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
 
 


urlpatterns = [
    path("admin/", admin.site.urls),
    path('movieblog/', include('movieblog.urls', namespace='movieblog')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('user/', include('user_app.urls', namespace='user_app')),
     
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "utils_app.exception_handlers.bad_request_handler"  
handler403 = "utils_app.exception_handlers.permission_denied_handler"  
handler404 = "utils_app.exception_handlers.page_not_found_handler"  
handler500 = "utils_app.exception_handlers.server_error_handler"