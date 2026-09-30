
# **Sports Analytics Platform (NFL)**  
A full‑stack NFL analytics project that loads real game data, builds useful features, trains a machine learning model, and serves predictions through a FastAPI backend.

---

## **Overview**
This project predicts NFL game outcomes using real data and a simple machine learning pipeline. It includes:

- Data loading  
- Feature engineering  
- Model training  
- API endpoint for predictions  

Built as part of my Computer Science program to demonstrate ML and backend development skills.

---

## **Machine Learning**
The model uses **supervised machine learning**, specifically **Logistic Regression**, to predict whether the home team will win.

This model is fast, easy to train, and works well with engineered sports features.

---

## **Features Used**
The model learns from several effective features:

- Score differential  
- Home‑field indicator  
- Team win percentage  
- Rolling 3‑game point differential  

These features capture team strength, momentum, and basic game context.

---

## **Tech Stack**
**ML & Data:** Python, scikit‑learn, pandas, nfl_data_py  
**Backend:** FastAPI, Uvicorn  
**Tools:** VS Code, GitHub 

---

## **Project Structure**
```
sports-analytics-project/
│
├── analytics/
│   ├── train.py
│   ├── model.py
│   ├── features.py
│   ├── nfl_data_loader.py
│   └── nfl_model.pkl
│
├── backend/
│   └── main.py
│
└── README.md
```

---

## **How It Works**

### **1. Load Data**  
Pull NFL schedules and scores using `nfl_data_py`.

### **2. Build Features**  
Add win percentages, rolling averages, score differences, and home‑field flags.

### **3. Train Model**  
Run:

```
py -3.11 analytics/train.py
```

This creates `nfl_model.pkl`.

### **4. Make Predictions**  
Start the API:

```
uvicorn backend.main:app --reload
```

Call:

```
/nfl/predict?team1=Packers&team2=Bears
```

---

## **Example Response**
```json
{
  "team1": "Packers",
  "team2": "Bears",
  "probability": 0.6421
}
```

---

## **Future Improvements**
- Include Vegas spread    
- Build a React dashboard  
- Add MLB support  

---

## **Current Progress**
I’ve built the full machine‑learning pipeline for my NFL analytics project. The system loads real NFL data, engineers features via pandas, and trains a logistic regression model to predict home‑team win probabilities. I also set up a FastAPI backend with a endpoint that uses the trained model to generate results based on team inputs. At this point, the training pipeline and prediction engine are functional, and the next step is connecting everything to a frontend interface and refining my model further. 



[Watch Milestone 1 on YouTube](https://youtu.be/Wqn1CApZlu8)


## **Author**
**Jack D**  
Computer Science Student — University of Wisconsin–River Falls  
