from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^view1$', 'example.stuff.views.view1', {}, 'view1'),
    (r'^view2$', 'example.stuff.views.view2', {}, 'view2'),
)
