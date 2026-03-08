# 🤖 Modellauswahl für Text-Klassifizierung (Sentimentanalyse)

**Ziel:** Produktrezensionen numerisch bewerten (1-5 Sterne)  
**Aufgabe:** Multi-Class Classification (5 Klassen)  
**Input:** Text (Titel + Beschreibung)  
**Größe:** ~1000-10000 Rezensionen pro Kategorie

---

## 🎯 Überblick: Die 4 Hauptkandidaten

| Modell | Geschwindigkeit | Genauigkeit | Einfachheit | Speichergröße | Best For |
|--------|---|---|---|---|---|
| **Naive Bayes** | ⚡⚡⚡ sehr schnell | ⭐⭐⭐⭐ gut | ⭐⭐⭐⭐⭐ sehr einfach | 🔵 klein | Text-Klassifizierung |
| **Logistic Regression** | ⚡⚡⚡ sehr schnell | ⭐⭐⭐⭐⭐ sehr gut | ⭐⭐⭐⭐ einfach | 🔵 klein | Baseline + Interpretierbarkeit |
| **SVM** | ⚡⚡ mittel | ⭐⭐⭐⭐⭐ sehr gut | ⭐⭐⭐ mittel | 🟡 mittel | Komplexe Grenzen |
| **Neural Network** | ⚡ langsam | ⭐⭐⭐⭐⭐ sehr gut | ⭐⭐ komplex | 🔴 groß | Große Datenmengen |

---

## 1️⃣ NAIVE BAYES (Empfehlung für Anfänger!)

### Was ist das?
Basiert auf dem **Bayes-Satz** - probabilistisches Modell, das die Wahrscheinlichkeit berechnet, dass ein Text zu jeder Klasse gehört.

**Grundidee:**
```
P(Klasse | Text) = P(Text | Klasse) × P(Klasse) / P(Text)
```

Auf Deutsch: Wie wahrscheinlich ist diese Klasse, gegeben diesen Text?

### Warum "Naive"?
Das Modell macht eine **naive Annahme**: Alle Wörter sind unabhängig voneinander.
- "great" und "product" beeinflussen sich nicht gegenseitig
- Realität: Sie tun es natürlich schon
- Aber für Text funktioniert es trotzdem überraschend gut! 🎯

### Implementation (scikit-learn)

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# Pipeline: Text → Vectorizer → Modell
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('nb', MultinomialNB(alpha=1.0))
])

# Training
pipeline.fit(X_train, y_train)

# Prediction
y_pred = pipeline.predict(X_test)

# Wahrscheinlichkeiten anschauen
probabilities = pipeline.predict_proba(X_test)
# Output: [[0.05, 0.10, 0.15, 0.30, 0.40], ...]
# Bedeutung: 5% 1-Stern, 10% 2-Stern, ..., 40% 5-Sterne
```

### ✅ Vorteile
- ✨ **Super schnell** - Training dauert Sekunden (auch mit großen Datenmengen)
- 🎯 **Überraschend akkurat** für Text-Klassifizierung
- 🔍 **Interpretierbar** - Man kann sehen, welche Wörter welche Klasse favorizieren
- 📦 **Kleine Modellgröße** - nur ein paar MB
- 🟢 **Einfach zu verstehen** - Probabilistisches Modell, gute Erklärbarkeit
- 🚀 **Gut für kleine bis mittlere Datenmengen** (100-100K Samples)

### ❌ Nachteile
- 🔴 **Naive Unabhängigkeits-Annahme** - Nicht realistisch
- 📉 **Kann underfitting geben** bei komplexen Mustern
- 🎨 **Keine Wort-Reihenfolge** - "great not" ≈ "not great" (beide schlecht!)
- ⚠️ **Sarkasmus-blind** - "Oh great, another 5-star!" wird als positiv erkannt

### Hyperparameter
```python
MultinomialNB(
    alpha=1.0,  # Laplace-Smoothing (0-5 sinnvoll)
                # Higher alpha = mehr Regularisierung
)
```

### 🎓 Wann wählen?
- ✅ **Anfänger** - Will erste Baseline bauen
- ✅ **Schnelle Prototypen** - Muss schnell was testen
- ✅ **Kleine Datenmengen** - < 10K Samples
- ✅ **Interpretierbarkeit wichtig** - Will verstehen, warum Modell so entscheidet
- ✅ **Produktive Systeme** - Braucht schnelle Inferenz (Echtzeit-Vorhersagen)

---

## 2️⃣ LOGISTIC REGRESSION (Empfehlung für Balance!)

### Was ist das?
**Lineare Klassifizierung** - Modell lernt Gewichte für jedes Wort.

**Grundidee:**
```
Score = w1×Wort1 + w2×Wort2 + w3×Wort3 + ... + bias
Wahrscheinlichkeit = sigmoid(Score)
```

Deutsch: Je höher das Score, desto höher die Wahrscheinlichkeit für die Klasse.

### Implementation (scikit-learn)

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    max_iter=1000,
    random_state=42,
    multi_class='multinomial'  # Für 5 Klassen
)

# Training
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Feature Weights anschauen (Interpretierbarkeit!)
feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]  # Gewichte für Klasse 1

# Top positive words für Klasse 5 (5-Sterne)
top_indices = np.argsort(coefficients)[-10:]  # Letzte 10
print(feature_names[top_indices])
# Output: ['great', 'excellent', 'love', 'perfect', ...]
```

