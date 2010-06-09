import functools

from django import http

def ajax_required(view):
    def decorator(request, *args, **kwargs):
        if not request.is_ajax():
            return http.HttpResponseBadRequest()
        return view(request, *args, **kwargs)
    return decorator
