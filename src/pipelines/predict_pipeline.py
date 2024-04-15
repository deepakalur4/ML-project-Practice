from src.exception import Custom_exception
from src.logger import logging
import os
from src.utils import load_object
import pandas as pd
import sys

class predict_pipeline_1:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocesser_path=os.path.join("artifacts","preprocessor.pkl")
            logging.info("Before loading")
            model=load_object(file_path=model_path)
            preprocesser=load_object(file_path=preprocesser_path)
            logging.info("after loading")
            data_scaled=preprocesser.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise Custom_exception(e,sys) 

class custom_data:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score
        
    def get_data_as_dataframe(self):
        try:
            custom_data_1= {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_1)
        
        except Exception as e:
            raise Custom_exception(e,sys) 