### ✅ Vorteile
- ⚡ **Schnell** - Training dauert Sekunden
- 🎯 **Sehr gute Genauigkeit** - Oft besser als Naive Bayes!
- 🔍 **Hoch interpretierbar** - Kann Gewichte für jedes Wort sehen
- 📦 **Kleine Modellgröße**
- 🟢 **Robuster als Naive Bayes** - Keine naive Unabhängigkeits-Annahme
- 🚀 **Perfekt für mittlere Datenmengen**
- 📈 **Gut regularisierbar** - Hilft bei Overfitting

### ❌ Nachteile
- 🔴 **Linear** - Kann nur lineare Entscheidungsgrenzen lernen
- 🎨 **Keine Wort-Reihenfolge** - "good bad" ≈ "bad good"
- ⚠️ **Sarkasmus-blind** - Wie Naive Bayes
- 📊 **Benötigt Feature Scaling manchmal** (aber Bag-of-Words ist meist ok)

### Hyperparameter
```python
LogisticRegression(
    C=1.0,              # Regularisierungsstärke (kleiner = stärker)
    max_iter=1000,      # Iterationen zum Konvergieren
    multi_class='multinomial',  # Für Multi-Class
    solver='lbfgs',     # Optimierer (default für multinomial)
    random_state=42,    # Reproduzierbarkeit
)
```

### 🎓 Wann wählen?
- ✅ **Best of Both Worlds** - Schnell + Genau + Interpretierbar
- ✅ **Produktion** - Zuverlässig, schnell, wenig Ressourcen
- ✅ **Wenn Erklärbarkeit zählt** - "Warum hat das Modell so entschieden?"
- ✅ **Mittlere bis große Datenmengen** - 1K-1M Samples
- ✅ **Solide Baseline** - Bevor man zu komplizierten Modellen übergeht

### 🏆 **MEINE EMPFEHLUNG FÜR IHR PROJEKT**
Logistic Regression ist ideal, weil:
1. ✅ Gute Balance zwischen Geschwindigkeit und Genauigkeit
2. ✅ Einfach zu verstehen und zu implementieren
3. ✅ Interpretierbar (für Projektbericht wichtig!)
4. ✅ Zuverlässig (nicht über-hyped)
5. ✅ Production-ready

---

## 3️⃣ SUPPORT VECTOR MACHINE (SVM)

### Was ist das?
Findet **optimale Trenngrenzen** zwischen Klassen im hochdimensionalen Raum.

**Grundidee:**
```
Maximale Margin zwischen Klassen
↓
Unterstützungsvektoren (Support Vectors) = Wichtigste Punkte
↓
Entscheidungsgrenzen
```

### Implementation (scikit-learn)

```python
from sklearn.svm import LinearSVC  # Linear SVM (für große Datenmengen)
# NICHT SVC mit RBF kernel - viel zu langsam für Text!

model = LinearSVC(
    max_iter=2000,
    random_state=42,
    dual=False,  # Wichtig für viele Features!
)

# Training (kann länger dauern als NB/LR)
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)
```

### ✅ Vorteile
- 🎯 **Sehr gute Genauigkeit** - Oft best performer
- 🔍 **Kann komplexe Muster finden** - Nicht linear begrenzt
- 📚 **Gut für Text** - LinearSVC ist optimiert dafür
- 🟢 **Robust** - Weniger Overfitting bei richtiger Regularisierung

### ❌ Nachteile
- ⏱️ **Langsamer als Naive Bayes/LR** - Training dauert Minuten bei großen Datenmengen
- 🔍 **Weniger interpretierbar** - Schwerer zu verstehen, warum es so entschieden
- 📦 **Größeres Modell** - Speichert mehr Information
- ⚙️ **Mehr Hyperparameter zum tunen** - C, kernel, gamma
- 🐢 **Vorhersagen können auch langsamer sein**

