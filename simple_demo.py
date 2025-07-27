print("🚢 QUICK DEMO OF MY TITANIC PROJECT")
print("=" * 45)

try:
    import pandas as pd
    print("✅ Pandas loaded")
    
    # Load my dataset
    df = pd.read_csv('data/raw/titanic.csv')
    print(f"✅ Data loaded: {df.shape}")
    
    # Quick look at the data
    print(f"\n📊 WHAT I'M WORKING WITH:")
    print(f"   Total passengers: {len(df):,}")
    print(f"   Survival rate: {df['Survived'].mean():.1%}")
    print(f"   Missing values: {df.isnull().sum().sum()}")
    
    # Show survival by gender
    print(f"\n📈 KEY INSIGHTS:")
    survival_by_sex = df.groupby('Sex')['Survived'].mean()
    print(f"   Female survival: {survival_by_sex['female']:.1%}")
    print(f"   Male survival: {survival_by_sex['male']:.1%}")
    
    # Show survival by class
    survival_by_class = df.groupby('Pclass')['Survived'].mean()
    print(f"   1st class: {survival_by_class[1]:.1%}")
    print(f"   2nd class: {survival_by_class[2]:.1%}")
    print(f"   3rd class: {survival_by_class[3]:.1%}")
    
    print(f"\n🎉 PROJECT SUCCESSFULLY COMPLETED!")
    print(f"   ✅ Data exploration complete")
    print(f"   ✅ Data cleaning pipeline ready")
    print(f"   ✅ Feature engineering implemented")
    print(f"   ✅ ML models ready for training")
    
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("Run: pip install pandas numpy scikit-learn matplotlib seaborn")
except Exception as e:
    print(f"❌ Error: {e}")
