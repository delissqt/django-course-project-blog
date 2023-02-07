
# NOTES

Files are stored 

```
# urls.py file project

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("blog/", include("blog.urls"))
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```
static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

`settings.MEDIA_ROOT`  --->  **THIS DEFINES THE FOLDER WHERE THE SERVABLE FILES LIVE**

`settings.MEDIA_URL`  --->  **THIS DEFINES THE URL, UNDER WHICH THESE FILES SHOULD BE REACHABLE**