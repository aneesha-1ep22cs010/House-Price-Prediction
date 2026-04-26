import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load data
df = pd.read_csv('AmesHousing.csv')

# 2. Select our top features (based on your chart!)
# We use numeric columns only for this baseline
features = ['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Total Bsmt SF']
X = df[features]
y = df['SalePrice']

# 3. Handle any missing values in these specific columns
X = X.fillna(X.median())

# 4. Split data (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Make Predictions
predictions = model.predict(X_test)

# 7. Evaluate
print(f"R2 Score: {r2_score(y_test, predictions):.2f}")
print(f"Mean Absolute Error: ${mean_absolute_error(y_test, predictions):,.2f}")