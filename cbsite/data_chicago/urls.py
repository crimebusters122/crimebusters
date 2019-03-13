from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_loc_type, name='location type'),
    path('ajax/load-locs-1/', views.load_locs_1, name='ajax_load_locs_1'),
    path('ajax/load-locs-2/', views.load_locs_2, name='ajax_load_locs_2'),
    path('ajax/load-var-types-1/', views.load_var_types_1, \
        name='ajax_load_var_types_1'),
    path('ajax/load-vars-1/', views.load_vars_1, name='ajax_load_vars_1'),
    path('ajax/load-var-types-2/', views.load_var_types_2, \
        name='ajax_load_var_types_2'),
    path('ajax/load-vars-2/', views.load_vars_2, name='ajax_load_vars_2'),
]