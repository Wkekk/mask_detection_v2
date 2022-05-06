# Brief détection de masques avancée

## Le projet

Le but de ce projet était de reprendre le brief de détection de masque et de l'améliorer en permettant une déection sur plusieurs visages en simultané.

## Le fonctionnement

Pour ce projet j'ai repris le code écrit lors du brief précédant, le modèle ML de détection et la partie détection en elle même, et je l'ai inséré dans le code effetué lors du tp de détection de visage et de création d'application avec streamlit. J'ai modifié la fonction `detection_visage` pour appliquer la détection de masque sur chaque rectangle retourné par la détection de visage. 