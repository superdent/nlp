# Klassifikationsmetriken

| Metrik | Formel | Zweck | Binär | Multiclass |
|--------|--------|-------|-------|------------|
| Accuracy | (TP + TN) / (TP + TN + FP + FN) | Wie oft lag ich insgesamt richtig? Irreführend bei schiefer Verteilung. | ja | ja |
| Precision | TP / (TP + FP) | Wie viele meiner positiven Vorhersagen sind korrekt? Bestraft FP. | ja | ja, pro Klasse berechnet |
| NPV | TN / (TN + FN) | Wie viele meiner negativen Vorhersagen sind korrekt? Bestraft FN. | ja | nein |
| Recall (Sensitivity) | TP / (TP + FN) | Wie gut erkenne ich Positive? Bestraft FN. | ja | ja, pro Klasse berechnet |
| Specificity | TN / (TN + FP) | Wie gut erkenne ich Negative? Bestraft FP. | ja | nein |
| F1-Score | 2 * Precision * Recall / (Precision + Recall) | Kompromiss aus Precision und Recall. | ja | ja, als Macro-F1 |