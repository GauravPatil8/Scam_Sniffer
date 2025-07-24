import os
import joblib
from ScamSniffer.utils.stages import Stages
from ScamSniffer.utils.common import read_yaml
from ScamSniffer.constants.common import CONFIG_PATH, PROJECT_ROOT
from xgboost import XGBClassifier

class ModelTrainer(Stages):

    def __init__(self):
        self.config = read_yaml(CONFIG_PATH)
        feature_dir = os.path.join(PROJECT_ROOT, self.config.model_trainer.feature_files)
        self.vectorizer = joblib.load(os.path.join(feature_dir, "tfidf_vectorizer.pkl"))
        self.X_train = joblib.load(os.path.join(feature_dir, "X_train_tfidf.pkl"))
        self.X_test = joblib.load(os.path.join(feature_dir, "X_test_tfidf.pkl"))
        self.y_train = joblib.load(os.path.join(feature_dir, "Y_train.pkl"))
        self.y_test = joblib.load(os.path.join(feature_dir, "Y_test.pkl"))

    def run(self):

        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

        model.fit(self.X_train, self.y_train)
        os.makedirs(os.path.join(PROJECT_ROOT, self.config.model_trainer.root_dir), exist_ok=True)
        joblib.dump(model, os.path.join(PROJECT_ROOT, self.config.model_trainer.root_dir, "xgboost_job_classifier.pkl"))
    

