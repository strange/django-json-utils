import datetime

from json_utils.http import JSONResponse
from json_utils import decorators

from example.stuff.models import Thing

@decorators.ajax_required
def view1(request):
    response_dict = {
        'id': 1,
        'date': datetime.datetime.now(),
    }
    return JSONResponse(response_dict)

@decorators.ajax_required
def view2(request):
    return JSONResponse(Thing.objects.create())
