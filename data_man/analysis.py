import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analysis(data: pd.DataFrame):

    pd.set_option("display.precision", 2)

    corr = data.corr()

    print(data.describe())
    print(data.head())
    print(corr)

    data.boxplot()
    plt.show()

    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation between features')
    plt.show()

    pd.reset_option("display.precision")