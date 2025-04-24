import pandas as pd
from jobspy import scrape_jobs

class ScraperJobs:

    def __init__(self):
        pass

    def scraper_jobs(self, searches, sites, results, old, country):

        df = pd.DataFrame()
        for search in searches:
            jobs = scrape_jobs(
               site_name=sites,
               search_term=search,
               results_wanted=results,
               hours_old=old,
               country_indeed=country, 
            )
            print(f"Found {len(jobs)} jobs")

            df_search = pd.DataFrame(jobs)
            df = pd.concat([df, df_search], ignore_index=True)

        df = df.drop_duplicates(subset = ['id'])
        return df
