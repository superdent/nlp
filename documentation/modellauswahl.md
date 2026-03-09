# Modellauswahl

## Naive Bayes

Naive Bayes ist ein probabilistisches Klassifikationsverfahren, das auf dem Satz von Bayes basiert und Klassen-Unabhängigkeit der Features voraussetzt. Trotz dieser vereinfachenden Annahme zeigt das Modell bei Textklassifikationsaufgaben mit TF-IDF-Features konsistent gute Ergebnisse und besticht durch sehr kurze Trainingszeiten. Es dient im vorliegenden Projekt als schnelle Baseline.

## Logistic Regression

Logistic Regression ist ein lineares Klassifikationsverfahren, das die Zugehörigkeit zu einer Klasse über eine Softmax-Funktion modelliert. Es eignet sich gut für hochdimensionale, sparse Feature-Räume wie TF-IDF-Vektoren und liefert interpretierbare Gewichte. Bei Textklassifikation gilt es als starke Baseline mit guter Generalisierung.

## Support Vector Machine

Support Vector Machines suchen die Hyperebene, die den Margin zwischen den Klassen maximiert. Lineare SVMs (LinearSVC) sind besonders effektiv bei hochdimensionalen Textfeatures und erzielen typischerweise die höchste Genauigkeit unter den klassischen Verfahren. Der Nachteil ist eine höhere Trainingszeit gegenüber Naive Bayes und Logistic Regression.

## Neuronales Netz

Ein mehrschichtiges Perzeptron (MLPClassifier) kann nicht-lineare Entscheidungsgrenzen lernen und ist damit flexibler als die linearen Verfahren. Bei der vorliegenden Datenmenge und Feature-Dimensionalität ist der Mehraufwand durch längere Trainingszeiten und Hyperparameter-Tuning jedoch hoch, der Genauigkeitsvorteil gegenüber SVM und Logistic Regression erfahrungsgemäß gering.

## k-Nearest Neighbors (verworfen)

kNN klassifiziert Datenpunkte anhand der k nächsten Nachbarn im Feature-Raum. Das Verfahren wurde verworfen, da es kein explizites Modell lernt und die Inferenzkomplexität linear mit der Trainingsdatenmenge wächst (O(n)). Darüber hinaus leidet kNN in hochdimensionalen Räumen unter dem Fluch der Dimensionalität, was bei TF-IDF-Vektoren mit mehreren tausend Dimensionen zu deutlich verschlechterter Performance führt.
