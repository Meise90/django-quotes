from django.urls import path

from quotesapp import views

app_name = 'quotesapp'

urlpatterns = [
    # C
    path('create/', views.quote_create_view, name='quote-create-view'),

    # R
    path('', views.quote_list_view, name='quote-list-view'),
    path('<int:quote_id>/', views.quote_detail_view, name='quote-detail-view'),

    # U
    path('<int:quote_id>/update/', views.quote_update_view, name='quote-update-view'),

    # D
    path('<int:quote_id>/delete/', views.quote_delete_view, name='quote-delete-view'),

]