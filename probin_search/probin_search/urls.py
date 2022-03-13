
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "মিত্র ফাউন্ডেশন । প্রবীণ"
admin.site.site_title = "মিত্র ফাউন্ডেশন । প্রবীণ"
admin.site.index_title = "মিত্র ফাউন্ডেশন । একটি স্বেচ্ছাসেবী সমাজকল্যাণ মূলক প্রতিষ্ঠান "


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
