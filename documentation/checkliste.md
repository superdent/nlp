# PROJEKT-CHECKLISTE: Sentimentanalyse
**Kurs:** DLBAIPNLP01_D – Projekt: NLP
**Aktualisiert:** [Datum]

---

# PHASE 0: SETUP & ENTSCHEIDUNGEN

## 0.1 GitHub-Repository einrichten

- [x] Neues GitHub Repository erstellen
- [x] .gitignore konfigurieren
- [x] Repository lokal klonen

## 0.2 Verzeichnisstruktur aufsetzen

- [x] Ordner `documentation/` erstellen
  - [x] Datei `phase1_data.md` erstellen
  - [ ] Datei `phase2_preprocessing.md` erstellen
  - [ ] Datei `phase3_training.md` erstellen
  - [ ] Datei `phase4_results.md` erstellen
- [x] Ordner `src/` erstellen
  - [ ] Datei `raw_data_analysis.py` erstellen
  - [ ] Datei `preprocessing.py` erstellen
  - [ ] Dateien `model_training.py` erstellen
  - [ ] Datei `evaluation.py` erstellen
- [ ] Ordner `results/` erstellen
  - [ ] Unterordner `figures/` erstellen 
  - [ ] Unterordner `metrics/` erstellen
  - [ ] Unterordner `models/` erstellen
- [x] Ordner `data/` erstellen
  - [x] Unterordner `raw/` erstellen (für Original-Daten)
  - [ ] Unterordner `processed/` erstellen (für verarbeitete Daten)
- [ ] Root-Level `README.md` erstellen
  - [x] Projekt-Titel
  - [x] Kurzbeschreibung (2–3 Sätze)
  - [x] Link zur Dokumentation
  - [ ] Setup-Anleitung (Python, Dependencies)
  - [ ] Ordnerstruktur-Erklärung

## 0.3 Python-Umgebung konfigurieren

- [x] Virtual Environment erstellen
- [x] `requirements.txt` erstellen
- [x] Dependencies installieren

## 0.4 Grundsätzliche Entscheidungen treffen

### Produktkategorien auswählen

- McAuley Lab Website https://amazon-reviews-2023.github.io/
  - [x] Datensätze durchsuchen, Kategorien auswählen. 
  
### Modelltyp auswählen

- [ ] Modelloptionen recherchieren:
  - [x] Naive Bayes
  - [x] SVM
  - [x] Logistic Regression
  - [x] Neural Network prüfen
  - [x] kNN (kommt vermutlich nicht infrage)
- [ ] Begründung dokumentieren (mindestens 3 Sätze):
  - [ ] Warum dieses Modell für Text-Klassifizierung geeignet/nicht geeignet?
  - [ ] Welche Vorteile hat es für die Aufgabenstellung?
  - [ ] Gibt es Nachteile, die akzeptabel sind?
- [ ] Hyperparameter-Recherche:
  - [ ] Standard-Hyperparameter für Modell notieren
  - [ ] Welche könnten tuned werden?
  - [ ] Welche Bereiche sind sinnvoll?

### Datenmengen planen

- [ ] Zieldatenmenge pro Kategorie festlegen (Rezensionen/Kategorie)
- [ ] Gesamtzieldatenmenge (3 Kategorien × X)
- [ ] Train/Test Split Ratio wählen:
  - [ ] 80/20, 70/20/10, ...
- [ ] Stratified Split recherchieren

---

# PHASE 1: DATENSAMMLUNG & EXPLORATION

## 1.1 Rohdaten explorieren

### Dateiformat verstehen
- [X] Daten herunterladen
- [X] Format und Encoding prüfen (UTF-8)
- [ ] Relevante Felder identifizieren

### Python-Script zum Laden erstellen
- [ ] Funktion `load_json_reviews(filepath)` schreiben:
  - [ ] JSON-Datei zeilenweise laden
  - [ ] Fehlerhafte Zeilen abfangen
  - [ ] Nur relevante Felder extrahieren (Titel, Text, Rating)
  - [ ] Pandas DataFrame zurückgeben
- [ ] Funktion `load_csv_reviews(filepath)` schreiben (falls CSV)
- [ ] Kleine Test-Datei mit 10 Zeilen erstellen zum Testen
- [ ] Script testen: `python src/data_collection.py`
- [ ] Script debuggen, bis es läuft

### Kategorie-1 laden und inspizieren
- [ ] Script ausführen: `df1 = load_json_reviews('data/raw/category1/reviews.json')`
- [ ] Formen prüfen: `df1.shape` → sollte (N, 3) sein
- [ ] Spaltennamen prüfen
- [ ] Datentypen prüfen: `df1.dtypes`
- [ ] Null-Werte prüfen: `df1.isnull().sum()`
- [ ] Erste 5 Zeilen anschauen: `df1.head()`
- [ ] Statistik: `df1.describe()`
- [ ] Beispiele aus jedem Rating anschauen:
  - [ ] Eine 1-Stern-Rezension
  - [ ] Eine 2-Stern-Rezension
  - [ ] Eine 3-Stern-Rezension
  - [ ] Eine 4-Stern-Rezension
  - [ ] Eine 5-Stern-Rezension

### Kategorie-2 laden und inspizieren
- [ ] (Wiederholen wie Kategorie 1)

### Kategorie-3 laden und inspizieren
- [ ] (Wiederholen wie Kategorie 1)

## 1.3 Datenbereinigung (Raw Data Phase)

### Duplikate entfernen
- [ ] Duplicates prüfen (insgesamt): `df.duplicated().sum()`
- [ ] Auf Basis welcher Spalte? (Text? Text+Rating?)
- [ ] Duplikate entfernen: `df.drop_duplicates(subset=['text', 'rating'], keep='first')`
- [ ] Zeilen vor/nach notieren

### Fehlende Werte handhaben
- [ ] Null-Werte identifizieren: `df.isnull().sum()`
- [ ] Zeilen mit NULL in kritischen Feldern (Titel, Text, Rating) löschen
- [ ] Rows removed notieren

### Text-Qualität prüfen
- [ ] Textlängen anschauen:
  - [ ] Min-Länge (Zeichen)?
  - [ ] Max-Länge?
  - [ ] Durchschnitt?
  - [ ] Histogramm erstellen (matplotlib)
- [ ] Sehr kurze Texte (<5 Zeichen) entfernen?
- [ ] Sehr lange Texte (>5000 Zeichen) kürzen?
- [ ] Decision dokumentieren

### Ratings validieren
- [ ] Einzigartige Rating-Werte: `df['rating'].unique()`
- [ ] Sollte [1, 2, 3, 4, 5] sein
- [ ] Andere Werte vorhanden? Entfernen!
- [ ] Rating-Verteilung anschauen: `df['rating'].value_counts()`

## 1.4 Daten zusammenführen

- [ ] Alle 3 Dataframes laden
- [ ] Spalten standardisieren (alle gleich benannt):
  - [ ] Spalte für Kategorie-Name hinzufügen
  - [ ] Spalte 'category' mit Werten 'Category1', 'Category2', 'Category3'
- [ ] Dframes zusammenführen: `df_combined = pd.concat([df1, df2, df3], ignore_index=True)`
- [ ] Shape prüfen
- [ ] Kategorie-Verteilung prüfen: `df_combined['category'].value_counts()`

## 1.5 Explorative Datenanalyse (EDA)

### Grundstatistiken
- [ ] Gesamtanzahl Rezensionen: ________
- [ ] Anzahl pro Kategorie:
  - [ ] Kategorie 1: ________
  - [ ] Kategorie 2: ________
  - [ ] Kategorie 3: ________
- [ ] Rating-Verteilung (absolut):
  - [ ] 1-Sterne: ________
  - [ ] 2-Sterne: ________
  - [ ] 3-Sterne: ________
  - [ ] 4-Sterne: ________
  - [ ] 5-Sterne: ________
- [ ] Rating-Verteilung (Prozentual):
  - [ ] 1-Sterne: _____%
  - [ ] 2-Sterne: _____%
  - [ ] 3-Sterne: _____%
  - [ ] 4-Sterne: _____%
  - [ ] 5-Sterne: _____%

### Klassen-Balance prüfen
- [ ] Prozentsätze notieren
- [ ] Starkes Imbalance vorhanden? (z.B. 80% 5-Sterne?)
  - [ ] Stratifikation bei Train/Test Split ist wichtig!
  - [ ] Evtl. Oversampling/Undersampling erwägen (später)

