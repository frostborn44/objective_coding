from django.shortcuts import render

# Create your views here.
def displayTableView(request) : # Function to return the web page for the table view
	return render(request, "tableView.html")