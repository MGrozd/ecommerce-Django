
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^proizvodi/edit/(?P<ID>\d+)$',views.proizvodi_edit,name='pr_edit'),
	url(r'^proizvodi/delete/(?P<ID>\d+)$',views.proizvodi_delete,name='pr_delete'),
	url(r'^proizvodi/add',views.proizvodi_add,name='pr_add'),
	url(r'^proizvodi/',views.proizvodi_index,name='proizvodi_index'),
	url(r'^$',views.index,name='index'),
]