### Textstatistiken berechnen
- [ ] Textlänge (Titel) - Statistiken:
  - [ ] Durchschnitt: ______ Zeichen
  - [ ] Median: ______ Zeichen
  - [ ] Min: ______ Zeichen
  - [ ] Max: ______ Zeichen
  - [ ] Std: ______ Zeichen
- [ ] Textlänge (Beschreibung) - Statistiken:
  - [ ] Durchschnitt: ______ Zeichen
  - [ ] Median: ______ Zeichen
  - [ ] Min: ______ Zeichen
  - [ ] Max: ______ Zeichen
  - [ ] Std: ______ Zeichen
- [ ] Wort-Anzahl (Titel):
  - [ ] Durchschnitt: ______ Wörter
- [ ] Wort-Anzahl (Beschreibung):
  - [ ] Durchschnitt: ______ Wörter

### Visualisierungen erstellen
- [ ] Rating-Verteilung Barplot: `results/figures/rating_distribution.png`
  - [ ] Absolute Häufigkeiten
  - [ ] Prozentual
- [ ] Rating-Verteilung pro Kategorie: `results/figures/rating_by_category.png`
  - [ ] 3 Subplots (eine pro Kategorie)
- [ ] Textlängen-Histogramm (Titel): `results/figures/text_length_title_hist.png`
- [ ] Textlängen-Histogramm (Beschreibung): `results/figures/text_length_description_hist.png`
- [ ] Alle Plots mit Labels, Title, Legend speichern

## 1.6 Phase-1 Dokumentation schreiben

- [ ] `documentation/phase1_data.md` öffnen
- [ ] Folgende Abschnitte schreiben:

### 1.6.1 Datenquelle
- [ ] McAuley Lab erwähnen
- [ ] Link: https://amazon-reviews-2023.github.io/
- [ ] Zitierweise/Lizenz notieren

### 1.6.2 Ausgewählte Kategorien
- [ ] Tabelle mit 3 Kategorien:
  | Kategorie | Rezensionszahl | Link | Begründung |
  |-----------|---|---|---|
  | ... | ... | ... | ... |

### 1.6.3 Datensammlungsprozess
- [ ] Wie wurden Daten heruntergeladen?
- [ ] Format (JSON/CSV)?
- [ ] Größe der heruntergeladenen Dateien?
- [ ] Fehler oder Probleme beim Download?

### 1.6.4 Rohdaten-Charakteristika
- [ ] Tabelle mit Statistiken:
  | Metrik | Kategorie 1 | Kategorie 2 | Kategorie 3 | Gesamt |
  |--------|---|---|---|---|
  | Rezensionen (vorher) | ... | ... | ... | ... |
  | Rezensionen (nachher) | ... | ... | ... | ... |
  | Duplikate entfernt | ... | ... | ... | ... |
  | NULL-Zeilen entfernt | ... | ... | ... | ... |

### 1.6.5 Datenbereinigung
- [ ] Dokumentieren, welche Zeilen entfernt wurden und warum
- [ ] Duplikate-Strategie
- [ ] NULL-Handling
- [ ] Text-Längen-Filter (falls angewandt)

### 1.6.6 EDA Ergebnisse
- [ ] Rating-Verteilung Tabelle
- [ ] Text-Längen-Statistiken (Tabelle)
- [ ] Beobachtungen zu Imbalance
- [ ] Besonderheiten pro Kategorie

### 1.6.7 Bilder einbinden
- [ ] Rating-Verteilung Plot
- [ ] Rating-by-Category Plot
- [ ] Text-Längen Histogramme

### 1.6.8 Erkenntnis & nächste Schritte
- [ ] Was wurde gelernt?
- [ ] Welche Herausforderungen gibt es (z.B. Imbalance)?
- [ ] Wie werden diese in Phase 2 adressiert?

## 1.7 Daten speichern für Phase 2

- [ ] Bereinigter kombinierter Datensatz speichern: `data/processed/combined_reviews.csv`
- [ ] Oder als Pickle: `data/processed/combined_reviews.pkl`
- [ ] Shape und Head nochmal verifikation
- [ ] Commit erstellen: `git add . && git commit -m "Phase 1: Data collection and EDA"`
- [ ] Pushen: `git push origin main`

---

# PHASE 2: VORVERARBEITUNG

## 2.1 Daten laden und Split vorbereiten

- [ ] Combined-Datensatz laden: `df = pd.read_csv('data/processed/combined_reviews.csv')`
- [ ] Shape prüfen
- [ ] Keine NULLs mehr?: `df.isnull().sum()`
- [ ] Titel + Beschreibung kombinieren?
  - [ ] Neue Spalte 'text' erstellen: `df['text'] = df['title'] + ' ' + df['description']`
  - [ ] Oder separat halten?
  - [ ] Decision dokumentieren
- [ ] Input-Spalte prüfen (was ist X?)
- [ ] Output-Spalte prüfen (Rating ist y?)

## 2.2 Train/Test Split durchführen

- [ ] Import `from sklearn.model_selection import train_test_split`
- [ ] Train/Test Split ausführen:
  ```python
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, 
      test_size=0.2,  # oder 0.3
      random_state=42,  # für Reproduzierbarkeit
      stratify=y  # um Klassen-Balance zu erhalten
  )
  ```
- [ ] Random Seed dokumentieren (42)
- [ ] Stratifikation dokumentieren (ja, warum)
- [ ] Größen prüfen:
  - [ ] X_train.shape: ______ x ______
  - [ ] X_test.shape: ______ x ______
  - [ ] y_train.shape: ______
  - [ ] y_test.shape: ______
- [ ] Train-Set Verteilung prüfen: `y_train.value_counts()`
- [ ] Test-Set Verteilung prüfen: `y_test.value_counts()`
- [ ] Verteilungen ähnlich? (Stratifikation war erfolgreich?)

## 2.3 NLTK Setup

