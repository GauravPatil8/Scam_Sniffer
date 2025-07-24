import os
import joblib
import numpy as np
import pandas as pd
from ScamSniffer.utils.stages import Stages
from ScamSniffer.utils.common import read_yaml
from ScamSniffer.constants.common import CONFIG_PATH, PROJECT_ROOT
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


class DataTransformer(Stages):

    def __init__(self ):
        self.config = read_yaml(CONFIG_PATH)

    def run(self):
        kaggle_dataset = pd.read_csv(os.path.join(PROJECT_ROOT ,self.config.data_transformation.kaggle_dataset))
        simulated_dataset = pd.read_csv(os.path.join(PROJECT_ROOT ,self.config.data_transformation.simulated_dataset))

        # The job decription in the dataset is split into many features, combining them all in one feature
        description_merged = kaggle_dataset["company_profile"].astype(str) + " " + kaggle_dataset["description"].astype(str) + " "+kaggle_dataset["requirements"].astype(str) + " " + kaggle_dataset["benefits"].astype(str)

        kaggle_dataset["description"] = description_merged

        kaggle_dataset_filtered = kaggle_dataset[["description", "fraudulent"]]

        # Appending another dataset at the bottom
        raw_data = pd.concat([kaggle_dataset_filtered, simulated_dataset[["description", "fraudulent"]]])


        # Train test split
        X = raw_data["description"]
        Y = raw_data["fraudulent"]

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)


        #feature extraction
        feature_extraction = TfidfVectorizer(min_df=1, stop_words = 'english', lowercase= True)

        X_train_features = feature_extraction.fit_transform(X_train)
        X_test_features = feature_extraction.transform(X_test)

        output_dir = os.path.join(PROJECT_ROOT, self.config.data_transformation.root_dir)
        os.makedirs(output_dir, exist_ok=True)


        # saving the features
        joblib.dump(feature_extraction, os.path.join(output_dir, "tfidf_vectorizer.pkl"))
        joblib.dump(X_train_features, os.path.join(output_dir, "X_train_tfidf.pkl"))
        joblib.dump(X_test_features, os.path.join(output_dir, "X_test_tfidf.pkl"))
        joblib.dump(Y_train, os.path.join(output_dir, "Y_train.pkl"))
        joblib.dump(Y_test, os.path.join(output_dir, "Y_test.pkl"))


