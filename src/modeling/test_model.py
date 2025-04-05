import pandas as pd
import os
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, classification_report

#test model
def evaluate_model(y_true, y_pred, dataset_name, model_name):
    os.makedirs(f"tests/{dataset_name}", exist_ok=True)
    
    if y_true.nunique() > 10:  # regression
        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        metrics = pd.DataFrame({"MSE": [mse], "MAE": [mae], "R2": [r2]})
    else:  #classification
        report = classification_report(y_true, y_pred, output_dict=True)
        metrics = pd.DataFrame(report).transpose()
    
    metrics.to_csv(f"tests/{dataset_name}/{model_name}_metrics.csv")
    print(f"Metrics saved to tests/{dataset_name}/{model_name}_metrics.csv")
    return metrics