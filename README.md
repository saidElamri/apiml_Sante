
# 3. Partie Machine Learning :
Cette section décrit la mise en place du modèle de Machine Learning pour évaluer le risque d'un patient et son intégration dans le service API FastAPI.
3.1. Préparation et Transformation des Données
L'objectif est de préparer un jeu de données hypothétique pour l'entraînement d'un modèle de classification.

| Tâche                      | Outil(s) Clé(s)               | Description |
|---------------------------|-------------------------------|-------------|
| Chargement des Données    | `Pandas`                      | Charger le jeu de données depuis un fichier (CSV ou JSON). Les données doivent contenir des caractéristiques (**X**) et une colonne cible (**y**) binaire (`0` = faible risque, `1` = risque élevé). |
| Nettoyage et Transformation | `Scikit-learn`, `Pandas`     | Catégorielles : `OneHotEncoder` ou `OrdinalEncoder`<br>Numériques : Imputation des valeurs manquantes + mise à l’échelle (`StandardScaler` ou `MinMaxScaler`). |
| Séparation X et y         | `train_test_split` (Scikit-learn) | Séparer les caractéristiques (**X**) de la variable cible (**y**). |
# 3.1 Construction du Pipeline Scikit-learn
 Un Pipeline est créé pour garantir que les étapes de prétraitement (nettoyage, encodage, mise à l'échelle) sont appliquées systématiquement sur les données d'entraînement, de test et, surtout, sur les données d'entrée de API.Structure du Pipeline :
 Structure du Pipeline :Préprocesseur :ColumnTransformer : Applique différents transformateurs (Scaler, OHE) à différents types de colonnes (numériques, catégorielles).Modèle :Un modèle de classification (ex: LogisticRegression, RandomForestClassifier, est choisi pour prédire la variable cible .
 # 3.3. Entraînement et Sauvegarde du Modèle
 Une fois le pipeline défini, il est entraîné sur le jeu de données X\_train / y\_train puis sauvegardé.
 # 3.4. (Bonus) Optimisation des Hyperparamètres avec GridSearchCV 
 Pour améliorer la performance du modèle, GridSearchCV est utilisé pour explorer systématiquement différentes combinaisons d'hyperparamètres.Principe : Il teste toutes les combinaisons possibles de paramètres définies dans une grille et utilise la Cross-Validation pour trouver la meilleure combinaison (best\_params\_) qui maximise une métrique cible (ex: accuracy ou F1-score).Intégration : La Pipeline peut être passée directement à GridSearchCV. L'objet grid_search.best_estimator_ devient alors le modèle à sauvegarder avec \textjoblib.
