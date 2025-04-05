# main.py
from src.preprocessing.load_data import load_dataset
from src.preprocessing.clean_data import handle_missing_values
from src.preprocessing.transform import encode_target, encode_categorical, scale_numerical, one_hot_encode
from src.preprocessing.split_data import split_and_save
from src.modeling.save_model import save_model
from src.modeling.test_model import evaluate_model
from src.config import DATASETS
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import pandas as pd

def process_dataset(name):
    print(f"\nProcessing: {name}")
    config = DATASETS[name]
    
    try:
        # 1. load and preprocess data
        df = load_dataset(name)
        df = handle_missing_values(df, config)
        df = one_hot_encode(df, config)
        df = encode_target(df, config)
        df = encode_categorical(df, config)
        
        # 2. scale features 
        if "numerical_cols" in config:
            scaler = StandardScaler()
            num_cols = [col for col in config["numerical_cols"] if col in df.columns]
            df[num_cols] = scaler.fit_transform(df[num_cols])
        
        # 3. split data
        split_and_save(df, config, name)
        
        # 4. train Ridge model
        X = df.drop(columns=[config["target"]])
        y = df[config["target"]]
        
        model = Ridge(alpha=1.0) 
        model.fit(X, y)
        
        # 5. save model and evaluate
        save_model(model, name, "ridge_model")
        y_pred = model.predict(X)
        metrics = evaluate_model(y, y_pred, name, "ridge_regression")
        
        # 6. basic visualization (actual distribution vs predictions)
        #fig, ax = plt.subplots(figsize=(10, 6))
        #ax.scatter(y, y_pred, alpha=0.3)
        #ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
        #ax.set_xlabel('Actual')
        #ax.set_ylabel('Predicted')
        #save_plot(fig, name, "actual_vs_predicted")
        
        return True
    
    except Exception as e:
        print(f"Error processing {name}: {str(e)}")
        return False

if __name__ == "__main__":
    # process all datasets
    for dataset_name in DATASETS.keys():
        process_dataset(dataset_name)