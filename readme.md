# Brief détection de masques avancée

## Le projet

Le but de ce projet était de reprendre le brief de détection de masque et de l'améliorer en permettant une déection sur plusieurs visages en simultané.

## Le fonctionnement

Pour ce projet j'ai repris le code écrit lors du brief précédant, le modèle ML de détection et la partie détection en elle même, et je l'ai inséré dans le code effetué lors du tp de détection de visage et de création d'application avec streamlit. J'ai modifié la fonction `detection_visage` pour appliquer la détection de masque sur chaque rectangle retourné par la détection de visage.

## Lancement :

1- récupérer le modèle sur le lien suivant : https://drive.google.com/drive/folders/10Vusfch62fMcX2MxIAvyxQWlFdrFcnc_?usp=sharing

2- lancer le programme visage_et_masque.py dans streamlit avec la commande : `streamlit run visage_et_masque.py`

3- ouvrir le lien sorti dans le terminal

4- upload un fichier image sur l'application et attendre que la photo s'affiche (peut prendre un peu de temps)

5- cliquer sur process et laisser le programme effectuer les détection (peut prendre un peu de temps)

Les résultats s'affiche sur une copie de l'image et l'historique dans un tableau juste sous celle-ci (il est également trouvable dans le fichier `output.csv`)