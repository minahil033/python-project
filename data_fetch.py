import pandas as pd

class CustomerChurnAnalyzer:
    def __init__(self, data):
        self.df = data

    def show_shape(self):
        print(f"\n🧱 Dataset Shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns\n")

    def show_head(self):
        print("🔍 First 5 Rows:")
        print(self.df.head(), "\n")

    def data_types(self):
        print("🔠 Data Types:")
        print(self.df.dtypes, "\n")

    def missing_values(self):
        print("🧼 Missing Values:")
        missing = self.df.isnull().sum()
        print(missing[missing > 0] if missing.sum() > 0 else "No missing values found.\n")

    def describe_data(self):
        print("📊 Summary Statistics (Numerical Features):")
        print(self.df.describe(), "\n")
    def unique_values(self):
        print("🔢 Unique Value Counts (Categorical Features):")
        cat_cols = self.df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            print(f"\n🧾 {col}:")
            print(self.df[col].value_counts())

    def churn_distribution(self):
        print("\n📉 Churn Distribution (Exited column):")
        print(self.df['Exited'].value_counts(normalize=True).map("{:.2%}".format))

    def correlation_matrix(self):
        print("\n📈 Correlation with Churn:")
        correlations = self.df.corr(numeric_only=True)['Exited'].sort_values(ascending=False)
        print(correlations)

    def run_all(self):
        self.show_shape()
        self.show_head()
        self.data_types()
        self.missing_values()
        self.describe_data()
        self.unique_values()
        self.churn_distribution()
        self.correlation_matrix()





# df = pd.read_csv(r"path of the data")

# analyzer = CustomerChurnAnalyzer(df)
# analyzer.run_all()
