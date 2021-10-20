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

## Lancer le serveur de l'application
Dans le dossier du projet softdesk saisissez : 

```python
python3 manage.py runserver
```

Vous pouvez ensuite lancer le serveur via l'addresse affichée sur votre console 
