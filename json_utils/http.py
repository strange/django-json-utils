from django import http

from json_utils import utils

class JSONResponse(http.HttpResponse):
    def __init__(self, content):
        # Considered adding some CSRF protection. Decided against it in favour
        # of the Django middleware and other more generic solutions.
        content = utils.to_json(content)
        super(JSONResponse, self).__init__(content,
                                           mimetype='application/json')
