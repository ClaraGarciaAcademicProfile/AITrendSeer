# AITrendSeer - Machine Learning Pipeline

"What doesn't kill your model makes it robust" - Modern Data Stoicism

A comprehensive data preprocessing and modeling framework that embraces the chaos of real-world data with philosophical resilience.

## Description

Features:
* Data Processing Pipeline
* Missing value handling:

"Medians don't lie" (Numerical imputation)

"When in doubt, label it 'UNKNOWN'", as a new category (Categorical imputation philosophy)

Feature transformations:

* "One-Hot Encoding: Because sometimes categories need personal space"

* "Standard Scaling: Keeping your features as balanced as a Stoic's emotions (-1 to 1)"

Automatic train-test splitting:

* "The 20% you must let go of (practice data detachment)"

## Supported Models
Linear Regression with Ridge:

"Discipline for overenthusiastic coefficients"

## Model metrics:

"MSE: Measuring suffering in squared units"

"R²: The virtue of explained variance"

## Visualization
"Plots so clear even Marcus Aurelius would approve"

"Feature importance: Knowing what truly matters"

Project Structure

## Project Structure
```bash
AITrendSeer/
│
├── data/                          
│   ├── raw/                      # "the unexamined data is not worth using" - Socrates (probably)
│   └── processed/                # data after Stoic transformation
│
├── models/                       # where we keep our disciplined models
│
├── notebooks/                    # thought experiments
│   └── simple_linear_regression.ipynb  # "Meditations on Linear Relationships"
│
├── src/                          # our digital Stoa
│   ├── preprocessing/            # data purification rituals
│   └── config.py                 # the Stoic's handbook for datasets
│
├── tests/                        # trials by fire
│
└── visualizations/               # "Pictures speak louder than p-values
```

## Quick Start
Install dependencies (wisdom begins with preparation):

```
bash
pip install -r requirements.txt
```

Run the pipeline (face your data with courage):
```
bash
python main.py
```
Explore the notebook (contemplate the nature of variables):

```
bash
jupyter notebook notebooks/simple_linear_regression.ipynb
```
"The obstacle in the data becomes the way to better features" - Epictetus (if he did feature engineering)