- [ ] NLTK Punkt-Tokenizer downloaden:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```
- [ ] Test: `from nltk.tokenize import word_tokenize`
- [ ] Test: `from nltk.corpus import stopwords`

## 2.4 Text-Vorverarbeitung Pipeline erstellen

### 2.4.1 Preprocessing-Funktion schreiben

- [ ] `src/preprocessing.py` öffnen
- [ ] Funktion `preprocess_text(text)` schreiben mit:
  - [ ] Lowercase konvertieren: `text.lower()`
  - [ ] Spezialzeichen entfernen (optional): `re.sub(r'[^a-zA-Z\s]', '', text)`
  - [ ] Tokenisierung: `word_tokenize(text)`
  - [ ] Stopwörter laden: `stopwords.words('english')`
  - [ ] Stopwörter entfernen: `[word for word in tokens if word not in stop_words]`
  - [ ] Lemmatisierung (optional):
    - [ ] WordNetLemmatizer importieren
    - [ ] `lemmatizer = WordNetLemmatizer()`
    - [ ] Jeden Token lemmatisieren
  - [ ] Tokens wieder zu String zusammensetzen: `' '.join(tokens)`
  - [ ] Verarbeiteten Text zurückgeben

- [ ] Funktion mit Beispielen testen:
  - [ ] Input: "This is a GREAT product! Really amazing!!!"
  - [ ] Erwartete Ausgabe: "great product really amazing"
  - [ ] Testen: `print(preprocess_text(...))` und vergleichen

### 2.4.2 Pipeline auf kompletten Datensatz anwenden

- [ ] Funktion `apply_preprocessing(dataframe, text_column)` schreiben:
  - [ ] Progress-Bar verwenden (tqdm)?
  - [ ] Für jede Zeile `preprocess_text()` anwenden
  - [ ] Neue Spalte `preprocessed_text` erstellen
  - [ ] Fehler handhaben (try/except)

- [ ] Pipeline auf Train-Set anwenden:
  - [ ] `X_train_processed = apply_preprocessing(X_train)`
  - [ ] Erste 5 Beispiele anschauen und verifyieren
  - [ ] Länge vor/nach vergleichen

- [ ] Pipeline auf Test-Set anwenden:
  - [ ] `X_test_processed = apply_preprocessing(X_test)`

## 2.5 Numerische Codierung (Vectorization)

### 2.5.1 Vectorizer wählen und trainieren

- [ ] **Option 1: Bag of Words (BoW)**
  - [ ] Import: `from sklearn.feature_extraction.text import CountVectorizer`
  - [ ] Vectorizer erstellen: `vectorizer = CountVectorizer(max_features=5000)`
  - [ ] Auf Train-Set fitten: `X_train_vec = vectorizer.fit_transform(X_train_processed)`
  - [ ] Vocabulary-Größe: ________
  - [ ] Sparsity-Level: ________

- [ ] **Option 2: TF-IDF**
  - [ ] Import: `from sklearn.feature_extraction.text import TfidfVectorizer`
  - [ ] Vectorizer erstellen: `vectorizer = TfidfVectorizer(max_features=5000)`
  - [ ] Auf Train-Set fitten: `X_train_vec = vectorizer.fit_transform(X_train_processed)`
  - [ ] Vocabulary-Größe: ________

- [ ] **Entscheidung dokumentieren:** Warum BoW oder TF-IDF?

### 2.5.2 Transform auf Test-Set

- [ ] Test-Set transformieren (mit gelerntem Vectorizer!):
  ```python
  X_test_vec = vectorizer.transform(X_test_processed)
  ```
- [ ] WICHTIG: `.fit_transform()` nur auf Train! `.transform()` auf Test!

### 2.5.3 Vektoren inspizieren

- [ ] Shape prüfen:
  - [ ] X_train_vec.shape: ______ x ______
  - [ ] X_test_vec.shape: ______ x ______
- [ ] Sparse-Matrix-Format?: (sollte sparse sein)
- [ ] Top Features anschauen:
  - [ ] `vectorizer.get_feature_names_out()[:20]`
  - [ ] Diese Features machen Sinn?

## 2.6 Data-Splits als CSV/Pickle speichern

- [ ] Processed Train-Text speichern: `data/processed/X_train_processed.pkl`
- [ ] Processed Test-Text speichern: `data/processed/X_test_processed.pkl`
- [ ] y_train speichern: `data/processed/y_train.pkl`
- [ ] y_test speichern: `data/processed/y_test.pkl`
- [ ] Vectorizer speichern (für Reuse): `data/processed/vectorizer.pkl`
  ```python
  import pickle
  with open('data/processed/vectorizer.pkl', 'wb') as f:
      pickle.dump(vectorizer, f)
  ```
- [ ] X_train_vec speichern: `data/processed/X_train_vec.pkl`
- [ ] X_test_vec speichern: `data/processed/X_test_vec.pkl`

## 2.7 Phase-2 Dokumentation

- [ ] `documentation/phase2_preprocessing.md` öffnen

### 2.7.1 Preprocessing-Schritte dokumentieren
- [ ] Subsection für jeden Schritt:
  - [ ] Lowercase + Spezialzeichen
  - [ ] Tokenisierung
  - [ ] Stopword-Removal
  - [ ] Lemmatisierung/Stemming
- [ ] Begründung für jeden Schritt
- [ ] Code-Links zu `src/preprocessing.py` (KEIN Code im Bericht!)

### 2.7.2 Train/Test Split dokumentieren
- [ ] Ratio: 80/20 oder 70/30?
- [ ] Stratified?: Ja/Nein
- [ ] Random Seed: 42
- [ ] Finale Größen:
  | Set | Größe |
  |-----|-------|
  | X_train | _____ |
  | X_test | _____ |
  | y_train | _____ |
  | y_test | _____ |

### 2.7.3 Vectorization dokumentieren
- [ ] Methode: BoW oder TF-IDF?
- [ ] max_features: _____ (z.B. 5000)
- [ ] Vocablary-Größe: _____
- [ ] Feature-Matrix-Größe:
  | | Dimension 1 | Dimension 2 |
  |---|---|---|
  | X_train_vec | _____ | _____ |
  | X_test_vec | _____ | _____ |

### 2.7.4 Beispiele einbinden
- [ ] Original-Text-Beispiel
- [ ] Nach Preprocessing
- [ ] Kurz erklären, welche Transformationen sichtbar sind

## 2.8 Commit Phase 2

- [ ] `git add .`
- [ ] `git commit -m "Phase 2: Data preprocessing and vectorization"`
- [ ] `git push origin main`

---

# PHASE 3: MODELLTRAINING

## 3.1 Modellsetup

### 3.1.1 Modell importieren und instanziieren

- [ ] **Für Naive Bayes:**
  ```python
  from sklearn.naive_bayes import MultinomialNB
  model = MultinomialNB(alpha=1.0)
  ```

- [ ] **Für SVM:**
  ```python
  from sklearn.svm import LinearSVC
  model = LinearSVC(max_iter=1000, random_state=42)
  ```

- [ ] **Für Logistic Regression:**
  ```python
  from sklearn.linear_model import LogisticRegression
  model = LogisticRegression(max_iter=1000, random_state=42)
  ```

- [ ] **Für Neural Network:**
  ```python
  from sklearn.neural_network import MLPClassifier
  model = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=500, random_state=42)
  ```

- [ ] Modell konfiguriert und notiert

### 3.1.2 Hyperparameter dokumentieren

- [ ] Alle Hyperparameter des Modells notieren:
  - [ ] Alpha/C/Learning-Rate: _____
  - [ ] Hidden-Layer-Größe (falls Neural Net): _____
  - [ ] Max-Iterations: _____
  - [ ] Random-Seed: 42
  - [ ] Andere: _____

- [ ] Begründung für Hyperparameter notieren:
  - [ ] Warum diese Alpha?
  - [ ] Warum diese Layer-Größe?
  - [ ] Standard-Werte verwendet?

## 3.2 Training durchführen

### 3.2.1 Modell trainieren

- [ ] X_train_vec und y_train laden
- [ ] Training starten:
  ```python
  model.fit(X_train_vec, y_train)
  ```
- [ ] Training dauert wie lange?: ______ Sekunden/Minuten
- [ ] Keine Errors?

### 3.2.2 Training-Zeit messen

- [ ] `import time`
- [ ] `start = time.time()`
- [ ] Training laufen lassen
- [ ] `duration = time.time() - start`
- [ ] Dauer notieren: ______ Sekunden

### 3.2.3 Trainings-Metriken

- [ ] Training-Accuracy berechnen:
  ```python
  train_pred = model.predict(X_train_vec)
  train_accuracy = accuracy_score(y_train, train_pred)
  ```
- [ ] Wert: ______ %
- [ ] Ist das realistisch (nicht 100%)?

## 3.3 Modell speichern

- [ ] Modell serialisieren:
  ```python
  import pickle
  with open('results/models/sentiment_model.pkl', 'wb') as f:
      pickle.dump(model, f)
  ```
- [ ] Dateigröße prüfen: ______ MB
- [ ] Reloading testen:
  ```python
  with open('results/models/sentiment_model.pkl', 'rb') as f:
      model_loaded = pickle.load(f)
  ```
- [ ] Laden erfolgreich?

## 3.4 Phase-3 Dokumentation

- [ ] `documentation/phase3_training.md` öffnen

### 3.4.1 Modellauswahl begründen
- [ ] Warum dieses Modell?
- [ ] Alternativen überlegt?
- [ ] Vor- und Nachteile?

### 3.4.2 Modellbeschreibung
- [ ] Theoretischer Hintergrund:
  - [ ] Wie funktioniert das Modell?
  - [ ] Mathematische Grundlagen (kurz)
- [ ] Hyperparameter-Tabelle:
  | Parameter | Wert | Grund |
  |-----------|------|-------|
  | ... | ... | ... |

### 3.4.3 Training-Prozess
- [ ] Trainings-Dauer: ______ Sekunden
- [ ] Training-Accuracy: ______ %
- [ ] Verlauf ohne Fehler?
- [ ] Besonderheiten beim Training?

### 3.4.4 Modell-Persistierung
- [ ] Wo gespeichert?: `results/models/sentiment_model.pkl`
- [ ] Dateigröße: ______ MB

## 3.5 Commit Phase 3

- [ ] `git add .`
- [ ] `git commit -m "Phase 3: Model training and serialization"`
- [ ] `git push origin main`

---

# PHASE 4: EVALUIERUNG & ERGEBNISSE

## 4.1 Predictions generieren

- [ ] Modell laden (oder falls noch im Memory)
- [ ] X_test_vec und y_test laden
- [ ] Predictions generieren:
  ```python
  y_pred = model.predict(X_test_vec)
  ```
- [ ] Shape prüfen: `y_pred.shape` sollte `y_test.shape` sein
- [ ] Vorhersage-Verteilung prüfen:
  ```python
  unique, counts = np.unique(y_pred, return_counts=True)
  ```

## 4.2 Grundmetriken berechnen

### 4.2.1 Accuracy

- [ ] Import: `from sklearn.metrics import accuracy_score`
- [ ] Berechnen:
  ```python
  accuracy = accuracy_score(y_test, y_pred)
  ```
- [ ] Wert: ______ % (0–100%)
- [ ] Notieren in Datei: `results/metrics/accuracy.txt`

### 4.2.2 Confusion Matrix

- [ ] Import: `from sklearn.metrics import confusion_matrix`
- [ ] Berechnen:
  ```python
  cm = confusion_matrix(y_test, y_pred)
  ```
- [ ] Shape: sollte (5, 5) sein (für 5 Klassen)
- [ ] Matrix ausdrucken und anschauen
- [ ] Speichern als CSV: `results/metrics/confusion_matrix.csv`
  ```python
  pd.DataFrame(cm, 
              index=[1,2,3,4,5], 
              columns=[1,2,3,4,5]).to_csv(...)
  ```

## 4.3 Erweiterte Metriken (optional aber empfohlen)

### 4.3.1 Per-Class Metrics

- [ ] Import: `from sklearn.metrics import precision_recall_fscore_support`
- [ ] Berechnen:
  ```python
  precision, recall, f1, support = precision_recall_fscore_support(
      y_test, y_pred, 
      average=None  # pro Klasse
  )
  ```
- [ ] Tabelle erstellen:
  | Klasse | Precision | Recall | F1-Score | Support |
  |--------|-----------|--------|----------|---------|
  | 1-Star | _____ | _____ | _____ | _____ |
  | 2-Star | _____ | _____ | _____ | _____ |
  | 3-Star | _____ | _____ | _____ | _____ |
  | 4-Star | _____ | _____ | _____ | _____ |
  | 5-Star | _____ | _____ | _____ | _____ |
- [ ] Speichern: `results/metrics/per_class_metrics.csv`

### 4.3.2 Macro / Micro Average

- [ ] Macro (ungewichtet):
  ```python
  macro_f1 = f1_score(y_test, y_pred, average='macro')
  ```
- [ ] Wert: _____ %

- [ ] Micro (gewichtet):
  ```python
  micro_f1 = f1_score(y_test, y_pred, average='weighted')
  ```
- [ ] Wert: _____ %

## 4.4 Visualisierungen erstellen

### 4.4.1 Confusion Matrix Heatmap

- [ ] Code:
  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns
  
  plt.figure(figsize=(8,6))
  sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
              xticklabels=[1,2,3,4,5],
              yticklabels=[1,2,3,4,5])
  plt.xlabel('Predicted')
  plt.ylabel('True')
  plt.title('Confusion Matrix - Sentiment Classification')
  plt.savefig('results/figures/confusion_matrix_heatmap.png', dpi=300, bbox_inches='tight')
  plt.close()
  ```
