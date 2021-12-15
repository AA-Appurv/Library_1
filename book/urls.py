from django.urls import path
from book import views
from library.settings import DEBUG, STATIC_URL,STATIC_ROOT, MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/',views.upload, name='upload-book'),
    path('upload/<int:book_id>',views.upload_book),
    path('upload/<int:book_id>', views.delete_book)
    
    
]
# DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT )
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
    
    