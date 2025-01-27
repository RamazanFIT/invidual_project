from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("blog.urls", "blog"), namespace="blog")),
    path("users/", include(("users.urls", "users"), namespace="users")),
    path("accounts/", include("django.contrib.auth.urls")),  # For login/logout
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
