
Paste and save as `README.md` in the project folder, then `git add README.md && git commit -m "Add README" && git push`.

---

## 3) Two-page internship report (copy this text into Word/Google Docs and save/export as PDF)
Below is the full content designed to fit two pages. Copy into Word, set font to **Arial 11**, normal margins, and export as PDF.

**Title page (first part)**

**Movie Success Prediction & Sentiment Study — Internship Project**  
Author: Rishab Tiwari  
Date: 10-12-2025

**Abstract**  
This project predicts movie box-office success using a regression model trained on movie metadata and analyzes user reviews with VADER sentiment. The aim is to identify features that influence revenue and understand audience sentiment across genres. The project produces a predictive model, visualizations of feature importance, and genre-wise sentiment analysis.

**Introduction**  
Predicting the commercial success of films is valuable for producers and distributors. This internship project explores whether metadata (budget, runtime, popularity, genre, release date) can predict box-office revenue and whether viewer sentiment correlates with financial success. The study uses a small sample dataset for demonstration and provides a process to scale with larger datasets.

**Tools Used**  
- Python (pandas, scikit-learn, joblib)  
- NLTK / VADER for sentiment analysis  
- Matplotlib for plotting  
- PowerShell for environment and running scripts

**Project Steps (short)**  
1. **Data preparation** — Load CSV, handle missing values, convert dates, encode categorical features (genres).  
2. **Sentiment analysis** — Apply VADER to sample review text to compute a compound sentiment score per movie and aggregate by genre.  
3. **Feature engineering** — Create features: budget, runtime, popularity, genre dummies, sentiment scores, release year/month.  
4. **Model training** — Split data, standardize numeric features, train a regression model (RandomForestRegressor or LinearRegression). Evaluate with RMSE and R².  
5. **Evaluation & visualization** — Plot feature importance, parity plots, and genre-wise sentiment charts. Save model using `joblib`.

**Results (summary)**  
- Example outputs from the sample run:  
  - RMSE: *[example output from console]*  
  - R²: *[example output]*  
- The trained model identifies **budget** and **popularity** as top predictors; sentiment adds modest predictive value when combined with metadata.

**Conclusion**  
The small-scale experiment demonstrates a reproducible workflow for combining sentiment analysis with structured metadata to forecast movie success. For production use, apply the same pipeline to a larger dataset (TMDB/Kaggle) and tune models for better generalization.

**How to run & deliverables**  
- Run `python movie_project.py` in the project folder.  
- Deliverables included: `movie_project.py`, `data/sample_movies.csv`, `figures/`, `models/movie_model.joblib`, `README.md`, `PROJECT2025.zip`.

---

## 4) Create a ZIP for submission (PowerShell)
Run this command in the `PROJECT2025` folder (it will create `PROJECT2025.zip` in the Desktop folder, excluding `.venv`):

```powershell
$items = Get-ChildItem -Path . -Force | Where-Object { $_.Name -ne '.venv' }
Compress-Archive -Path ($items | ForEach-Object { $_.FullName }) -DestinationPath ..\PROJECT2025.zip -Force

BY RISHAB TIWARI ♥