- [ ] Speichern: `results/figures/confusion_matrix_heatmap.png`
- [ ] Visualisierung überprüfen

### 4.4.2 Accuracy Bar Chart

- [ ] Code:
  ```python
  plt.figure(figsize=(8,4))
  categories = ['1-Star', '2-Star', '3-Star', '4-Star', '5-Star']
  f1_scores = [f1[0], f1[1], f1[2], f1[3], f1[4]]
  plt.bar(categories, f1_scores)
  plt.ylabel('F1-Score')
  plt.title('Per-Class F1-Scores')
  plt.ylim([0, 1])
  plt.savefig('results/figures/per_class_f1_scores.png', dpi=300, bbox_inches='tight')
  plt.close()
  ```
- [ ] Speichern: `results/figures/per_class_f1_scores.png`

### 4.4.3 Prediction Distribution

- [ ] Code:
  ```python
  plt.figure(figsize=(8,4))
  pred_counts = np.unique(y_pred, return_counts=True)
  plt.bar(pred_counts[0], pred_counts[1], label='Predicted')
  true_counts = np.unique(y_test, return_counts=True)
  plt.bar(true_counts[0], true_counts[1], label='True', alpha=0.5)
  plt.xlabel('Rating')
  plt.ylabel('Count')
  plt.title('Prediction vs True Distribution')
  plt.legend()
  plt.savefig('results/figures/prediction_distribution.png', dpi=300, bbox_inches='tight')
  plt.close()
  ```
- [ ] Speichern: `results/figures/prediction_distribution.png`

## 4.5 Fehleranalyse (optional)

### 4.5.1 Missclassified Samples finden

- [ ] Fehler-Indizes ermitteln:
  ```python
  errors = y_test != y_pred
  error_indices = np.where(errors)[0]
  ```
- [ ] Anzahl Fehler: ________
- [ ] Fehlerrate: _________ %

### 4.5.2 Fehler-Beispiele anschauen

- [ ] Zufällig 10 Fehler auswählen
- [ ] Für jeden Fehler notieren:
  - [ ] Originaler Text (kurz)
  - [ ] True Rating
  - [ ] Predicted Rating
  - [ ] Beispiel 1: True=5, Pred=4, Text="..."
  - [ ] Beispiel 2: ...
  - [ ] ... (10 Beispiele insgesamt)

### 4.5.3 Fehler-Muster erkennen

- [ ] Treten bestimmte Fehler häufiger auf?
  - [ ] (z.B. 5→4? 1→2?)
- [ ] Unterscheiden sich die falschen Sample systematisch?
- [ ] Sarkasmus oder Mehrdeutigkeit erkannt?

## 4.6 Optionale: Vergleiche durchführen

### 4.6.1 Accuracy pro Kategorie (optional)

- [ ] Für jede Produktkategorie:
  ```python
  cat1_mask = X_test['category'] == 'Category1'
  cat1_accuracy = accuracy_score(y_test[cat1_mask], y_pred[cat1_mask])
  ```
- [ ] Ergebnisse:
  | Kategorie | Accuracy |
  |-----------|----------|
  | Kat 1 | _____ % |
  | Kat 2 | _____ % |
  | Kat 3 | _____ % |

### 4.6.2 Verschiedene Modelle vergleichen (optional)

- [ ] Falls Zeit: Naiver Bayes vs. SVM vs. Logistic Regression trainieren
- [ ] Alle auf gleichem Test-Set evaluieren
- [ ] Vergleichstabelle erstellen:
  | Modell | Accuracy | F1-Macro | Training-Zeit |
  |--------|----------|----------|---------------|
  | NB | _____ % | _____ % | _____ s |
  | SVM | _____ % | _____ % | _____ s |
  | LR | _____ % | _____ % | _____ s |

## 4.7 Phase-4 Dokumentation

- [ ] `documentation/phase4_results.md` öffnen

### 4.7.1 Ergebnisse klar darstellen

**Numerische Ergebnisse:**
- [ ] Accuracy-Tabelle:
  | Metrik | Wert |
  |--------|------|
  | Test-Accuracy | _____ % |
  | Macro-F1 | _____ % |
  | Weighted-F1 | _____ % |

- [ ] Per-Class Metrics Tabelle (aus 4.3.1)
- [ ] Confusion Matrix (als Tabelle oder Heatmap-Beschreibung)

### 4.7.2 Visualisierungen einbinden

- [ ] Confusion Matrix Heatmap
- [ ] Per-Class F1-Scores Bar Chart
- [ ] Prediction Distribution Comparison

### 4.7.3 Ergebnisse analysieren & diskutieren

**Welche Klassen werden gut erkannt?**
- [ ] Welche Klassen haben hohe Precision/Recall?
- [ ] 5-Sterne werden gut erkannt? Warum?
- [ ] 1-Sterne? 3-Sterne?

**Wo treten häufig Fehler auf?**
- [ ] Welche Verwechslungen passieren? (5→4? 3→2?)
- [ ] Sind manche Übergänge häufiger als andere?

**Warum könnten diese Fehler auftreten?**
- [ ] 4→5 Verwechslung: Ähnliche Wörter?
- [ ] 3-Sterne schwierig: Neutral vs. Positive?
- [ ] Sarkasmus nicht erkannt?
- [ ] Zu kurze Texte?

**Vergleiche (falls durchgeführt):**
- [ ] Unterschiede zwischen Kategorien?
- [ ] Unterschiede zwischen Modellen?
- [ ] Warum ein Modell besser als anderes?

### 4.7.4 Limitationen nennen

