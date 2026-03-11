# Modellauswahl

## Naive Bayes

Naive Bayes ist ein Klassifikationsalgorithmus, der auf dem Satz von Bayes basiert.
Der Algorithmus nimmt an, dass die verwendeten Features voneinander unabhängig sind.
Bei der Sentimentanalyse würde es bedeuten, dass jedes einzelne Wort unabhängig von den anderen vorkommt. Diese Annahme ist in der Realität offensichtlich falsch, weil Wörter ihre Bedeutung erst im Kontext anderer Wörter bekommen.
Trotz dieser unrealistischen (naiven) Annahme soll Naive Bayes bei Klassifikationsaufgaben mit Dokumenten erstaunlich gut funktionieren.

## Logistic Regression

Logistische Regression ist ein Klassifikationsverfahren, in dem das Modell für eine Beobachtung die Wahrscheinlichkeit berechnet, zu einer bestimmten Klasse zu gehören.
Dazu wird eine lineare Kombination der Features berechnet und anschließend durch eine logistische Funktion in einen Wert zwischen 0 und 1 umgewandelt.
Auf Basis dieser Wahrscheinlichkeit wird entschieden, zu welcher Klasse die Beobachtung gehört.
## Support Vector Machine

Support Vector Machines sind ebenfalls ein Klassifikationsverfahren im überwachten Lernen.
Das Modell sucht eine Trennlinie (bzw. allgemein eine Trennebene) im Feature-Raum, die die Datenpunkte zweier Klassen voneinander trennt.
Dabei wird diejenige Trennlinie gewählt, die den größtmöglichen Abstand zu den nächstgelegenen Datenpunkten beider Klassen hat. Diese Punkte heißen Support-Vektoren und bestimmen die Lage der Grenze.
Wenn die Daten nicht linear trennbar sind, können sie mithilfe des Kernel-Tricks so behandelt werden, als lägen sie in einem höherdimensionalen Raum, in dem eine Trennung möglich ist.
Nachteil von SVM ist eine höhere Trainingszeit gegenüber Naive Bayes und Logistic Regression.

## Neuronales Netz

Ein neuronales Netz ist ein Modell, das aus mehreren miteinander verbundenen Recheneinheiten besteht.
Diese Einheiten sind in Schichten organisiert: eine Eingabeschicht, eine oder mehrere versteckte Schichten und eine Ausgabeschicht.
Jede Einheit berechnet aus den Eingaben einen gewichteten Wert und gibt das Ergebnis über eine Aktivierungsfunktion weiter.
Während des Trainings werden die Gewichte so angepasst, dass das Modell möglichst gute Vorhersagen für die Trainingsdaten macht.

## k-Nearest Neighbors
k-Nearest Neighbors (kNN) ist ein Lazy Learner.
Das Modell speichert die Trainingsdaten und berechnet für eine neue Beobachtung den Abstand zu den vorhandenen Datenpunkten.
Anschließend werden die k nächstgelegenen Nachbarn bestimmt.
Die neue Beobachtung wird der Klasse zugeordnet, die unter diesen Nachbarn am häufigsten vorkommt.