
import os
import json
import joblib
from ScamSniffer.utils.stages import Stages
from ScamSniffer.utils.common import read_yaml
from ScamSniffer.constants.common import CONFIG_PATH, PROJECT_ROOT
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, classification_report

class ModelEvaluator(Stages):
    def __init__(self):
        self.config = read_yaml(CONFIG_PATH)


    def run(self):
        X_test = joblib.load(os.path.join(PROJECT_ROOT, self.config.data_transformation.root_dir,"X_test_tfidf.pkl"))
        Y_test = joblib.load(os.path.join(PROJECT_ROOT, self.config.data_transformation.root_dir,"Y_test.pkl"))

        # Load trained model
        model = joblib.load(os.path.join(PROJECT_ROOT, self.config.model_trainer.root_dir,"xgboost_job_classifier.pkl"))

        # Predict
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

        accuracy = accuracy_score(Y_test, y_pred)
        f1 = f1_score(Y_test, y_pred)
        report_dict = classification_report(Y_test, y_pred, output_dict=True)
        roc_auc = roc_auc_score(Y_test, y_proba) if y_proba is not None else None

        metrics = {
            "accuracy": accuracy,
            "f1_score": f1,
            "roc_auc": roc_auc,
            "classification_report": report_dict
        }

        os.makedirs(os.path.join(PROJECT_ROOT, self.config.model_evaluator.root_dir), exist_ok=True)
        with open(os.path.join(PROJECT_ROOT, self.config.model_evaluator.root_dir,"evaluation_metrics.json"), "w") as f:
            json.dump(metrics, f, indent=4)

    
