import pandas as pd
import re
from word2number import w2n
from config import SKILLS_DICT,EDUCATION_PRIORITY,CATEGORIES,AGE_PHRASES,COMPANY_PHRASES

class SkillsExtractor:

    def __init__(self):
        self.skills_dict=SKILLS_DICT
        self.education_priority=EDUCATION_PRIORITY
        self.categories=CATEGORIES
        self.age_phrases = AGE_PHRASES
        self.company_phrases = COMPANY_PHRASES

    def extract_skills(self,df):
        if 'skills' not in df.columns:
            df['skills'] = None
        
        df['skills'] = df.apply(lambda row:", ".join(
            list(set([self.skills_dict[skill] for skill in self.skills_dict.keys() if skill in row['description_clean']]))
        ) if pd.isna(row['skills']) or row['skills'] == "" else row['skills'],
        axis=1)

        return df

    def extract_highest_education(self,skills):

        normalized_priority = {key.lower(): value for key, value in self.education_priority.items()}
        education_levels = [level for level in skills if level.lower() in normalized_priority]

        if education_levels:
            return max(education_levels, key=lambda x:normalized_priority[x.lower()])
        return None
    
    def word_to_number(self,text):
        try:
            return w2n.word_to_num(text.lower())
        except:
            return None
    
    def extract_experience(self,text):
        for phrase in self.age_phrases:
            text = re.sub(r'\b' + re.escape(phrase) + r'\b', "", text, flags=re.IGNORECASE)

        for phrase in self.company_phrases:
            text = re.sub(r'\b' + re.escape(phrase) + r'\b.*?(\d{1,2})\s*(Years|years|year|yrs)',"",text,flags=re.IGNORECASE)

        regex_words = r'(\b(?:twenty|nineteen|eighteen|seventeen|sixteen|fifteen|fourteen|thirteen|twelve|eleven|ten|nine|eight|seven|six|five|four|three|two|one)\b)\s*\(?(\d{1,2})?\)?\s*(years|year|yrs)'

        match_words = re.search(regex_words,text,re.IGNORECASE)

        if match_words:
            if match_words.group(2):
                number = int(match_words.group(2))
            else:
                number = self.word_to_number(match_words.group(1))
            if number is not None and number < 21:
                return number

        regex_range = r'(\d+)\s*-\s*(\d+)\s*(years|year|yrs)'
        match_range = re.search(regex_range,text,re.IGNORECASE)
        if match_range:
            lower = int(match_range.group(1))
            upper = int(match_range.group(2))
            experience = (lower + upper - 1) // 2
            if experience < 21:
                return experience
        
        regex_exp = r'(\d+)\+?\s*(years|year|yrs)'
        match = re.search(regex_exp,text,re.IGNORECASE)
        if match:
            experience = int(match.group(1))
            if experience < 21:
                return experience
        
        return 0

    def new_column_extract_skills(self,df,skills_column):

        result = pd.DataFrame(index=df.index)
        for category, skills_set in self.categories.items():
            result[category] = df[skills_column].apply(lambda x: ', '.join(skill for skill in map(str.strip, x.split(',')) if skill in skills_set))
        
        return pd.concat([df,result], axis=1)


        