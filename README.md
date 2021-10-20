Développez une architecture back-end sécurisée en utilisant Django ORM
----------------------------------------------------------------------------------------------

## Installation

Tout d'abord, créez un dossier via la commande mkdir (ici projet12) dans lequel se trouvera l'environnement virtuel et l'application. Puis y accéder via la commande cd.

```python
mkdir projet12
cd projet12
```
Placer le dossier softdesk dedans.

```python
gh repo clone akfio/OCProjet-12
```

créez un environnement virtuel dans le dossier projet12 (ici nommé env):
```python
python3 -m venv env
```
Puis activez l'environnement virtuel via :

```python
source env/bin/activate #MacOS ou Unix
ou
env/Scripts/activate.bat #Sur Windows
```

Importer les packages nécessaire avec la commande :

```python 
pip install -r requirements.txt
``` 
## Mise en place de la base de donnée

Suivez les instructions d'installation de Postgresql : https://www.postgresql.org/download/
Puis, suivez les instructions d'installation pour pgAdmin4 : https://www.pgadmin.org/download/
ensuite, accéder à la console postgres:

```python 
sudo su - postgres
psql
``` 
Dans la console, il faut créer un mot de passe pour ajouter un server

```python 
ALTER USER <username> password '<mot de passe>'
``` 
Dans pgadmin4, créer un serveur avec votre username et votre mot de passe, et un nom de host (ici 'localhost'). 
Ensuite, créer un utilisateur et son mot de passe: ici Epic_Events 
Puis créer une Database et son mot de passe : ici Epic_Events et ocp12

Dans le fichier setting.py, Mettre à jour les informations de la database: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Epic_Events',
        'USER': 'Epic_Events',
        'PASSWORD': 'ocp12',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Vous pouvez maintenant réaliser les migrations :

```python 
python3 manage.py makemigrations
python3 manage.py migrate
``` 
Lancer la commande pour créer un superutilisateur 

```python
python manage.py createsuperuser
```

## Lancer le serveur de l'application
Dans le dossier du projet EpicEvents saisissez : 

```python
python3 manage.py runserver
```

Vous pouvez ensuite accéder à l'interface d'administration via http://127.0.0.1:8000/admin/