- [ ] Datenlimitationen:
  - [ ] Imbalance in Klassen
  - [ ] Textlängen variabel
  - [ ] Sarkasmus/Mehrdeutigkeit schwer
- [ ] Modell-Limitationen:
  - [ ] Bag-of-Words: Wort-Reihenfolge ignoriert
  - [ ] Keine Kontext-Berücksichtigung
  - [ ] Keine Negation-Handling (z.B. "not good")
- [ ] Ressourcen-Limitationen:
  - [ ] Rechenzeit
  - [ ] Datenmenge

### 4.7.5 Mögliche Verbesserungen nennen

- [ ] Daten-Seite:
  - [ ] Mehr Daten sammeln
  - [ ] Imbalance durch Oversampling adressieren
  - [ ] Data Augmentation
- [ ] Modell-Seite:
  - [ ] Andere Modelle (Neural Networks, Transformers)
  - [ ] Hyperparameter-Tuning
  - [ ] Ensemble-Methoden
- [ ] Feature-Seite:
  - [ ] Word Embeddings (Word2Vec, GloVe)
  - [ ] N-Grams berücksichtigen
  - [ ] Sarkasmus-Erkennung

## 4.8 Alle Ergebnisse-Dateien speichern

- [ ] Metriken-CSV: `results/metrics/`
  - [ ] `accuracy.txt`
  - [ ] `confusion_matrix.csv`
  - [ ] `per_class_metrics.csv`
- [ ] Figures: `results/figures/`
  - [ ] `confusion_matrix_heatmap.png`
  - [ ] `per_class_f1_scores.png`
  - [ ] `prediction_distribution.png`
- [ ] Model: `results/models/`
  - [ ] `sentiment_model.pkl`

## 4.9 Commit Phase 4

- [ ] `git add .`
- [ ] `git commit -m "Phase 4: Model evaluation and results analysis"`
- [ ] `git push origin main`

---

# PHASE 5: PROJEKTBERICHT SCHREIBEN

## 5.1 Bericht-Vorbereitung

- [ ] Word-Datei öffnen oder `.docx` erstellen (mit python-docx oder manuell)
- [ ] Alle Dokumentations-Dateien (Phase 1–4) nochmal durchlesen
- [ ] Alle Grafiken und Tabellen zusammentragen
- [ ] Notizen für Schreiben vorbereiten

## 5.2 Titelblatt erstellen

- [ ] Titel der Arbeit: "Sentimentanalyse von Produktrezensionen"
- [ ] Art der Arbeit: "Projektbericht"
- [ ] Kursbezeichnung: "DLBAIPNLP01_D – Projekt: NLP"
- [ ] Studiengang: "[eintragen]"
- [ ] Datum: "[heutiges Datum]"
- [ ] Name der Verfasserin/des Verfassers: "[Name]"
- [ ] Matrikelnummer: "[Nummer]"
- [ ] Name Tutor/in: "[Name]"
- [ ] Alle Angaben zentriert und einheitlich formatiert

## 5.3 Verzeichnisse erstellen

### 5.3.1 Inhaltsverzeichnis
- [ ] Alle Kapitel mit Nummern (1., 1.1, 1.1.1, max 3 Ebenen)
- [ ] Seitenzahlen
- [ ] Automatisch generiert (Word: Referenzen → Inhaltsverzeichnis) oder manuell

### 5.3.2 Abbildungsverzeichnis
- [ ] Alle Bilder/Grafiken auflisten:
  - [ ] Confusion Matrix Heatmap
  - [ ] Per-Class F1-Scores
  - [ ] Prediction Distribution
  - [ ] Rating Distribution (aus Phase 1)
  - [ ] Rating by Category (aus Phase 1)
  - [ ] Andere Grafiken?
- [ ] Nummern und Seitenzahlen

### 5.3.3 Tabellenverzeichnis
- [ ] Alle Tabellen auflisten:
  - [ ] Kategorien-Übersicht (Phase 1)
  - [ ] Datenbereinigung-Statistiken
  - [ ] Rating-Verteilung
  - [ ] Train/Test Split Größen (Phase 2)
  - [ ] Vectorization-Details
  - [ ] Modell-Hyperparameter (Phase 3)
  - [ ] Confusions Matrix (Phase 4)
  - [ ] Per-Class Metrics (Phase 4)
  - [ ] Andere?
- [ ] Nummern und Seitenzahlen

### 5.3.4 Abkürzungsverzeichnis (falls nötig)
- [ ] Abkürzungen, die im Bericht verwendet werden:
  - [ ] NLP = Natural Language Processing
  - [ ] BoW = Bag of Words
  - [ ] TF-IDF = Term Frequency - Inverse Document Frequency
  - [ ] SVM = Support Vector Machine
  - [ ] ML = Machine Learning
  - [ ] EDA = Explorative Datenanalyse
  - [ ] Andere?

## 5.4 EINLEITUNG schreiben (1–1,5 Seiten = 10–15%)

### 5.4.1 Hintergrund und Problematik
- [ ] Satz 1: Warum ist Sentimentanalyse wichtig?
  - Beispiel: "Mit dem Wachstum des E-Commerce sind automatische Methoden zur Analyse von Kundenbewertungen..."
- [ ] Satz 2–3: Relevanz für Unternehmen und Kunden
- [ ] Satz 4–5: Herausforderung: Größe der Datenmengen, Vielfalt der Ausdrücke

### 5.4.2 Zielsetzung definieren
- [ ] Satz: "Ziel dieses Projekts ist es, ein automatisches Textklassifizierungssystem zu entwickeln, das..."
- [ ] Spezifisch: Numerische Bewertung 1–5
- [ ] Auf Basis von Titel + Beschreibung

### 5.4.3 Methodisches Vorgehen kurz skizzieren
- [ ] "Das Projekt wird in vier Phasen durchgeführt:"
- [ ] Kurze Zusammenfassung jeder Phase (1–2 Sätze):
  - [ ] Phase 1: Datensammlung und Analyse
  - [ ] Phase 2: Textvorverarbeitung
  - [ ] Phase 3: Modelltraining
  - [ ] Phase 4: Evaluierung
- [ ] Theoretische Basis erwähnen (z.B. Machine Learning für Textklassifizierung)

### 5.4.4 Aufbau des Berichts
- [ ] "Der Bericht ist wie folgt strukturiert: In Kapitel 2 wird... In Kapitel 3 wird... Im Fazit werden..."

## 5.5 HAUPTTEIL schreiben (5–8 Seiten = 70–80%)

### 5.5.1 Kapitel 2: Datensammlung und Analyse (1–1,5 Seiten)

**2.1 Datenquelle**
- [ ] McAuley Lab erwähnen
- [ ] Amazon Reviews 2023 Dataset
- [ ] URL: https://amazon-reviews-2023.github.io/
- [ ] Lizenz (falls relevant)

**2.2 Ausgewählte Kategorien**
- [ ] Tabelle mit 3 Kategorien:
  | # | Kategorie | Geschätzte Größe | Begründung |
  |---|-----------|---|---|
  | 1 | | | |
  | 2 | | | |
  | 3 | | | |
- [ ] Text: Kurz erklären, warum diese 3 (unterschiedlich, interessant, etc.)

**2.3 Datenbereinigung**
- [ ] Rohdatenumfang notieren (vor und nach)
- [ ] Welche Schritte: Duplikate, NULLs, etc.
- [ ] Wie viele Zeilen entfernt?

**2.4 Datencharakteristika**
- [ ] Tabelle mit Statistiken:
  | Metrik | Kategorie 1 | Kategorie 2 | Kategorie 3 | Gesamt |
  |--------|---|---|---|---|
  | Rezensionen | | | | |
  | Avg. Titel-Länge | | | | |
  | Avg. Text-Länge | | | | |
  | 1-Sterne % | | | | |
  | 2-Sterne % | | | | |
  | etc. | | | | |

**2.5 Explorative Analyse**
- [ ] Rating-Verteilung Graph (Rating Distribution Barplot)
- [ ] Rating-Verteilung pro Kategorie Graph (Rating by Category)
- [ ] Beobachtung zu Imbalance (z.B. "Es werden mehr 5-Stern-Rezensionen gegeben...")
- [ ] Textlängen-Statistiken

### 5.5.2 Kapitel 3: Vorverarbeitung (1–1,5 Seiten)

