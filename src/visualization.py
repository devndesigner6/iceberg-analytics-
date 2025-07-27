import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_distribution(df, column):
    plt.figure(figsize=(8,4))
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def plot_survival_by_category(df, category):
    fig = px.bar(df.groupby(category)['Survived'].mean().reset_index(), x=category, y='Survived', title=f'Survival Rate by {category}')
    fig.show()
