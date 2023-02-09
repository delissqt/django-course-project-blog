
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


---

# Deployment Considerations



```
|-----------------------|                               |--------------------------------------------|
|  Choose Database      |                               | SQLite might work but might be too slow or |
|  (reconsider SQLite)  |-----------------------------> | be erased (depending on hosting provider)  |
|-----------------------|                               |--------------------------------------------|


|-----------------------|                               |---------------------------------------------|
|  Adjust Settings      |-----------------------------> | Adjust config for choosen hosting provider, | 
|-----------------------|                               | disable development-only settings           |
                                                        |---------------------------------------------|


|-----------------------|                               |--------------------------------------------|
|  Collect Static Files |-----------------------------> | Static files are NOT served automatically  |
|-----------------------|                               | ( just like user uploads )                 |
                                                        |--------------------------------------------|


|----------------------------------|                    |--------------------------------------------|
|  Handle Static & Uploaded Files  |                    | Static files are NOT served automatically  | 
|             Serving              |------------------> | ( just like user uploads )                 |
|----------------------------------|                    |--------------------------------------------|


|---------------------------|                           |----------------------------------------------|
|  Choose a Host + Deploy!  |-------------------------> | Also dive into host-specific docs + examples |
|---------------------------|                           |----------------------------------------------|

```

* Using SQLite might work. But it might also not be the best choice. We'll have to consider moving to a different database.
  
* Revisit and adjust the settings of your Django application `settings.py` file project.
  There are some some settings which we now need to adjust depending on our chosen hosting provider, depending on the database we're using and also a couple of other aspects you should be aware of.
  
* Static files considerations: We need to collect them or we need to let Django collect them
  for us. And that might be unexpected. In general, static files, so our CSS files, JavaScript files we might have, images we might have, are not served automatically just like user uploads. For example in `urls.py` file project we configured le next line in order to get images uploads by the user
  ```
    ...

    urlpatterns = [
        ...
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

*  In general, have a look at how we can handle static and uploaded files, not just
   regarding where we store it but also how we serve them and how we can serve then in differents ways because they are not served automatically.(That's related to the previous point) 

* We will also need to choose a host and then deploy our application because it turns out
  that there will not just be one option for deploying a Django application.
  ultimately there will be multiple options. When you decide to use a certain host or a certain hosting provider, then you will always also need to dive into DIR docs



  ---

# Static Files & User Uploads

```
|-------------------------------------------------------------------------------------------------|
| Django does NOT serve static or uploaded files automatically                                    |
|-------------------------------------------------------------------------------------------------|
|`python manage.py runserver` is a development - only server which handles static files serving   |
|-------------------------------------------------------------------------------------------------|
             ||                                   ||                                  ||
            _||_                                 _||_                                _||_
            \  /                                 \  /                                \  /
             \/                                   \/                                  \/
|---------------------------|         |-------------------------|        |------------------------|
| Configure Django to serve |         | Configure web server to |        | Use dedicated service/ |
| such files (via urls.py   |         | serve static files AND  |        |  server for static and |
|---------------------------|         |    Django app           |        |     uploaded files     |
                                      |-------------------------|        |------------------------|

|-----------------------------|       |-------------------------|        |-------------------------|
| Okey for smaller sites, not |       | Same server and device  |        | Initial setup is more   |
|   performance-optimized     |       | but separate processes, |        | complex but offers best |
|        though               |       | better for performance  |        |      performance        |
|-----------------------------|       |-------------------------|        |-------------------------|

```