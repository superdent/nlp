"""
Naive Bayes Training Script für Produktrezensionen-Klassifizierung
"""

import json
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import pandas as pd

# Pfade
DATA_DIR = Path("data/splits")
TRAIN_FILE = DATA_DIR / "train_0_50000_80_0_20.jsonl"
TEST_FILE = DATA_DIR / "test_0_50000_80_0_20.jsonl"
MODEL_DIR = Path("results/models")
METRICS_DIR = Path("results/metrics")

# Ordner erstellen
MODEL_DIR.mkdir(parents=True, exist_ok=True)
METRICS_DIR.mkdir(parents=True, exist_ok=True)


def load_data(filepath):
    """Lädt JSONL-Datei und extrahiert title, text, rating"""
    texts = []
    ratings = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            # Kombiniere title und text
            combined_text = f"{data['title']} {data['text']}"
            texts.append(combined_text)
            ratings.append(int(data['rating']))
    
    return texts, ratings


def preprocess_texts(texts):
    """TF-IDF Vektorisierung"""
    vectorizer = TfidfVectorizer(
        max_features=5000,
        min_df=2,
        max_df=0.95,
        lowercase=True,
        stop_words='english'
    )
    X = vectorizer.fit_transform(texts)
    return X, vectorizer


def train_model(X_train, y_train):
    """Trainiere Naive Bayes Modell"""
    model = MultinomialNB(alpha=1.0)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, class_names):
    """Evaluiere Modell"""
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    print(f"\n{'='*60}")
    print(f"EVALUIERUNG")
    print(f"{'='*60}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"\nConfusion Matrix:")
    print(conf_matrix)
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))
    
    return accuracy, conf_matrix, y_pred


def save_results(accuracy, conf_matrix, y_pred, y_test, class_names):
    """Speichere Metriken"""
    results = {
        'accuracy': accuracy,
        'confusion_matrix': conf_matrix.tolist(),
        'num_test_samples': len(y_test),
        'classes': class_names
    }
    
    with open(METRICS_DIR / "naive_bayes_metrics.json", 'w') as f:
        json.dump(results, f, indent=2)
    
    # CSV für Vergleiche
    metrics_df = pd.DataFrame({
        'Model': ['Naive Bayes'],
        'Accuracy': [accuracy],
        'Test_Samples': [len(y_test)]
    })
    metrics_df.to_csv(METRICS_DIR / "naive_bayes_results.csv", index=False)
    print(f"\nMetriken gespeichert in {METRICS_DIR}")


def main():
    print("Loading training data...")
    X_train_texts, y_train = load_data(TRAIN_FILE)
    print(f"Trainings-Samples: {len(X_train_texts)}")
    
    print("Loading test data...")
    X_test_texts, y_test = load_data(TEST_FILE)
    print(f"Test-Samples: {len(X_test_texts)}")
    
    print("\nVektorisierung (TF-IDF)...")
    X_train, vectorizer = preprocess_texts(X_train_texts)
    X_test = vectorizer.transform(X_test_texts)
    print(f"Feature-Dimension: {X_train.shape[1]}")
    
    print("\nModell-Training...")
    model = train_model(X_train, y_train)
    
    # Klassen-Namen
    class_names = ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars']
    
    # Evaluierung
    accuracy, conf_matrix, y_pred = evaluate_model(model, X_test, y_test, class_names)
    
    # Speichern
    save_results(accuracy, conf_matrix, y_pred, y_test, class_names)
    
    # Modell speichern
    with open(MODEL_DIR / "naive_bayes_model.pkl", 'wb') as f:
        pickle.dump(model, f)
    with open(MODEL_DIR / "vectorizer.pkl", 'wb') as f:
        pickle.dump(vectorizer, f)
    
    print(f"\nModell gespeichert in {MODEL_DIR}")


if __name__ == "__main__":
    main()
