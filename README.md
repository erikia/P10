# P10

Projet 10 : Créez une API sécurisée RESTful en utilisant Django REST

Ce projet a pour but de créer une API (SOFTDESK) permettant un suivi des problèmes pour les trois plateformes (site web, applications Android et iOS).
L'application permettra essentiellement aux utilisateurs de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.
Les trois applications exploiteront les points de terminaison d'API qui serviront les données.

# Processus
## Framework : Django REST
Ce projet utilise le framework Django REST pour crée une API (SOFTDESK).

Pour plus de détails sur le fonctionnement de cette API, se référer à sa documentation[https://documenter.getpostman.com/view/23795852/2s8YRgsF4J] (Postman).

# Utilisation

## Création de l'environnement virtuel

Pour la mise en palce de l'environnement virtuel :

## Sur Windows :
Dans le Windows Powershell il faudra cloner le git.
### Récupération du projet

    $ git clone https://github.com/erikia/P10.git

### Activer l'environnement virtuel
    $ cd P10 
    $ python -m venv env 
    $ ~env\scripts\activate
    
### Installer les modules
    $ pip install -r requirements.txt

### Executer le programme
Dans le répertoire qui contient manage.py dans le terminal, exécutez le programme:

    $ python manage.py migrate
    $ manage.py runserver

Puis ouvrez votre navigateur et allez sur la page suivante : http://127.0.0.1:8000/
    
----------------------------------------------
## Sur MacOS ou Linux :
Dans le terminal, il faudra cloner le git.
### Récupération du projet

    $ git clone https://github.com/erikia/P10.git

### Activer l'environnement virtuel
    $ cd P10
    $ python3 -m venv env 
    $ source env/bin/activate
    
### Installer les modules
    $ pip install -r requirements.txt

### Executer le programme
Dans le répertoire qui contient manage.py dans le terminal, exécutez le programme:

    $ python manage.py migrate
    $ manage.py runserver

Puis ouvrez votre navigateur et allez sur la page suivante : http://127.0.0.1:8000/

#### Endpoint API :

| #   | *Point de terminaison d'API*                                              | *Méthode HTTP* | *URL (base: http://127.0.0.1:8000)*       |
|-----|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| 1   | Inscription de l'utilisateur                                              | POST           | /signup/                                  |
| 2   | Connexion de l'utilisateur                                                | POST           | /login/                                   |
| 3   | Récupérer la liste de tous les projets rattachés à l'utilisateur connecté | GET            | /projects/                                |
| 4   | Créer un projet                                                           | POST           | /projects/                                |
| 5   | Récupérer les détails d'un projet via son id                              | GET            | /projects/{id}/                           |
| 6   | Mettre à jour un projet                                                   | PUT            | /projects/{id}/                           |
| 7   | Supprimer un projet et ses problèmes                                      | DELETE         | /projects/{id}/                           |
| 8   | Ajouter un utilisateur (collaborateur) à un projet                        | POST           | /projects/{id}/users/                     |
| 9   | Récupérer la liste de tous les utilisateurs attachés à un projet          | GET            | /projects/{id}/users/                     |
| 10  | Supprimer un utilisateur d'un projet                                      | DELETE         | /projects/{id}/users/{id}/                |
| 11  | Récupérer la liste des problèmes liés à un projet                         | GET            | /projects/{id}/issues/                    |
| 12  | Créer un problème dans un projet                                          | POST           | /projects/{id}/issues/                    |
| 13  | Mettre à jour un problème dans un projet                                  | PUT            | /projects/{id}/issues/{id}/               |
| 14  | Supprimer un problème d'un projet                                         | DELETE         | /projects/{id}/issues/{id}/               |
| 15  | Créer des commentaires sur un problème                                    | POST           | /projects/{id}/issues/{id}/comments/      |
| 16  | Récupérer la liste de tous les commentaires liés à un problème            | GET            | /projects/{id}/issues/{id}/comments/      |
| 17  | Modifier un commentaire                                                   | PUT            | /projects/{id}/issues/{id}/comments/{id}/ |
| 18  | Supprimer un commentaire                                                  | DELETE         | /projects/{id}/issues/{id}/comments/{id}/ |
| 19  | Récupérer un commentaire via son id                                       | GET            | /projects/{id}/issues/{id}/comments/{id}/ |
