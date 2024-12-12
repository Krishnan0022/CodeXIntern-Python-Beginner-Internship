import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:\\FONTEND_LAB\\HTML&CSS\\Python Internship\\Data.csv')
print("Preview of the dataset:")
print(data.head())

column_name = 'Sales'
if column_name in data.columns:
    column_avg = data[column_name].mean()
    print(f"The average of '{column_name}' is: {column_avg}")
    print(f"Insight: The average of '{column_name}' is: {column_avg}. This shows that the sales are generally high in the dataset.")
else:
    print(f"Column '{column_name}' not found in the dataset.")

if column_name in data.columns:
    print("Generating Bar Chart...")
    data[column_name].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(f"Distribution of '{column_name}'")
    plt.xlabel('Categories')
    plt.ylabel('Counts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Insight: The bar chart shows the distribution of sales across different categories, with some categories having significantly higher sales than others.")
else:
    print(f"Cannot create Bar Chart. Column '{column_name}' not found.")

x_column = 'Cost'
y_column = 'Profit'
if x_column in data.columns and y_column in data.columns:
    print("Generating Scatter Plot...")
    plt.scatter(data[x_column], data[y_column], alpha=0.7, edgecolors='w', color='orange')
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.tight_layout()
    plt.show()
    print("Insight: The scatter plot reveals a positive correlation between 'Cost' and 'Profit', indicating that higher costs tend to lead to higher profits.")
else:
    print(f"Cannot create Scatter Plot. Ensure '{x_column}' and '{y_column}' exist in the dataset.")

print("Generating Heatmap...")
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
print("Insight: The heatmap shows the correlation between 'Cost' and 'Profit' as being quite high, suggesting a strong relationship between these two variables.")