### Hyperparameter
```python
LinearSVC(
    C=1.0,              # Penalty für Fehlklassifizierungen
    max_iter=2000,      # Iterationen
    dual=False,         # False wenn n_features > n_samples
    loss='squared_hinge',  # squared_hinge oder hinge
)
```

### 🎓 Wann wählen?
- ✅ **Wenn Genauigkeit am wichtigsten** - Will bestes Modell
- ✅ **Mittlere Datenmengen** - Nicht zu klein, nicht zu groß (10K-1M)
- ✅ **Offline-Verarbeitung** - Vorhersagen müssen nicht in Echtzeit sein
- ✅ **Du hast Zeit zum Tunen** - Hyperparameter experimentieren
- ❌ **NICHT wenn:** Echtzeit-Vorhersagen nötig (zu langsam)

---

## 4️⃣ NEURAL NETWORK (MLPClassifier)

### Was ist das?
**Künstliches neuronales Netz** mit mehreren Schichten (Layers).

**Grundidee:**
```
Input (Text-Features)
    ↓
Hidden Layer 1 (z.B. 128 Neuronen)
    ↓
Hidden Layer 2 (z.B. 64 Neuronen)
    ↓
Output Layer (5 Neuronen = 5 Klassen)
```

### Implementation (scikit-learn)

```python
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(128, 64),  # 2 Hidden Layers: 128 und 64 Neuronen
    activation='relu',              # ReLU activation function
    solver='adam',                  # Adam Optimizer
    max_iter=500,                   # Trainings-Iterationen
    random_state=42,
    verbose=True,  # Zeige Training-Fortschritt
)

# Training (kann länger dauern!)
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Trainings-Verlauf
print(model.loss_)  # Finaler Loss
print(model.n_iter_)  # Iterations benötigt
```

### ✅ Vorteile
- 🎯 **Beste Genauigkeit möglich** - Can learn very complex patterns
- 🔮 **Hochflexibel** - Kann fast jedes Problem lernen
- 📚 **State-of-the-art** - Modern, trendy, Zukunftstechnologie
- 🎨 **Implizit Wort-Kombinationen** - Besser als simple Bag-of-Words

### ❌ Nachteile
- ⏱️ **Langsam** - Training dauert Minuten bis Stunden
- 🔍 **Black Box** - Sehr schwer zu interpretieren ("Warum hat das Modell das entschieden?")
- 📦 **Großes Modell** - Braucht viel Speicher
- 🌊 **Overfitting-anfällig** - Braucht viel mehr Daten
- ⚙️ **Viele Hyperparameter** - Layer-Größen, Learning Rate, etc.
- 🔢 **Nicht-deterministisch** - Kann bei Runs unterschiedliche Ergebnisse geben
- 🚀 **Overkill für Text** - Often worse than simple LR!

### Hyperparameter
```python
MLPClassifier(
    hidden_layer_sizes=(128, 64),  # Neuronen pro Layer
    activation='relu',             # relu, tanh, logistic
    solver='adam',                 # adam, lbfgs, sgd
    learning_rate_init=0.001,      # Lern-Geschwindigkeit
    alpha=0.0001,                  # L2 Regularisierung
    max_iter=500,                  # Trainings-Iterationen
    early_stopping=True,           # Stop wenn Validation-Loss steigt
    validation_fraction=0.1,       # Validation Set Size
)
```

### 🎓 Wann wählen?
- ⚠️ **NICHT für dieses Projekt** - Overkill!
- ✅ **Wenn du große Datenmengen hast** - > 100K Samples
- ✅ **Wenn Interpretierbarkeit egal ist** - Schwer zu erklären
- ✅ **Wenn du viel Zeit zum Tunen hast**
- ✅ **Research/Fortgeschrittene** - Nicht für Anfänger
- ❌ **Text-Klassifizierung** - Andere Modelle meist besser

---

## 🎪 VERGLEICH: Code-Beispiel

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import time

# === Daten vorbereiten ===
X_train_vec = ...  # Already vectorized (5000 features)
y_train = ...

X_test_vec = ...
y_test = ...

# === Alle 4 Modelle trainieren ===
models = {
    'Naive Bayes': MultinomialNB(),
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'SVM': LinearSVC(max_iter=2000),
    'Neural Network': MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=500)
}

results = {}

