# Fraud Detection System

### Project Overview
This project detects fraudulent transactions using Machine Learning.
The model is trained using classification algorithms and deployed as Flask API.

### Problem Statement
Detect whether a financial transaction is fraudulent(1) or not(0).

### Project Pipeline
1. Data Cleaning and EDA
2. Handling Class Imbalance
3. Feature Preparation
4. Model Training 
5. Model Comparison
6. Model Selection
7. Model Serialization(.pkl)
8. API Developement using Flask
9. Deployment to Cloud

### Model comparison
Models evaluated:
- Logistic Regression
- Decision Tree
- Random Forest

#### Best Model: Random Forest Classifier
Reason:
 - Better recall on fraud cases
 - Handles imbalanced data
 - Strong overall performance
 
### Framework: Flask
### Deployment: Render

### Base URL:
https://fraud-api-project.onrender.com

### API Endpoint:
POST/Predict
