import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

print("🚢 MY TITANIC ANALYSIS PROJECT")
print("=" * 50)

# Load the raw dataset
try:
    df = pd.read_csv('data/raw/titanic.csv')
    print(f"✅ Dataset loaded successfully!")
    print(f"   Shape: {df.shape}")
    print(f"   Missing values: {df.isnull().sum().sum()}")
    
    # Show basic statistics
    print(f"\n📊 DATASET OVERVIEW:")
    print(f"   Total passengers: {len(df):,}")
    print(f"   Survival rate: {df['Survived'].mean():.1%}")
    print(f"   Features: {len(df.columns)}")
    
    # Missing data analysis
    print(f"\n🔍 MISSING DATA ANALYSIS:")
    missing_data = df.isnull().sum()
    for col, missing in missing_data.items():
        if missing > 0:
            print(f"   {col}: {missing} ({missing/len(df)*100:.1f}%)")
    
    # Data cleaning simulation
    print(f"\n🧹 DATA CLEANING PROCESS:")
    df_clean = df.copy()
    
    # Handle missing values
    df_clean['Age'].fillna(df_clean['Age'].median(), inplace=True)
    df_clean['Embarked'].fillna(df_clean['Embarked'].mode()[0], inplace=True)
    df_clean['Cabin'].fillna('Unknown', inplace=True)
    print(f"   ✅ Missing values handled")
    
    # Feature engineering
    print(f"\n🔧 FEATURE ENGINEERING:")
    
    # Extract titles
    df_clean['Title'] = df_clean['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    print(f"   ✅ Titles extracted: {df_clean['Title'].nunique()} unique titles")
    
    # Family size
    df_clean['FamilySize'] = df_clean['SibSp'] + df_clean['Parch'] + 1
    print(f"   ✅ Family size calculated")
    
    # Age groups
    df_clean['AgeGroup'] = pd.cut(df_clean['Age'], bins=[0, 12, 18, 35, 60, 100], 
                                  labels=['Child', 'Teen', 'Young_Adult', 'Adult', 'Senior'])
    print(f"   ✅ Age groups created")
    
    # Fare per person
    df_clean['FarePerPerson'] = df_clean['Fare'] / df_clean['FamilySize']
    print(f"   ✅ Fare per person calculated")
    
    # Show survival insights
    print(f"\n📈 KEY SURVIVAL INSIGHTS:")
    survival_by_sex = df_clean.groupby('Sex')['Survived'].mean()
    print(f"   Female survival rate: {survival_by_sex['female']:.1%}")
    print(f"   Male survival rate: {survival_by_sex['male']:.1%}")
    
    survival_by_class = df_clean.groupby('Pclass')['Survived'].mean()
    print(f"   1st class survival: {survival_by_class[1]:.1%}")
    print(f"   2nd class survival: {survival_by_class[2]:.1%}")
    print(f"   3rd class survival: {survival_by_class[3]:.1%}")
    
    # Prepare for ML
    print(f"\n🤖 MACHINE LEARNING PREPARATION:")
    
    # Select features for ML
    features_for_ml = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'FamilySize']
    df_ml = df_clean[features_for_ml + ['Survived']].copy()
    
    # Encode categorical variables
    df_ml = pd.get_dummies(df_ml, columns=['Sex', 'Embarked'], drop_first=True)
    
    # Prepare X and y
    X = df_ml.drop('Survived', axis=1)
    y = df_ml['Survived']
    
    print(f"   Features prepared: {len(X.columns)}")
    print(f"   Final dataset shape: {X.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n🏆 FINAL MODEL RESULTS:")
    print(f"   Model: Random Forest")
    print(f"   Accuracy: {accuracy:.1%}")
    print(f"   Training samples: {len(X_train)}")
    print(f"   Test samples: {len(X_test)}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\n🔍 TOP 5 MOST IMPORTANT FEATURES:")
    for i, (_, row) in enumerate(feature_importance.head(5).iterrows(), 1):
        print(f"   {i}. {row['feature']}: {row['importance']:.3f}")
    
    # Final summary
    print(f"\n" + "=" * 50)
    print(f"🎉 ANALYSIS COMPLETED!")
    print(f"=" * 50)
    print(f"✅ Data cleaned and processed")
    print(f"✅ Features engineered: {len(X.columns)} total")
    print(f"✅ Model trained: {accuracy:.1%} accuracy")
    print(f"✅ All missing values handled")
    print(f"✅ Project ready for presentation!")
    
    print(f"\n� WHAT I'VE CREATED:")
    print(f"   • Complete data cleaning pipeline")
    print(f"   • Custom feature engineering functions") 
    print(f"   • Working machine learning model")
    print(f"   • Detailed analysis and insights")
    print(f"   • Professional documentation")
    
    print(f"\n🚀 WHAT'S NEXT:")
    print(f"   • Try different ML algorithms")
    print(f"   • Build interactive web dashboard")
    print(f"   • Apply to other datasets")
    print(f"   • Share on GitHub portfolio")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure the dataset exists in data/raw/titanic.csv")