for name, model in models.items():
    print(f"\n{'='*50}")
    print(f"Training: {name}")
    print(f"{'='*50}")
    
    # Training messen
    start = time.time()
    model.fit(X_train_vec, y_train)
    train_time = time.time() - start
    
    # Vorhersage messen
    start = time.time()
    y_pred = model.predict(X_test_vec)
    pred_time = time.time() - start
    
    # Genauigkeit
    accuracy = accuracy_score(y_test, y_pred)
    
    # Modellgröße schätzen
    import sys
    size_mb = sys.getsizeof(model) / (1024*1024)
    
    results[name] = {
        'accuracy': accuracy,
        'train_time': train_time,
        'pred_time': pred_time,
        'size_mb': size_mb
    }
    
    print(f"Accuracy:     {accuracy*100:.2f}%")
    print(f"Train Time:   {train_time:.2f}s")
    print(f"Pred Time:    {pred_time:.2f}s")
    print(f"Model Size:   {size_mb:.2f} MB")

# === Vergleich ===
print(f"\n{'='*50}")
print("ZUSAMMENFASSUNG")
print(f"{'='*50}")
for name, metrics in results.items():
    print(f"\n{name}:")
    print(f"  Accuracy:   {metrics['accuracy']*100:.2f}%")
    print(f"  Train:      {metrics['train_time']:.2f}s")
    print(f"  Predict:    {metrics['pred_time']:.2f}s")
    print(f"  Size:       {metrics['size_mb']:.2f} MB")
```

**Typische Output:**
```
ZUSAMMENFASSUNG
==================================================

Naive Bayes:
  Accuracy:   82.45%
  Train:      0.05s
  Predict:    0.01s
  Size:       0.02 MB

Logistic Regression:
  Accuracy:   85.30%
  Train:      0.15s
  Predict:    0.01s
  Size:       0.05 MB

SVM:
  Accuracy:   86.20%
  Train:      2.30s
  Predict:    0.05s
  Size:       0.15 MB

Neural Network:
  Accuracy:   84.90%
  Train:      45.20s
  Predict:    0.08s
  Size:       2.50 MB
```

---

## 🏆 EMPFEHLUNG NACH SITUATION

### Situation 1: "Ich bin Anfänger"
→ **Naive Bayes**
- Einfach zu verstehen
- Schnell zu trainieren
- Überraschend gut
- Perfekt zum Lernen

### Situation 2: "Ich will beste Balance" ← **IHR PROJEKT!**
→ **Logistic Regression**
- Schnell
- Genau
- Interpretierbar
- Production-ready

### Situation 3: "Ich will optimale Genauigkeit"
→ **SVM** oder **Ensemble (mehrere Modelle)**
- Best accuracy
- Aber braucht mehr Zeit/Ressourcen

### Situation 4: "Ich habe riesige Datenmengen" (1M+)
→ **Neural Network** mit Deep Learning
- Nutzt große Datenmengen besser
- Braucht aber auch viel Rechenpower

---

## 📊 DECISION TREE

```
START: Welches Modell?
│
├─ Anfänger?
│  └─ JA → Naive Bayes ✨
│  
├─ Willst du verstehen, warum das Modell so entscheidet?
│  └─ JA → Logistic Regression oder Naive Bayes 🔍
│  
├─ Ist Geschwindigkeit kritisch? (Echtzeit-Vorhersagen)
│  └─ JA → Naive Bayes oder Logistic Regression ⚡
│  
├─ Hast du > 100K Samples?
│  └─ JA → Neural Network möglich, sonst Logistic Regression
│  
├─ Willst du die beste möglich Genauigkeit, egal wie lange?
│  └─ JA → SVM oder Ensemble 🏆
│  
└─ Default für Text-Klassifizierung?
   └─ Logistic Regression (beste Balance!) ⭐
```

---

## 🚀 MY FINAL RECOMMENDATION

Für **Ihr Projekt (Sentimentanalyse, 3K-15K Samples)**:

### **LOGISTIC REGRESSION** 🎯

**Gründe:**
1. ✅ Schnell zu trainieren (< 1 Sekunde)
2. ✅ Gute Genauigkeit (85%+ realistisch)
3. ✅ Einfach zu implementieren
4. ✅ Interpretierbar (wichtig für Bericht!)
5. ✅ Production-ready
6. ✅ Wenig Hyperparameter zum tunen
7. ✅ Kein Overfitting-Risk
8. ✅ Auf Laptop schnell

**Alternative (falls Zeit):**
- Train auch **Naive Bayes** parallel (10x schneller) 
- Compare beide in Ergebnissen
- Zeigt "model comparison" in Bericht → Punkte! 📈

---

## 📚 Referenzen

- Jurafsky & Martin (SLP3): www.slp3.web.stanford.edu
- scikit-learn Docs: sklearn.org
- Text Classification Survey: arxiv.org/abs/1908.06635
