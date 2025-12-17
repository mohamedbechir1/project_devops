# Projet DevOps - Application Web & Pipeline CI/CD

Ce projet est conçu pour une évaluation académique et vise à démontrer une chaîne **DevOps complète**. Il s'agit d'une application distribuée (Microservices) intégrant le développement, la conteneurisation, l'Infrastructure as Code (IaC) et l'automatisation CI/CD.

## 🎯 But du Projet

L'objectif principal est de mettre en œuvre les meilleures pratiques DevOps à travers :
1.  **Développement d'une application 3-tiers** moderne (Frontend, Backend, AI Service).
2.  **Conteneurisation** des services pour garantir la portabilité (Docker).
3.  **Infrastructure as Code (IaC)** pour automatiser le déploiement d'environnements (Vagrant & Ansible).
4.  **Intégration et Déploiement Continus (CI/CD)** pour automatiser le cycle de vie du logiciel (Jenkins).

---

## 🛠 Technologies Utilisées

### Application
*   **Frontend** : Vue.js 3 + Vite + TypeScript (Interface utilisateur réactive).
*   **Backend** : Python + FastAPI (API REST principale).
*   **Service AI** : Python + FastAPI (Microservice d'analyse de sentiment).
*   **Base de Données** : PostgreSQL 15.

### DevOps & Infrastructure
*   **Conteneurisation** : Docker & Docker Compose.
*   **Virtualisation** : Vagrant (Simulation d'environnement de production avec des VMs).
*   **Configuration Management** : Ansible (Provisioning des serveurs).
*   **CI/CD** : Jenkins (Automation des tests et builds).

---

## 🏗 Architecture du Projet

L'application suit une architecture micro-services où chaque composant a une responsabilité unique :

1.  **Frontend (Vue.js)** : Envoie les requêtes des utilisateurs au Backend.
2.  **Backend (FastAPI)** : Orchestre la logique métier.
    *   Il stocke et récupère les données dans **PostgreSQL**.
    *   Il délègue l'analyse de texte au **Service AI**.
3.  **AI Service** : Analyse le sentiment (Positif/Négatif) d'un texte donné via un algorithme simple.

### Schéma de Communication
`Utilisateur` ➡️ `Frontend (Port 3000)` ➡️ `Backend (Port 8000)` ➡️ `Database (Port 5432)`
                                                        ⬇️
                                      `AI Service (Port 8001)`

---

## 📂 Aperçu des Dossiers

Voici la structure de notre référentiel et la fonction de chaque dossier :

*   **`frontend/`** : Code source de l'interface utilisateur (Vue.js, composants, styles).
*   **`backend/`** : API principale (connexion DB, logique métier).
*   **`ai-service/`** : Microservice dédié à l'analyse de sentiments.
*   **`db/`** : Scripts ou configurations liés à la base de données PostgreSQL.
*   **`deploy/`** : Contient le fichier `docker-compose.yml` pour lancer l'environnement complet en local.
*   **`infra/`** : Code Infrastructure as Code.
    *   `Vagrantfile` : Définition des machines virtuelles (ex: vm-jenkins, vm-app).
    *   `ansible/` : Playbooks et rôles pour configurer les VMs automatiquement.
*   **`ci/`** : Fichiers de configuration pour l'intégration continue (ex: `Jenkinsfile`).

---

## ✨ Fonctionnalités

### Fonctionnalités de l'Application
1.  **Vérification de Santé (Health Check)** : Monitoring de l'état des services API et DB.
2.  **Analyse de Sentiment** : L'utilisateur envoie une phrase, l'IA détermine si elle est positive ou négative (via des mots-clés prédéfinis).
3.  **Interaction Base de Données** : Exemple de requête pour vérifier le temps de réponse de la DB.

### Fonctionnalités DevOps
*   **Lancement en une commande** : Environnement de développement complet via Docker Compose.
*   **Provisioning Automatisé** : Déploiement de l'infrastructure serveurs via Ansible.
*   **Pipeline Automatisé** : Build et Tests gérés par Jenkins.

---

## 🚀 Démarrage Rapide (Local)

**Prérequis** : Docker et Docker Compose installés.

1.  Accédez au dossier de déploiement :
    ```bash
    cd deploy
    ```

2.  Lancez les services :
    ```bash
    docker compose up --build
    ```

3.  Accédez à l'application :
    *   **Frontend** : http://localhost:3000
    *   **Backend API** : http://localhost:8000/docs
    *   **AI Service Docs** : http://localhost:8001/docs
