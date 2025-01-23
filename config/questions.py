'''
Author:     Vikas Malik
LinkedIn:   https://www.linkedin.com/in/vikas-malik-3a854310/

Copyright (C) 2024 Vikas Malik

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "20"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = ""                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/vikas-malik-3a854310/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for current employer"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 1000000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 85000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "USD"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "20+ year multi faceted manager in variety of Data engineering and Data Science Experience" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Dynamic career of 20+ years that reflects rich Software Development
and Project Management experience in Data Science and Data Engineering across e-Commerce, Automotive, FMCG & Supply Chain Management domains
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Sir,
I am excited to apply for the Data Analyst position at Sherwin Williams. With a proven background in data analysis, visualization, and actionable insights generation, coupled with 20 yrs of experience working in data-driven roles, I am eager to contribute my expertise to support your mission of leveraging data for impactful decision-making.
In my previous role(s) at WIPRO, I successfully developed an automated dashboard that reduced reporting time by 30% and was able to reduce 5 redundant jobs. My experience includes analyzing large datasets, ensuring data integrity, and creating intuitive visualizations that guide strategic planning. I am proficient in tools like SQL, Python, Tableau/BI, and Excel, and I have experience working with cloud technologies such as Google Big Query and AWS to manage and analyze data effectively.
What excites me most about the opportunity at Williams is working for products which most of the industries and humans are consuming. My ability to combine technical expertise with strategic thinking aligns perfectly with your mission.
Some highlights of my qualifications include:
•	Data Analysis and Interpretation: Expertise in deriving actionable insights from complex datasets, supporting leadership in making informed decisions.
•	Advanced Reporting Skills: Skilled in creating automated, interactive dashboards using BI/ Node technologies, enabling real-time monitoring and improved communication.
•	Problem-Solving Mindset: Adept at identifying data anomalies, ensuring accuracy, and providing solutions for process improvement.
Beyond technical skills, I take pride in my ability to collaborate with cross-functional teams, communicate findings effectively, and adapt to the evolving demands of data analytics. I am confident that my skills and passion for data will make me an asset to your team.
I would welcome the opportunity to discuss how my background, skills, and enthusiasm can contribute to the success of Sherwin Williams. Thank you for considering my application. I look forward to the possibility of contributing to your team and am available at your earliest convenience for an interview.
Sincerely,
Vikas Malik
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Dispute Resolution Center" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Vikas Malik
'''
############################################################################################################
