import pandas as pd
import sqlite3
from utils.scraper import ScraperJobs
from utils.data_cleaning import DataCleaning

def main():

    '''searches = ["data analyst", "data scientist", "data engineer"]
    sites = ["indeed"]
    results = 1000
    old = 1000
    country = "USA"

    scraper = ScraperJobs()
    df = scraper.scraper_jobs(searches,sites,results,old,country)

    conn = sqlite3.connect('jobs.db')
    df.to_sql('jobs_raw_table', conn, if_exists='append', index=False)
    conn.close()

    df.to_csv('jobs_raw_table.csv')'''

    conn = sqlite3.connect('jobs2.db')
    query = "SELECT * FROM jobs_backup"
    df = pd.read_sql_query(query,conn)

    datacleaner = DataCleaning()

    df_processed = datacleaner.clean_data_jobs(df)

    df_processed_sql = df_processed[['id','site','job_url','job_url_direct','title','company','date_posted','level','job_group','remote',
                                     'city','state','country','city_state','max_salary','min_salary','mean_salary','skills','experience',
                                     'education','programming_languages','languages']]

    df_processed_sql.to_sql('jobs_cleaned_table',conn, if_exists='replace',index=False)

    conn.close()

if __name__ == "__main__":
    main()