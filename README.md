# 🚢 Titanic Data Analysis & Machine Learning

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

*My personal exploration of the Titanic dataset through comprehensive data cleaning, feature engineering, and machine learning.*

[Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Features](#-features) • [Results](#-results) • [Contributing](#-contributing)

</div>

## 🌟 What I've Built

- **85%+ Model Accuracy** through careful feature engineering
- **15+ New Features** extracted from the original dataset
- **Complete Data Pipeline** from raw data to predictions
- **Clean, Modular Code** that's easy to understand and extend
- **Interactive Visualizations** to explore the data
- **Detailed Analysis** with insights about passenger survival

## 📊 Dataset

The Titanic dataset contains information about passengers aboard the RMS Titanic, including:
- **PassengerId**: Unique identifier for each passenger
- **Survived**: Survival status (0 = No, 1 = Yes)
- **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- **Name**: Passenger name
- **Sex**: Gender
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Ticket**: Ticket number
- **Fare**: Passenger fare
- **Cabin**: Cabin number
- **Embarked**: Port of embarkation

## 🔧 Features Implemented

### Data Cleaning
- ✅ Missing value identification and handling
- ✅ Duplicate detection and removal
- ✅ Data type corrections and validation
- ✅ Outlier detection and treatment
- ✅ Data consistency checks

### Feature Engineering
- ✅ Title extraction from names
- ✅ Age group categorization
- ✅ Family size calculation
- ✅ Fare per person calculation
- ✅ Deck extraction from cabin numbers
- ✅ Ticket class-based features
- ✅ One-hot encoding for categorical variables
- ✅ Feature scaling and normalization

### Advanced Analytics
- ✅ Comprehensive exploratory data analysis
- ✅ Statistical summaries and distributions
- ✅ Correlation analysis
- ✅ Interactive visualizations
- ✅ Feature importance analysis

## 🛠️ Technologies Used

- **Python 3.8+**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Static visualizations
- **seaborn** - Statistical data visualization
- **plotly** - Interactive visualizations
- **scikit-learn** - Machine learning preprocessing
- **jupyter** - Interactive development environment

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Git

### 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/titanic-data-cleaning-project.git
   cd titanic-data-cleaning-project
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**
   - The Titanic dataset is included in `data/raw/titanic.csv`
   - Original source: [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)

🚢 TITANIC DATA SCIENCE PROJECT - FINAL OUTPUT
============================================================
✅ Dataset loaded successfully!
   Shape: (891, 12)
   Missing values: 866

📊 DATASET OVERVIEW:
   Total passengers: 891
   Survival rate: 38.4%
   Features: 12

🔍 MISSING DATA ANALYSIS:
   Age: 177 (19.9%)
   Cabin: 687 (77.1%)
   Embarked: 2 (0.2%)

🧹 DATA CLEANING PROCESS:
   ✅ Missing values handled

🔧 FEATURE ENGINEERING:
   ✅ Titles extracted: 17 unique titles
   ✅ Family size calculated
   ✅ Age groups created
   ✅ Fare per person calculated

📈 KEY SURVIVAL INSIGHTS:
   Female survival rate: 74.2%
   Male survival rate: 18.9%
   1st class survival: 62.9%
   2nd class survival: 47.3%
   3rd class survival: 24.2%

🤖 MACHINE LEARNING PREPARATION:
   Features prepared: 9
   Final dataset shape: (891, 9)

🏆 FINAL MODEL RESULTS:
   Model: Random Forest
   Accuracy: 85.2%
   Training samples: 712
   Test samples: 179

🔍 TOP 5 MOST IMPORTANT FEATURES:
   1. Sex_male: 0.284
   2. Fare: 0.263
   3. Age: 0.174
   4. FamilySize: 0.089
   5. Pclass: 0.067

🎉 PROJECT COMPLETED SUCCESSFULLY!
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kaggle for hosting the Titanic dataset competition
- The pandas and scikit-learn communities for excellent documentation
- Fellow data science enthusiasts who shared their insights online

## ⭐ Show Your Support

If you found this project interesting or learned something new, please give it a ⭐!
