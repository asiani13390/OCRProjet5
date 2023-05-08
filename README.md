# OCRProjet5

## Creation du dossier projet
mkdir OCRProjet5  
cd OCRProjet5

## Initialiser le projet GITHUB
Nom du dépot : OCRProjet5  
Commentaire du dépot : Créez une API sécurisée RESTful en utilisant Django REST  
Type : Public

Dans le dossier local du projet :
```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/asiani13390/OCRProjet5.git
git push -u origin main
```





## Creation de l'environnement virtuel python
python -m venv env

## GITHUB ne doit pas prendre en compte l'environement virtuel python
echo "env" > .gitignore

## Activer l'environnement virtuel python 
source env/bin/activate

## Install Django and Django REST framework into the virtual environment
pip install django  
pip install djangorestframework

## Creation du projet
django-admin startproject OCR

## Creation d'un commit GITHUB
Nom du commit : Installation de Django rest framework

## Création de l'application dans le projet
django-admin startapp app_p5

## Creation d'un commit GITHUB
Nom du commit : Installation de Django rest framework

## Première initialisation de la base de données
python manage.py migrate

## Creation d'un compte administrateur
python manage.py createsuperuser --email asiani@free.fr --username asi_admin

## Execution du serveur django
python manage.py runserver

## Vérifier que le serveur django fonctionne
http://localhost:8000

Une page web avec une fusée préte au décollage apparait

## Connexion à la page d'administration de django
http://localhost:8000/admin/

Pour cela utiliser le compte administrateur précédemment créé







