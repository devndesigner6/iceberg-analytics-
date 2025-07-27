"""
Data cleaning functions for the Titanic dataset.

I created these functions to handle the most common data quality issues
I found while exploring the Titanic dataset. Each function addresses
specific problems I encountered during my analysis.

Author: Your Name
"""

import pandas as pd
import numpy as np

def load_data(path):
    """Simple function to load the dataset"""
    return pd.read_csv(path)

def handle_missing_values(df):
    """Handle missing values based on my analysis of the data"""
    # After exploring the data, I decided on these strategies:
    # - Age: Use median since it's less affected by outliers
    # - Embarked: Use mode (most common port)  
    # - Cabin: Mark as 'Unknown' since so many are missing
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df['Cabin'].fillna('Unknown', inplace=True)
    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def correct_data_types(df):
    df['Survived'] = df['Survived'].astype(int)
    df['Pclass'] = df['Pclass'].astype(int)
    df['Age'] = df['Age'].astype(float)
    df['Fare'] = df['Fare'].astype(float)
    return df

def clean_data(path):
    df = load_data(path)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = correct_data_types(df)
    return df
