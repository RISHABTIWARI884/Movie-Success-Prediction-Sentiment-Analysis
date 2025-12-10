import os
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# paths
ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_FILE = os.path.join(ROOT, "data", "sample_movies.csv")
FIG_DIR = os.path.join(ROOT, "figures")
MODEL_DIR = os.path.join(ROOT, "models")

os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# Load sample dataset
movies = pd.read_csv(DATA_FILE)

# Sentiment analysis
analyzer = SentimentIntensityAnalyzer()
movies["sentiment"] = movies["overview"].apply(lambda txt: analyzer.polarity_scores(txt)["compound"])

# Plot: Genre-wise sentiment
plt.figure(figsize=(10, 4))
movies.groupby("genre")["sentiment"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Sentiment by Genre")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "genre_sentiment.png"))
plt.close()

# Predicting revenue
X = movies[["budget", "vote_average", "vote_count", "sentiment"]]
y = movies["revenue"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=120, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
rmse = mean_squared_error(y_test, pred)**0.5
r2 = r2_score(y_test, pred)

print("RMSE:", rmse)
print("R2 Score:", r2)

joblib.dump(model, os.path.join(MODEL_DIR, "movie_model.joblib"))

# Feature importance plot
plt.figure(figsize=(6,4))
plt.bar(X.columns, model.feature_importances_)
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "feature_importance.png"))
plt.close()

print("Project completed successfully. Check figures/ and models/ folders.")
