# Training-Checkliste

| # | Modell | Datensätze | Parameter |
|---|--------|-----------|-----------|
| 1 | Naive Bayes | 300.000 | |
| 2 | Naive Bayes | 6.000.000 | |
| 3 | Naive Bayes | ALLE | |
| 4 | SVM (LinearSVC) | 300.000 | C=1.0 |
| 5 | SVM (LinearSVC) | 6.000.000 | C=1.0 |
| 6 | SVM (LinearSVC) | 6.000.000 | C=0.5 |
| 7 | SVM (LinearSVC) | 6.000.000 | C=2.0 |
| 8 | SVM (LinearSVC) | ALLE | C=1.0 |
| 9 | Logistic Regression | 300.000 | C=1.0, solver=saga |
| 10 | Logistic Regression | 6.000.000 | C=1.0, solver=saga |
| 11 | Logistic Regression | 6.000.000 | C=0.5, solver=saga |
| 12 | Logistic Regression | 6.000.000 | C=2.0, solver=saga |
| 13 | Logistic Regression | 6.000.000 | C=1.0, solver=lbfgs |
| 14 | Logistic Regression | ALLE | C=1.0, solver=saga |
| 15 | Neural Network | 300.000 | layers=256, lr=0.0001 |
| 16 | Neural Network | 6.000.000 | layers=256, lr=0.0001 |
| 17 | Neural Network | 6.000.000 | layers=256, lr=0.005 |
| 18 | Neural Network | 6.000.000 | layers=512, lr=0.005 |
| 19 | Neural Network | ALLE | layers=512, lr=0.005 |