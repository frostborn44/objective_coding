# objective_coding
The purpose of this project is to demonstrate the knowledge and skill to be able to create django project for the purpose of demonstration.

Tech used: 
Python 3.13 version
Django 5.2 version
coded in Microsoft Visual Studio
Git (uploaded to Git)

To run the program: 
From the command line, navigate to the objective_coding file. 
Then start the server with "python manage.py runserver" (control + C will stop the server)
It is not set up for any specific server, so the default should run on url http://127.0.0.1:8000/
Once you have the server running, and go to the webpage URL, it should automatically return back the only page set up.

Included:
There is a mandatory hard-coded 6-header fields, "job" "applicant name" "email address" "website" "skills" and "cover letter paragraph"

Requirements:
To run this properly, you will need to use a JSON file. 
That JSON file must be named "data.json" and be included in the directory. You can replace the current one there if you want to run another file.
You must keep the data formatting with the json file. A library of "applicants" "jobs" and "skills".
The applicants need to contain a "id" "name" "email" "website" "cover_letter" and "job_id".
The jobs needs to contain "id" and "name"
The skills needs to contain "name" and "applicant_id". It can contain an "id"

Functionality/scalability:
This program can run with any number of jobs, any number of applicants, and any number of skills, and will dynamically match the table to fit.
There is a statistic added to the footer that includes the total number of applicants, as well as the total number of unique skills from the json file.
There can be unlimited number of skills for each applicant, but they can only have 1 job.
Having more would require a seperate entry for the applicant and would then be some sort of clone or ID fraud at that point.

Addtional Info:
#### Job

* Columns:
  * id: integer
  * name: string (e.g. Web Developer)

#### Applicant

* Columns:
  * id: integer
  * name: string
  * email: string
  * website: string
  * cover_letter: text
  * job_id: integer
* Relationships:
  * has one job
  * has many skills

#### Skill

* Columns:
  * id: integer
  * name: string
  * applicant_id: integer