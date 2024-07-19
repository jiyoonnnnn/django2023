from django.urls import path

from .views import base_views, comwrite_views, comcomment_views, sale_views, find_views

app_name = 'pybo'

urlpatterns = [
# base_views.py
    path('',
         base_views.index, name='index'),
    path('guicom/',
         base_views.guicom, name='guicom'),
    path('salep/',
         base_views.salep, name='salep'),
    path('findp/',
         base_views.findp, name='findp'),
    path('<int:comwrite_id>/',
         base_views.detail, name='detail'),
    path('salep/<int:sale_id>/',
         base_views.saledetail, name='saledetail'),
    path('findp/<int:find_id>/',
         base_views.finddetail, name='finddetail'),


    # question_views.py
    path('comwrite/create/',
         comwrite_views.comwrite_create, name='comwrite_create'),
    path('sale/create/',
         sale_views.sale_create, name='sale_create'),
    path('sale/delete/<int:sale_id>/',
         sale_views.sale_delete, name='sale_delete'),
    path('find/create/',
         find_views.find_create, name='find_create'),
    path('find/delete/<int:find_id>/',
         find_views.find_delete, name='find_delete'),
    path('comwrite/modify/<int:comwrite_id>/',
         comwrite_views.comwrite_modify, name='comwrite_modify'),
    path('comwrite/delete/<int:comwrite_id>/',
         comwrite_views.comwrite_delete, name='comwrite_delete'),

    # answer_views.py
    path('comcomment/create/<int:comwrite_id>/',
         comcomment_views.comcomment_create, name='comcomment_create'),
    path('comcomment/delete/<int:comcomment_id>/',
         comcomment_views.comcomment_delete, name='comcomment_delete'),

]