**3.1 Train/Test Split**
- [ ] Ratio: 80/20 oder 70/30 → Begründung
- [ ] Stratifikation verwendet → Warum? (um Klassen-Verteilung zu erhalten)
- [ ] Finale Größen:
  | | Größe |
  |---|---|
  | Training-Set | ____ |
  | Test-Set | ____ |

**3.2 Textvorverarbeitung**
- [ ] Beschreibe die Pipeline (KEINE Code-Snippets!):
  1. Lowercase: "Der Text wird zu Kleinbuchstaben konvertiert, um..."
  2. Spezialzeichen: "Sonderzeichen werden entfernt, da sie..."
  3. Tokenisierung: "Der Text wird in einzelne Wörter aufgeteilt..."
  4. Stopword-Removal: "Häufige englische Wörter wie 'the', 'a' werden entfernt, weil..."
  5. Lemmatisierung: "Wörter werden auf ihre Grundform reduziert (z.B. 'running' → 'run'), um..."
- [ ] Für jeden Schritt: Begründung geben

**3.3 Numerische Codierung (Vectorization)**
- [ ] Methode wählen (BoW oder TF-IDF) → Begründung
- [ ] "Bag of Words/TF-IDF erstellt eine Matrix, bei der..."
- [ ] max_features Wert notieren und begründen
- [ ] Finale Dimensionalität:
  | | Dimensionen |
  |---|---|
  | Training-Matrix | ____ × ____ |
  | Test-Matrix | ____ × ____ |

**3.4 Beispiel-Transformation zeigen**
- [ ] Original-Text-Beispiel: "This is a GREAT product! Really amazing!!!"
- [ ] Nach Preprocessing: "great product really amazing"
- [ ] Erklären, welche Transformationen sichtbar sind

### 5.5.3 Kapitel 4: Modellauswahl und Training (1–1,5 Seiten)

**4.1 Modell-Begründung**
- [ ] Gewähltes Modell: ________
- [ ] Begründung (2–3 Sätze):
  - [ ] Warum dieses Modell für Text-Klassifizierung?
  - [ ] Welche Vorteile hat es?
  - [ ] Gibt es Nachteile?
- [ ] Theoretischer Hintergrund kurz skizzieren (nicht tief, 2–3 Sätze):
  - [ ] Naive Bayes z.B.: "Das Modell basiert auf dem Bayes-Satz und geht von der Unabhängigkeit von Features aus, was für Text-Klassifizierung oft ausreichend ist."

**4.2 Hyperparameter**
- [ ] Tabelle:
  | Parameter | Wert | Begründung |
  |-----------|------|-----------|
  | alpha | | |
  | max_iter | | |
  | random_state | 42 | Reproduzierbarkeit |
  | Other | | |

**4.3 Training**
- [ ] Training-Dauer: ______ Sekunden
- [ ] Training-Accuracy: ______ %
- [ ] Kurz beschreiben, wie Training funktioniert (keine Code-Details!)

**4.4 Code-Verweis**
- [ ] "Der komplette Code für Datensammlung, Vorverarbeitung und Modelltraining ist im GitHub-Repository verfügbar: [LINK]"

### 5.5.4 Kapitel 5: Evaluierung und Ergebnisse (2–2,5 Seiten)

**5.1 Evaluierungs-Metriken**
- [ ] Accuracy definieren: "Accuracy ist der Anteil der korrekt klassifizierten Rezensionen..."
- [ ] Confusion Matrix erklären: "Die Confusion Matrix zeigt, welche Bewertungsklassen häufig miteinander verwechselt werden..."
- [ ] F1-Score erklären (optional aber empfohlen)

**5.2 Numerische Ergebnisse - Hauptmetriken**
- [ ] Tabelle:
  | Metrik | Wert |
  |--------|------|
  | Test-Accuracy | _____ % |
  | Macro-F1 Score | _____ % |
  | Weighted-F1 | _____ % |

**5.3 Per-Class Performance**
- [ ] Tabelle:
  | Bewertung | Precision | Recall | F1-Score | Support |
  |-----------|-----------|--------|----------|---------|
  | 1-Star | | | | |
  | 2-Star | | | | |
  | 3-Star | | | | |
  | 4-Star | | | | |
  | 5-Star | | | | |

**5.4 Confusion Matrix Darstellung**
- [ ] Graph einfügen: Confusion Matrix Heatmap
- [ ] Kurz beschreiben: "Die Konfusionsmatrix zeigt, dass..."
- [ ] Welche Verwechslungen treten auf? (z.B. 5→4, 1→2?)

**5.5 Weitere Visualisierungen**
- [ ] Per-Class F1-Scores Graph
- [ ] Prediction Distribution Graph
- [ ] Kurz kommentieren: "Die Klassifizierung funktioniert besonders gut bei..."

**5.6 Analyse und Diskussion der Ergebnisse**

**Welche Klassen werden gut erkannt?**
- [ ] Beispiel: "5-Sterne-Rezensionen werden sehr gut erkannt (F1=0.85), da..."
- [ ] Beispiel: "1-Sterne-Rezensionen werden gut erkannt (F1=0.78), da..."
- [ ] Welche sind schwierig? (wahrscheinlich 3-Sterne)

**Wo treten Fehler auf?**
- [ ] Confusion Matrix analysieren: "Die häufigste Verwechslung ist 5→4 (200 Fälle), was darauf hindeutet, dass..."
- [ ] Muster erkennen: "4→5 und 5→4 Verwechslungen sind symmetrisch, was für ähnliche Sprachmuster spricht"
- [ ] 3-Sterne Problem?: "3-Sterne-Bewertungen sind schwer, da sie neutral oder subtil positiv sein können"

**Warum könnten diese Fehler auftreten?**
- [ ] Ähnliche Wörter: "5-Sterne und 4-Sterne Rezensionen verwenden oft ähnliche positive Wörter"
- [ ] Textlänge: "Sehr kurze Rezensionen sind schwerer zu klassifizieren"
- [ ] Sarkasmus/Mehrdeutigkeit: "Sarkastische Aussagen können missinterpretiert werden"
- [ ] Bag-of-Words Limitation: "Das Modell berücksichtigt nicht die Wort-Reihenfolge"
- [ ] Negation: "Negationen wie 'not good' werden nicht korrekt erkannt"

**Vergleiche (falls durchgeführt):**
- [ ] Kategorien vergleichen (falls pro Kategorie evaluiert)
- [ ] Modelle vergleichen (falls mehrere Modelle getestet)

**5.7 Limitationen kritisch diskutieren**
- [ ] Datenlimitationen:
  - [ ] "Die Daten zeigen ein Imbalance mit überrepräsentierten 5-Stern-Rezensionen"
  - [ ] "Nur Englische Rezensionen (falls relevant)"
  - [ ] "Begrenzte Datenmenge pro Kategorie"
- [ ] Modell-Limitationen:
  - [ ] "Bag-of-Words ignoriert Wort-Reihenfolge und Kontext"
  - [ ] "Keine Berücksichtigung von Sarkasmus oder ironischen Aussagen"
  - [ ] "Keine explizite Negations-Behandlung"
- [ ] Methoden-Limitationen:
  - [ ] "Simple Tokenisierung erfasst keine Mehrwort-Ausdrücke"
  - [ ] "Lemmatisierung kann Bedeutung verändern"

### 5.5.5 Kapitel 6: Reflexion (1–1,5 Seiten)

**6.1 Vorgehen kritisch beleuchten**
- [ ] War die Modellauswahl sinnvoll?
  - [ ] "Das gewählte Modell [Model] war eine gute Wahl, weil..."
  - [ ] "Alternativen wie [Model X] hätten möglicherweise bessere Ergebnisse geliefert, aber..."
- [ ] Funktionierte die Vorverarbeitung?
  - [ ] "Die Textvorverarbeitung war effektiv und entfernte erfolgreich Rauschen"
  - [ ] "Die Lemmatisierung könnte zu aggressive sein, da..."
- [ ] Welche Herausforderungen gab es?
  - [ ] "Das Imbalance der Klassen war eine Herausforderung"
  - [ ] "Die Datensammlung war zeitaufwändig"

**6.2 Theoretische Verbindung**
- [ ] Verbinde Ergebnisse mit NLP-Theorie:
  - [ ] "Die Ergebnisse unterstützen die Theorie, dass Bag-of-Words für Sentiment-Klassifizierung ausreichend ist"
  - [ ] "Das Projekt zeigt praktisch, wie Machine Learning-Klassifizierer auf Text-Daten angewandt werden"
  - [ ] "Die Confusion-Matrix-Analyse zeigt typische Herausforderungen bei Multi-Class-Klassifizierung"

