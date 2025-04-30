# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# Load and summarize
df = pd.read_excel("your_data.csv")
print(df.describe())
print(df.info())

# visual: distribution
sns.histplot(df['age'], kde=True)
plt.title("Age Ditribution")
plt.show()

# visual: relationship
sns.scatterplot(x='age', y='income', data=df)
plt.title("Age vs Income")
plt.show()

# Statistical: correlation
print(df[['age', 'income']].corr())
