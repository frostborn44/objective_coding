import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

# Create your views here.

# Turn the jason file into a json data object to use with modifications
with open('data.json') as d:
	data = json.load(d)
	appCount = 0
	skillList = []
	# some heavy lifting calculations of data
	for applicant in data["applicants"]:
		skillCount = 0
		appCount=appCount+1 # calculate how many applicants there is
		for skill in data["skills"]:
			if skill["applicant_id"] == applicant["id"]:
				skillCount=skillCount+1 # calculate the number of skills for each applicant, used for rowspan later
				if skill['name'] not in skillList: # adding up the total unique skills
					skillList.append(skill['name'])
				if skillCount==1:
					applicant['firstSkill'] = skill["name"] # adding 1 skill for each applicant to later use on row
					skill["applicant_id"] = 0 # remove the link since ive already got the list above
		if skillCount==0: # taking care of the off chance someone has no skills, input 3 dashes
			applicant['firstSkill'] = '---'
		applicant['skillCount'] = skillCount # adding skill count to the json data
	skillCountUnique = len(skillList)
	# calculate the total number of skills applying for each job, for rowspan later
	for job in data["jobs"]:
		rowCount = 0
		for applicant in data["applicants"]:
			if applicant["job_id"]==job["id"]:
				rowCount=rowCount+applicant["skillCount"]
		job['rows'] = rowCount




# Return the webpage tableView.html, along with the json data added ti the page
def loadJsonTableFormat(request):
	return render(request, 'tableView.html', {'d': data, 'ac':appCount, 'sc':skillCountUnique}, content_type="text/html")