**6.3 Verbessungsmöglichkeiten**
- [ ] Daten:
  - [ ] "Mehr Daten sammeln würde Imbalance reduzieren"
  - [ ] "Data-Augmentation könnte synthetische Beispiele generieren"
- [ ] Modell:
  - [ ] "Neural Networks oder Transformer-Modelle könnten bessere Ergebnisse liefern"
  - [ ] "Ensemble-Methoden könnten Robustheit erhöhen"
- [ ] Features:
  - [ ] "Word Embeddings (Word2Vec, GloVe) könnten semantische Ähnlichkeit erfassen"
  - [ ] "N-Grams könnten Wort-Kombinationen berücksichtigen"
  - [ ] "Spezielle Features für Sarkasmus und Negation"

**6.4 Learnings für zukünftige Projekte**
- [ ] Was wurde gelernt?
- [ ] Welche Praktiken waren hilfreich?
- [ ] Was würde man nächstes Mal anders machen?

## 5.6 FAZIT & AUSBLICK schreiben (1–1,5 Seiten = 10–15%)

### 5.6.1 Kernerkenntnisse zusammenfassen
- [ ] Satz 1: "In diesem Projekt wurde ein Textklassifizierungssystem entwickelt, das Produktrezensionen automatisch auf einer Skala von 1 bis 5 Sternen bewertet."
- [ ] Satz 2: "Das System erreichte eine Test-Accuracy von _____%..."
- [ ] Satz 3: "Die Confusion Matrix zeigt, dass..."

### 5.6.2 Ergebnisse in Kontext setzen
- [ ] "Das Ergebnis demonstriert, dass Machine Learning für praktische NLP-Aufgaben einsetzbar ist"
- [ ] "Die automatische Sentimentanalyse könnte für Unternehmen Zeit und Kosten sparen"

### 5.6.3 Schlussfolgerungen aus Reflexion
- [ ] "Obwohl das Modell gute Ergebnisse erreichte, zeigten sich auch Limitationen..."
- [ ] "Diese Limitationen könnten durch fortgeschrittene Methoden adressiert werden"

### 5.6.4 Ausblick und Zukunftsarbeit
- [ ] "Für zukünftige Arbeiten könnten folgende Richtungen untersucht werden:"
  - [ ] Transformer-basierte Modelle (BERT, RoBERTa)
  - [ ] Multilingual-Klassifizierung
  - [ ] Aspekt-basierte Sentimentanalyse (welche Features mögen/mögen Kunden nicht?)
  - [ ] Real-Time Processing von neuen Rezensionen

### 5.6.5 Abschließender Gedanke
- [ ] "Die Sentimentanalyse ist ein wichtiges Werkzeug für moderne Unternehmen..."
- [ ] "Dieses Projekt hat gezeigt, dass mit grundlegenden Machine-Learning-Techniken bereits aussagekräftige Ergebnisse erreicht werden können."

## 5.7 LITERATURVERZEICHNIS erstellen

- [ ] Alle zitierten Quellen sammeln:
  - [ ] McAuley Lab (Amazon Reviews) - Publikation
  - [ ] Jurafsky & Martin (SLP3)
  - [ ] Scikit-learn Dokumentation (falls zitiert)
  - [ ] NLTK Dokumentation
  - [ ] Andere recherchierte Papers/Bücher

- [ ] Alphabetisch ordnen
- [ ] Einheitliches Format (gemäß IU-Vorgaben, z.B. Harvard oder APA):
  - Beispiel Harvard: "Author, A. A. (Year) 'Title', Journal, volume(issue), pp. pages. doi: ..."
  - Beispiel APA: "Author, A. A. (Year). Title of work. Publisher."

- [ ] Mindestens 5–10 Quellen notwendig?

## 5.8 ANHÄNGE (falls nötig)

- [ ] GitHub-Repository-Link (prominent!)
  - [ ] "Der vollständige Code ist unter folgendem Link verfügbar: [URL]"
- [ ] Zusätzliche Tabellen/Grafiken (falls zu lang für Haupttext)
- [ ] Konfigurationsdateien oder Hyperparameter-Experimente

## 5.9 Formale Anforderungen überprüfen

### 5.9.1 Umfang
- [ ] Textteil (ohne Titelblatt, Verzeichnisse, Anhänge): 7–10 Seiten
- [ ] Ungefähre Seitenzahl prüfen

### 5.9.2 Formatierung
- [ ] **Schrifttyp:** Arial 11pt (Text), 12pt (Überschriften)
- [ ] **Zeilenabstand:** 1,5
- [ ] **Seitenränder:** 2 cm überall (oben, unten, links, rechts)
- [ ] **Seitenzahlen:**
  - [ ] Titelblatt: keine Nummer
  - [ ] Verzeichnisse: römisch (I, II, III, IV, V...)
  - [ ] Textteil: arabisch (1, 2, 3, ... bis Ende)
- [ ] **Satz:** Blocksatz, Silbentrennung aktiviert
- [ ] **Hervorhebungen:** Nur *Kursiv*, KEINE Unterstreichungen
- [ ] **Nummerierung:**
  - [ ] Nur Kapitel nummerieren (1., 1.1, 1.1.1 max!)
  - [ ] Verzeichnisse NICHT nummerieren
  - [ ] Anhänge NICHT nummerieren

### 5.9.3 Sprachliche Anforderungen
- [ ] **3. Person verwenden:** "Der Verfasser hat...", "Es wurde...", NICHT "Ich habe..."
- [ ] **Sachlicher, wissenschaftlicher Stil**
- [ ] **Keine Umgangssprache** ("cool", "crazy", etc.)
- [ ] **Präzise und verständliche Sätze**
- [ ] **Fachbegriffe erläutert** beim ersten Auftreten

### 5.9.4 Abbildungen und Tabellen
- [ ] Jede Abbildung hat:
  - [ ] Nummer ("Abbildung 1", "Abbildung 2", etc.)
  - [ ] Aussagekräftigen Titel/Caption
  - [ ] Quelle/Verweis (z.B. "Quelle: Eigene Erstellung")
- [ ] Jede Tabelle hat:
  - [ ] Nummer ("Tabelle 1", "Tabelle 2", etc.)
  - [ ] Aussagekräftigen Titel
  - [ ] Im Text referenziert ("Wie in Tabelle 1 gezeigt...")
- [ ] Alle Abbildungen sind gut lesbar (Schrift groß genug?)
- [ ] Alle Tabellen sind aufgeräumt und konsistent formatiert

### 5.9.5 Zitierung
- [ ] Alle Informationen aus Quellen sind zitiert
- [ ] Einheitliches Zitationssystem (Harvard, APA, Chicago, etc.)
- [ ] Literaturverzeichnis vollständig
- [ ] Keine Plagiate! (eigene Worte verwenden)

### 5.9.6 Code-Handling
- [ ] ❌ KEIN Code-Snippet im Bericht!
- [ ] ✅ Nur Link zu GitHub-Repository erwähnen
- [ ] ✅ Algorithmische Ideen dürfen in Prosa beschrieben werden
- [ ] ✅ Verweise auf Code-Dateien sind ok (z.B. "siehe src/preprocessing.py")

## 5.10 Korrektur und Review

### 5.10.1 Selbst-Review (3x durchlesen!)

**Durchgang 1: Inhalt**
- [ ] Sind alle erforderlichen Abschnitte vorhanden?
- [ ] Ist die Logik schlüssig?
- [ ] Sind Übergänge zwischen Abschnitten sinnvoll?
- [ ] Fehlt etwas wichtiges?

**Durchgang 2: Sprachliche Qualität**
- [ ] Rechtschreibung prüfen (Word-Rechtschreibprüfung nutzen)
- [ ] Grammatik prüfen
- [ ] Sätze verständlich formuliert?
- [ ] Satzlängen variabel? (nicht nur kurz oder nur lang)
- [ ] Alliterationen oder Wiederholungen?

**Durchgang 3: Formatierung**
- [ ] Alle Formatierungsvorgaben eingehalten?
- [ ] Schriftarten, Größen konsistent?
- [ ] Seitenzahlen richtig?
- [ ] Verzeichnisse aktualisiert?
- [ ] Bilder und Tabellen korrekt nummeriert?

