# 🚀 Planification du Projet d'API de Score de Risque Cardiovasculaire
# 1. 🤝 Organisation et Collaboration
Le travail en binôme sera réparti comme suit, avec une méthodologie Git/GitHub claire :
Branche Principale : main (Contient la version stable et déployable).
Fusion : Les branches de fonctionnalités (feature/api, feature/ml) seront fusionnées dans main après validation des tests et revue de code.
# 2. 💻 Développement Web & Base de Données (Backend)
Le Développeur Backend se concentrera sur l'infrastructure de l'API.

A. Structure FastAPI & Modèles de Données
Pydantic : Définir les schémas pour la validation des données :

PatientBase: Attributs communs (nom, âge, sexe, etc.).

PatientCreate: Hérite de PatientBase, utilisé pour la création.

Patient: Hérite de PatientBase et inclut l'ID de la DB.

RiskPrediction: Schéma de la réponse pour la prédiction (ex: risk_score: float, category: str).

API Principal : Création du fichier principal (main.py ou app.py) et initialisation de FastAPI.
# B. Base de Données SQLite avec SQLAlchemy
Configuration : Mettre en place la connexion à SQLite et configurer l'ORM (SQLAlchemy).

Modèle DB : Définir le modèle SQLAlchemy (PatientModel) correspondant au schéma Pydantic.

CRUD (Create & Read) Endpoints :
**POST /patients** : Prend un objet PatientCreate et l'ajoute à la base de données. Retourne l'objet Patient créé.
**GET /patients** : Retourne la liste de tous les patients enregistrés.
# 3. 🧠 Modélisation IA/Data (Data Science)
Le Développeur IA/Data se concentrera sur la construction du modèle et son intégration.
# A. Préparation et Entraînement du Modèle
Nettoyage du Dataset : Gérer les valeurs manquantes, encoder les variables catégorielles, normaliser/standardiser les caractéristiques numériques.
Sélection & Entraînement : Choisir un algorithme (ex: Régression Logistique, Random Forest, Gradient Boosting) et l'entraîner sur les données.
Sauvegarde : Sauvegarder le modèle entraîné (ex: avec joblib ou pickle) dans un fichier (ex: model.pkl) pour qu'il puisse être chargé par l'API.
**POST /patients** : Prend un objet PatientCreate et l'ajoute à la base de données. Retourne l'objet Patient créé.
**GET /patients** : Retourne la liste de tous les patients enregistrés.
# B. Intégration de la Prédiction (Endpoint)
Chargement : La fonction d'initialisation de l'API doit charger le modèle sauvegardé en mémoire une seule fois au démarrage.

**POST /predict_risk** :

Prend un schéma Pydantic des caractéristiques d'entrée (PatientFeatures - les données nécessaires à la prédiction, sans l'ID de la DB).

Effectue les mêmes transformations (normalisation/encodage) que celles utilisées lors de l'entraînement.

Utilise le modèle chargé pour générer le score de risque.

Retourne une réponse structurée selon le schéma RiskPrediction.
# 4. ✅ Tests Unitaires et Documentation
# A. Tests Unitaires avec pytest
Tests pour feature/api (Développeur Backend) :

Vérifier le statut 201 Created pour POST /patients et la bonne persistance des données en DB.

Vérifier le statut 200 OK et le contenu correct de la réponse pour GET /patients.

Test pour feature/ml (Développeur IA/Data) :

Utiliser le TestClient de FastAPI pour tester l'endpoint **POST /predict_risk**.

Vérifier le **status_code = 200**.

Vérifier que la réponse est conforme au schéma RiskPrediction (score est un flottant, etc.).

# B. Documentation Interactive (Swagger)
FastAPI génère automatiquement la documentation interactive (Swagger UI) à l'adresse /docs par défaut.
