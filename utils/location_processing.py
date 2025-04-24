from config import STATES_DICT

class LocationProcessor:

    def __init__(self):
        self.states_dict = STATES_DICT

    def find_state(self,location):
        for state,code in self.states_dict.items():
            if state.lower() in location.lower():
                return code
        return None
    
    def parse_location(self,location):
        parts = [p.strip() for p in location.split(',')]

        if len(parts) == 3:
            return parts[1], parts[0], parts[2]
        
        elif len(parts) == 2:
            if "US" in location or "United States" in location:
                return parts[0],None,parts[1]
            else:
                return parts[1],parts[0],None
            
        state = self.find_state(location)
        return state, None,None
    
    def city_state(self,df):

        df['city'] = None
        df['state'] = None
        df['country'] = None

        for idx, row in df.iterrows():
            location = row['location']

            if isinstance(location,str):
                df.at[idx,'state'],df.at[idx,'city'],df.at[idx,'country'] = self.parse_location(location)

        df['state'] = df['state'].replace(['Remote',r'^Remote in ', r'^Hybrid remote in '], None, regex=True)
        df['city'] = df['city'].replace(['Remote',r'^Remote in ', r'^Hybrid remote in '], None, regex=True)

        df['city_state'] = df['city'] + ',' + df['state']

        return df