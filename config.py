import pandas as pd

job_level_df = pd.read_excel('master_data/profile.xlsx')
JOB_LEVEL_DICT = job_level_df.set_index('Value')['Profile'].to_dict()

job_group_df = pd.read_excel('master_data/categories.xlsx')
JOB_GROUP_DICT = job_group_df.set_index('keyword')['category'].to_dict()

REMOTE_KEYWORDS = ['remote','hybrid','on site']

states_df = pd.read_excel('master_data/states.xlsx')
STATES_DICT = states_df.set_index('State')['Code'].to_dict()

INTERVAL_FACTORS = {'yearly':1,'monthly':12,'weekly':49,'daily':230,'hourly':1840,}

skills_df = pd.read_excel('master_data/skills.xlsx')
SKILLS_DICT = skills_df.set_index('Skills')['Group'].to_dict()

EDUCATION_PRIORITY = {"None":0,"Bachelor":1,"Master":2,"MBA":3,"PhD":4}

CATEGORIES = {'programming_languages':{"DAX","Python","R","SQL","JavaScript","VBA","Rust","C++","C#","HTML","PHP","CSS","ABAP","Java","Julia"},
              'languages':{"English","Spanish","German","Italian","French","Russian","Chinese","Japanese","Hindi"}
              }

AGE_PHRASES = ["Yearly","Adolescence (13 to 17 years)","years!","last 20 years","years in a row","years in age","Must be 18 years",
               "years-old","years old","years of age","yrs of age","years or older", "years or over","years and older","yrs or older","yrs. or older","or older"]

COMPANY_PHRASES = ["designs up to","For more than **","For more than","Minimum age requirement is","For over","for over","provider with more than","celebrating",
                   "In over","We are","with over","has over","company experience","years in business","years of success","in operation for","founded"]

