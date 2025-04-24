import pandas as pd
from config import JOB_LEVEL_DICT, JOB_GROUP_DICT, REMOTE_KEYWORDS

class JobsCategorization:

    def __init__(self):

        self.job_level_dict = JOB_LEVEL_DICT
        self.job_group_dict = JOB_GROUP_DICT
        self.remote_keywords = REMOTE_KEYWORDS

    def job_level(self,job_name):

        job_name_lower = job_name.lower()

        for value, profile in self.job_level_dict.items():
            if value.lower() in job_name_lower:
                return profile
        return 'Mid-Level'
    
    def job_group(self,job_name):
        
        job_name_lower = job_name.lower()

        for keyword,category in self.job_group_dict.items():
            if keyword.lower() in job_name_lower:
                return category  
        return "Others"
    
    def remote_jobs (self,row):

        if pd.isna(row.get('location')):
            return 'Remote'
        
        description_lower = row.get('description',"").lower()
        location_lower = row.get('location',"").lower()
        title_lower = row.get('title',"").lower()

        if any(keyword in description_lower for keyword in self.remote_keywords):
            return 'Hybrid' if 'hybrid' in description_lower else 'Remote'
        if any(keyword in location_lower for keyword in self.remote_keywords):
            return 'Hybrid' if 'hybrid' in location_lower else 'Remote'
        if any(keyword in title_lower for keyword in self.remote_keywords):
            return 'Hybrid' if 'hybrid' in title_lower else 'Remote'
        
        return 'On Site'

    def check_is_remote(self,row):

        if row['remote'] in ['Remote','Hybrid']:
            return row['remote']

        elif pd.notna(row.get('is_remote')) and row['is_remote'] == 1.0:
            return 'Hybrid'
        
        return 'On Site'



