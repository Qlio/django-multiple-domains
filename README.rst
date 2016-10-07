Django Multiple Domain
**********************

Django middleware for serving single Django instance in multiple domains with different urls.


Installation
============

ost recent **Django Multiple Domain** version using pip: ::

    pip install django-multiple-domains

Setup
=====

**NOTE**: The following settings should be added to the project file 'settings.py'.

1. Add 'multipledomain' to ''INSTALLED_APPS'': ::

    INSTALLED_APPS += ( 'multidomain', )

2. Add 'multipledomain.middleware.MultipleDomainMiddleware' to ''MIDDLEWARE_CLASSES'': ::

    MIDDLEWARE_CLASSES += ( 'multipledomain.middleware.MultipleDomainMiddleware', )

3. Create different urls config file for each domain (Ex: 'site.com' and 'blog.com'): ::

    * urls_site.py   (by default)
        url(r'^$', TemplateView.as_view(template_name='site.html'), name='site'),

    * urls_blog.py
        url(r'^$', TemplateView.as_view(template_name='blog.html'), name='blog'),

4. Declare host/domain urlconfig tuple ''MULTIURL_CONFIG'': ::

    MULTIURL_CONFIG = {
        'site.com': 'urls_site',
        'blog.com': 'urls_blog',
    }

    ROOT_URLCONF = 'urls_site'


Related urls: `https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.get_host`
