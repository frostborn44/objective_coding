from django.urls import path
from .views import displayTableView

urlpatterns = [
	path("", displayTableView, name="tableView") # When nothing in url, route to the table view
]