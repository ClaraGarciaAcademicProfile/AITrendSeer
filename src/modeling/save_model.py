import joblib
import os

#save model
def save_model(model, dataset_name, model_name):
    os.makedirs(f"models/{dataset_name}", exist_ok=True)
    joblib.dump(model, f"models/{dataset_name}/{model_name}.pkl")
    print(f"Model saved to models/{dataset_name}/{model_name}.pkl")