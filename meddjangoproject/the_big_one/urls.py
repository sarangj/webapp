from django.conf.urls import url

from . import views

# The intention here is that they go to .../doctors to search for doctors, see a
# list of doctors etc. They then go to .../doctors/2 to see the details of an
# individual doctor

urlpatterns = [
    # Now .../doctors and .../doctors/ dispatch to the correct index page
    url(r'^doctors/*$', views.doc_index, name='index'),
    url(r'^doctors/(?P<doctor_id>[0-9]+)/$', views.doctor, name='doctor'),
    ]
