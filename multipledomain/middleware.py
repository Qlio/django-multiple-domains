from django.conf import settings


class MultipleDomainMiddleware(object):
    def process_request(self, request):
        url_config = getattr(settings, 'MULTIURL_CONFIG', None)
        if not url_config:
            return

        host = request.get_host()
        if host in url_config:
            request.urlconf = url_config[host]
