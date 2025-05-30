from django.urls import path
from .views import loadJsonTableFormat

urlpatterns = [
	path("", loadJsonTableFormat, name="tableView") # When nothing in url, route to the table view
]