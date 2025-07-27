import pandas as pd
import numpy as np

def extract_title(df):
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    return df

def create_age_category(df):
    bins = [0, 12, 18, 35, 60, 120]
    labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
    df['AgeGroup'] = pd.cut(df['Age'], bins, labels=labels)
    return df

def family_size(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    return df

def fare_per_person(df):
    df['FarePerPerson'] = df['Fare'] / df['FamilySize']
    return df

def extract_deck(df):
    df['Deck'] = df['Cabin'].str[0]
    return df

def encode_categoricals(df):
    df = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title', 'AgeGroup', 'Deck', 'Pclass'], drop_first=True)
    return df

def scale_features(df):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[['Age', 'Fare', 'FarePerPerson']] = scaler.fit_transform(df[['Age', 'Fare', 'FarePerPerson']])
    return df

def engineer_features(df):
    df = extract_title(df)
    df = create_age_category(df)
    df = family_size(df)
    df = fare_per_person(df)
    df = extract_deck(df)
    df = encode_categoricals(df)
    df = scale_features(df)
    return df
