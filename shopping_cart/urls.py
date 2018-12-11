from django.urls import path
from shopping_cart import views

app_name = 'shopping_cart'

urlpatterns = [
	path('add-to-cart/<item_id>/',views.add_to_cart,name='add_to_cart'),
	path('order-summary/',views.order_summary,name='order_summary'),
	path('enter-address/',views.enter_address,name='enter_address'),
	path('delete/<item_id>/',views.delete_from_cart,name='delete_from_cart'),
	path('delete2/<item_id>/',views.delete_from_cart2,name='delete_from_cart2'),
	path('purchase-success/',views.purchase_success,name='purchase_success'),
	path('purchase-success-cod/',views.purchase_success_cod,name='purchase_success_cod'),
	path('order-history/',views.show_order_history,name='order'),
	path('order-summary-ajax/',views.order_summary_ajax,name='order_summary_ajax'),

]