### 5.10.2 Peer-Review (optional)
- [ ] Freund/in oder Kommilitone/in prüfen lassen
- [ ] Feedback einholen (Verständlichkeit, Fehler, Logik)
- [ ] Feedback einarbeiten

### 5.10.3 Finale Prüfung vor Abgabe
- [ ] PDF-Export testen (Formatierung erhalten?)
- [ ] Alle Grafiken sichtbar in PDF?
- [ ] Alle Verzeichnisse korrekt?
- [ ] Keine leeren Seiten?
- [ ] Seitenzahl realistisch?

## 5.11 Bericht als Word-Datei speichern

- [ ] Dateiname: `Projektbericht_Sentimentanalyse_[Name]_[Datum].docx`
- [ ] Speicherort: `results/` oder Root
- [ ] Sicherung erstellen (CloudStorage oder lokale Kopie)

## 5.12 Commit Phase 5

- [ ] Projektbericht-Datei zu Git hinzufügen (auch große .docx ok):
  ```
  git add results/Projektbericht_*.docx
  git add documentation/
  ```
- [ ] Commit: `git commit -m "Phase 5: Final project report"`
- [ ] Push: `git push origin main`

---

# PHASE 6: FINAL SUBMISSION

## 6.1 Vor der Abgabe - Checkliste

### 6.1.1 Projekt-Verzeichnis prüfen
- [ ] GitHub-Repository aktuell (alle Dateien gepusht)?
- [ ] `README.md` aussagekräftig?
  - [ ] Projektbeschreibung
  - [ ] Ordnerstruktur erklärt
  - [ ] Wie man Code ausführt
  - [ ] Link zu Dokumentation
- [ ] `src/` Ordner:
  - [ ] `data_collection.py`
  - [ ] `preprocessing.py`
  - [ ] `model_training.py`
  - [ ] `evaluation.py`
  - [ ] `utils.py` (optional)
  - [ ] `__init__.py`
- [ ] `documentation/` Ordner:
  - [ ] `phase1_data.md`
  - [ ] `phase2_preprocessing.md`
  - [ ] `phase3_training.md`
  - [ ] `phase4_results.md`
- [ ] `results/` Ordner:
  - [ ] `figures/` mit Grafiken
  - [ ] `metrics/` mit CSV-Dateien
  - [ ] `models/` mit serialisiertem Modell
- [ ] `.gitignore` konfiguriert (große Dateien nicht gepusht?)

### 6.1.2 Projektbericht prüfen
- [ ] Dateiname korrekt? `Projektbericht_Sentimentanalyse_*.docx`
- [ ] Formatierung vollständig?
  - [ ] Schrifttyp/Größe
  - [ ] Seitenränder
  - [ ] Zeilenabstand
  - [ ] Nummerierung (Titelblatt, Verzeichnisse, Text)
- [ ] Inhalt vollständig?
  - [ ] Titelblatt mit allen Angaben
  - [ ] Verzeichnisse
  - [ ] 5 Kapitel (Einleitung, 4 Phasen) oder 6 (mit Fazit)
  - [ ] Literaturverzeichnis
  - [ ] Anhänge
- [ ] Sprachliche Qualität?
  - [ ] 3. Person
  - [ ] Keine Rechtschreibfehler
  - [ ] Wissenschaftlicher Stil
- [ ] Länge?
  - [ ] 7–10 Seiten Textteil (ungefähr?)
- [ ] Bilder und Tabellen?
  - [ ] Alle nummeriert und referenziert
  - [ ] Alle Quellen angegeben

### 6.1.3 GitHub-Link verfügbar?
- [ ] Repository-URL notieren: ____________________________
- [ ] Link im Anhang des Berichts erwähnen
- [ ] Link in myCampus-Notizen hinterlegen (optional)

## 6.2 myCampus-Upload

- [ ] myCampus-Portal öffnen
- [ ] Kurs "DLBAIPNLP01_D" suchen
- [ ] Aufgabe "Projektbericht" finden
- [ ] Projektbericht hochladen (.docx-Datei)
- [ ] Überprüfung: Upload erfolgreich?
- [ ] Dateigröße ok?

## 6.3 Eidesstattliche Erklärung

- [ ] Eidesstattliche Erklärung ausfüllen (Template von IU)
- [ ] Unterschrift leisten (digital oder handschriftlich)
- [ ] Eidesstattliche Erklärung in myCampus hochladen
  - [ ] WICHTIG: Dies ist Voraussetzung für Abgabe!
- [ ] Einreichungsbestätigung speichern

## 6.4 Nach der Abgabe

- [ ] Einreichungsbestätigung überprüfen
- [ ] Zeitstempel und Abgabedatum notieren
- [ ] GitHub-Repository nochmal aktualisieren (falls letzte Änderungen):
  - [ ] Final commit: `git commit -m "Final submission"`
  - [ ] Final push: `git push origin main`
- [ ] Backup des Projekts erstellen (externe Festplatte, Cloud)
- [ ] Abgabe-Screenshot machen (als Dokumentation)

---

# 🎯 SELBST-CHECK: BEWERTUNGSKRITERIEN

Die Universität bewertet nach 6 Kriterien mit Gewichtung. Selbst-Check:

## ✅ Qualität (25%)
- [ ] Ist die Reflexion tief und gründlich?
  - [ ] Fehler kritisch analysiert?
  - [ ] Theoretische Konzepte angewandt?
- [ ] Sind Erkenntnisse nachvollziehbar?
  - [ ] Logische Argumentation?
  - [ ] Evidenz basiert?
- Selbst-Rating: __/10

## ✅ Prozess (25%)
- [ ] Ist das Vorgehen schlüssig?
  - [ ] Ziele klar?
  - [ ] Schritte logisch aufgebaut?
- [ ] Sind die Methoden geeignet?
  - [ ] Modellauswahl begründet?
  - [ ] Preprocessing angemessen?
- [ ] Ist die Durchführung sauber?
  - [ ] Keine methodischen Fehler?
  - [ ] Best Practices eingehalten?
- Selbst-Rating: __/10

## ✅ Transfer (15%)
- [ ] Sind Verbindungen zu Theorie hergestellt?
  - [ ] NLP-Konzepte erwähnt?
  - [ ] Machine-Learning-Theorie angewandt?
- [ ] Sind Erkenntnisse allgemeingültig?
  - [ ] Nicht nur auf dieses Projekt begrenzt?
  - [ ] Lessons für andere Projekte?
- Selbst-Rating: __/10

## ✅ Kreativität (15%)
- [ ] Gibt es innovative Ansätze?
  - [ ] Über Anforderungen hinaus gegangen?
  - [ ] Optionale Erweiterungen gemacht?
- [ ] Sind Schlussfolgerungen original?
  - [ ] Nicht nur wiedergekaut?
  - [ ] Neue Perspektive?
- Selbst-Rating: __/10

## ✅ Dokumentation (10%)
- [ ] Ist der Bericht fehlerfrei?
  - [ ] Keine Rechtschreibfehler?
  - [ ] Grammatik korrekt?
- [ ] Ist die Struktur sinnvoll?
  - [ ] Kapitel logisch geordnet?
  - [ ] Übergänge flüssig?
- [ ] Sind formale Vorgaben erfüllt?
  - [ ] Formatierung korrekt?
  - [ ] Länge im Bereich?
- Selbst-Rating: __/10

## ✅ Ressourcen (10%)
- [ ] Effizienter Umgang mit Daten?
  - [ ] Datenmenge angemessen?
  - [ ] Keine unnötigen Dateien?
- [ ] Effizienter Umgang mit Tools?
  - [ ] Richtige Bibliotheken gewählt?
  - [ ] Nicht zu kompliziert?
- [ ] Zeitmanagement?
  - [ ] Realistischer Zeitaufwand?
  - [ ] Keine unnötigen Experimente?
- Selbst-Rating: __/10

---

## 📊 FINAL SCORE ESTIMATE
(Alle 6 Kriterien mit Gewichtung)

| Kriterium | Rating (/10) | Gewichtung | Punkte |
|-----------|---|---|---|
| Qualität | ___ | 25% | ___ |
| Prozess | ___ | 25% | ___ |
| Transfer | ___ | 15% | ___ |
| Kreativität | ___ | 15% | ___ |
| Dokumentation | ___ | 10% | ___ |
| Ressourcen | ___ | 10% | ___ |
| | | | **GESAMT = __%** |

---

**Viel Erfolg beim Projekt! 🚀**
