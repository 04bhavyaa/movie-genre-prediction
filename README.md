## Movie Genre Prediction

This project aims to predict the genre of a movie based on its plot summary. Leveraging Natural Language Processing (NLP) and machine learning techniques, the system processes textual data and applies various models to achieve accurate predictions.
Hugging Space Link: https://huggingface.co/spaces/04bhavyaa/movie-genre-classificationn

### Directory Structure:

```
Directory structure:
└── 04bhavyaa-movie-genre-prediction/
    ├── app.py
    ├── artifacts.dvc
    ├── data/
    │   ├── train_data.txt
    │   ├── test_data_solution.txt
    │   ├── description.txt
    │   └── test_data.txt
    ├── requirements.txt
    ├── genre-classification.ipynb
    └── README.md
```

### Tech Stack:

- Libraries: Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, NLTK
- Models: Logistic Regression, Linear SVC, Random Forest, Naive Bayes
- Best Performing Model: Ensemble of Linear SVC and Logistic Regression with an accuracy of 58.88% on the validation set.

### Key Takeaways:

- Ensemble models outperformed individual models due to combined decision-making.
- Fine-tuning hyperparameters significantly improved accuracy for individual models.
- Preprocessing steps like lemmatization and scaling were essential for handling text data.

### App Gallery:
![Screenshot 2024-12-22 162608](https://github.com/user-attachments/assets/51be92ba-666c-428c-9add-b2ea35805738)

title: Movie Genre Classification
emoji: 🌖
colorFrom: purple
colorTo: yellow
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py
pinned: false

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

