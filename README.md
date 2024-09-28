# Email Spam Classifier
## Overview
The Email Spam Classifier is a natural language processing (NLP) project designed to classify emails as either spam or not spam (ham). It leverages various machine learning algorithms and techniques to achieve accurate classification based on the content of the email.

## Features
Binary Classification: Classifies emails into two categories: spam (1) or not spam (0).
Multiple Models: Utilizes Logistic Regression, Naive Bayes, Random Forest, and LSTM models to evaluate and compare performance.
Text Preprocessing: Implements comprehensive preprocessing steps including:
Removal of special characters and non-alphabetic characters.
Expansion of contractions for better tokenization.
Tokenization of text into words.
Lowercasing of words and removal of stopwords.
Lemmatization to reduce words to their base form.

## Importance of the Project
Email spam remains a significant issue in digital communication, impacting individuals, businesses, and organizations worldwide. The Email Spam Classifier addresses this problem by providing an automated solution to identify and filter out unwanted spam emails from legitimate ones. Key reasons why this project is important include:
Effective Email Management: Helps users efficiently manage their email inbox by automatically separating spam emails, reducing the time spent on manual filtering.

Enhanced Productivity: Ensures that users focus on relevant emails, improving productivity and workflow efficiency.

Protecting Against Cyber Threats: Identifies potentially harmful content such as phishing attempts, malware distribution, and fraudulent schemes, thereby enhancing cybersecurity measures.

Improved User Experience: Enhances user experience by providing a cleaner and safer email environment, ensuring that important communications are not missed or overlooked.

Educational and Research Purposes: Supports research in NLP, machine learning, and cybersecurity, contributing to advancements in technology and knowledge.

## Models comapared
Logistic Regression: Supervised learning model for binary classification.
Multinomial Naive Bayes: Probability-based classifier suitable for text classification tasks.
Random Forest: Ensemble learning method that builds multiple decision trees.
Long Short-Term Memory (LSTM): Deep learning model designed to handle sequence data, particularly useful for NLP tasks.

## Deployment
The project includes a Streamlit web application for deploying the trained models. Users can input email text and receive instant predictions regarding its classification as spam or not spam.
The application allows users to:
Input email text for classification.
View the predicted classification (spam or not spam) 
The web application is accessible via Streamlit Share at the following URL:  https://email-spam-classifier-osoz.onrender.com

## Acknowledgments
NLTK: For providing powerful tools for text preprocessing.
Scikit-learn: For machine learning algorithms and tools.
Streamlit: For easy deployment of the web application.
Special thanks to all contributors and the open-source community.
