DATASETS = {      
    # Dataset Housing
    "housing": {
        "path": "data/raw/house_prediction_dataset.csv",
        "has_header": False,
        "space_delimited": True,
        "columns": ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"],
        "target": "MEDV",
        "numerical_cols": ["CRIM","ZN","INDUS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT"]
    },
}