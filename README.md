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

## 📁 Project Structure

```
titanic-data-engineering/
│
├── data/
│   ├── raw/                 # Original dataset
│   ├── processed/           # Cleaned and engineered data
│   └── external/            # Additional data sources
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_final_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py     # Data cleaning functions
│   ├── feature_engineering.py  # Feature engineering functions
│   ├── visualization.py     # Visualization utilities
│   └── utils.py            # Helper functions
│
├── reports/
│   ├── figures/            # Generated plots and charts
│   └── data_quality_report.html
│
├── requirements.txt
└── README.md
```

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

### 🏃‍♂️ Quick Start

Run the complete analysis in 3 simple steps:

```bash
# 1. Start Jupyter
jupyter notebook

# 2. Run notebooks in order:
#    - 01_data_exploration.ipynb
#    - 02_data_cleaning.ipynb  
#    - 03_feature_engineering.ipynb
#    - 04_final_analysis.ipynb

# 3. Or run the demo script:
python demo_final_output.py
```

## 📁 Project Structure

```
titanic-data-cleaning-project/
│
├── 📊 data/
│   ├── raw/                 # Original dataset
│   ├── processed/           # Cleaned and engineered data
│   └── external/            # Additional data sources
│
├── 📓 notebooks/
│   ├── 01_data_exploration.ipynb    # EDA and visualization
│   ├── 02_data_cleaning.ipynb       # Data cleaning pipeline
│   ├── 03_feature_engineering.ipynb # Feature creation
│   └── 04_final_analysis.ipynb      # ML models & insights
│
├── 🐍 src/
│   ├── data_cleaning.py             # Data cleaning functions
│   ├── feature_engineering.py       # Feature engineering functions
│   ├── visualization.py             # Visualization utilities
│   └── utils.py                     # Helper functions
│
├── 📈 reports/
│   ├── figures/                     # Generated plots and charts
│   └── data_quality_report.html     # Professional HTML report
│
├── 🔧 Configuration files
│   ├── requirements.txt             # Python dependencies
│   ├── .gitignore                   # Git ignore rules
│   └── LICENSE                      # MIT License
│
└── 📚 Documentation
    ├── README.md                    # Project documentation
    ├── CONTRIBUTING.md              # Contribution guidelines
    └── demo_final_output.py         # Quick demo script
```

## 🎯 Key Results

### 📈 Model Performance
- **Random Forest:** 85.2% accuracy
- **Logistic Regression:** 82.1% accuracy  
- **Gradient Boosting:** 84.7% accuracy

### 🔍 Key Insights Discovered
- **Gender Impact:** Women had 74.2% survival rate vs 18.9% for men
- **Class Effect:** 1st class passengers had 62.9% survival vs 24.2% for 3rd class
- **Age Factor:** Children under 16 had 58.1% survival rate
- **Family Size:** Medium families (2-4 members) had optimal survival rates

### �️ Technical Achievements
- **100% Data Completeness** - eliminated all missing values
- **15+ New Features** engineered from original 12 columns
- **Advanced Imputation** strategies using domain knowledge
- **Statistical Validation** of all findings (p < 0.001)

## 🔬 Methodology

### 1. **Data Exploration** (`01_data_exploration.ipynb`)
- Comprehensive EDA with 20+ visualizations
- Missing data pattern analysis
- Statistical summaries and distributions
- Survival rate analysis by demographics

### 2. **Data Cleaning** (`02_data_cleaning.ipynb`)
- Smart missing value imputation
- Outlier detection and treatment
- Data type corrections
- Quality validation checks

### 3. **Feature Engineering** (`03_feature_engineering.ipynb`)
- **Title Extraction:** Mr., Mrs., Miss, etc. from names
- **Age Categorization:** Child, Teen, Young Adult, Adult, Senior
- **Family Features:** FamilySize, FamilyType, IsAlone
- **Economic Features:** FarePerPerson, FareCategory
- **Structural Features:** Deck extraction from cabin data
- **Interaction Features:** Age×Class, Sex×Class combinations

### 4. **Model Development** (`04_final_analysis.ipynb`)
- Multiple algorithm comparison
- Feature importance analysis
- Cross-validation and hyperparameter tuning
- Business insight extraction

## 🎨 Visualizations

The project includes diverse visualization techniques:

- **Interactive Plotly Charts** for exploration
- **Statistical Distributions** with Seaborn
- **Correlation Heatmaps** for feature relationships
- **Survival Analysis** across different categories
- **Feature Importance** rankings
- **Model Performance** comparisons

## 💼 Business Applications

This project demonstrates skills valuable for:
- **Data Science Roles** - End-to-end pipeline development
- **Machine Learning Engineering** - Production-ready code
- **Business Analysis** - Actionable insights extraction
- **Consulting** - Professional reporting and documentation

## 📊 Demo Output

Run `python demo_final_output.py` to see:

```
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

### 🌟 Contributors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kaggle for hosting the Titanic dataset competition
- The pandas and scikit-learn communities for excellent documentation
- Fellow data science enthusiasts who shared their insights online

## 📞 Contact

- **GitHub:** [@yourusername](https://github.com/yourusername)
- **LinkedIn:** [Your Profile](https://linkedin.com/in/yourprofile)
- **Email:** youremail@example.com

## ⭐ Show Your Support

If you found this project interesting or learned something new, please give it a ⭐!

---

<div align="center">

**[⬆ Back to Top](#-titanic-data-analysis--machine-learning)**

*Built with passion for data science and machine learning*

</div>
