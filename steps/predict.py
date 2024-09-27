import os
import joblib
import yaml
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score


class Predictor:
    def __init__(self):
        self.config = self.load_config()
        self.model_path = self.config['model']['store_path']
        self.model_name = self.config['model']['name']
        self.pipeline = self.load_model()

    def load_config(self):
        with open('config.yml', 'r') as config_file:
            return yaml.safe_load(config_file)

    def load_model(self):
        model_file_path = os.path.join(self.model_path, self.model_name + '_model.pkl')
        return joblib.load(model_file_path)

    def feature_target_separator(self, data):
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        return X, y

    def evaluate_model(self, X_test, y_test):
        y_pred = self.pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        class_report = classification_report(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)
        return accuracy, class_report, roc_auc
