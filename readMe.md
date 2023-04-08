# Objectif
L’objectif de ce projet est de créer un programme en python avec la librairie OpenCV capable à partir d’un dossier contenant des images de pochettes d’albums, de créer un fond d’écran sous la forme d’une grille de ces pochettes d’albums.

# Lancement
Utilisez le script run en tapant dans un terminal la commande :

`./run` <br/>
ou <br/>
`./run fichierParametres.txt`

# Paramètres
## Lecture des paramètres
Le programme lit sur l’entrée standard et il lit ses paramètres toujours dans l’ordre suivant :
- Le chemin (relatif ou absolu) du dossier contenant les images des pochettes d’albums (appelé dossier des pochettes par la suite).
- Le chemin (relatif ou absolu du dossier dans lequel l'image résultat sera sauvegardée (appelé dossier de sauvegarde par la suite).
- Le nom de fichier de l'image résultat.
- Le format de l'image résultat.
- La taille des cases sur la grille.
- La définition ciblée de l’image à générer (appelé définition cible par la suite).
- La section des tailles des pochettes.
- La section des poids des pochettes.

Le contenu, format et validité de chaque paramètres sont donnés dans la section validités des paramètres.

## Validités des paramètres
Lors de la lecture des paramètres du programme dès qu’un paramètre est manquant ou invalide alors le programme s’arrête avec le code de retour 1 et affiche un message d’erreur à propos du paramètre problématique.
### Dossier des pochettes
Ce paramètre est une chaîne de caractères sur une ligne correspondant au chemin (relatif ou absolu) du dossier contenant les pochettes d’albums à utiliser.
Le dossier indiqué par le chemin doit exister, être accessible et le programme doit pouvoir lire son contenu.
### Dossier de sauvegarde
Une chaîne de caractères sur une ligne correspondant au chemin (relatif ou absolu) du dossier où l'image résultat sera sauvegardée.
Le dossier indiqué par le chemin doit exister, être accessible et le programme doit pouvoir lire son contenu.
### Nom
Une chaîne de caractères sur une ligne correspondant au nom du fichier dans laquelle l'image résultat sera sauvegardée.
Le nom ne peut pas être une chaîne de caractères vide et il ne doit contenir que des caractères ASCII.
### Format
Une chaîne de caractères sur une ligne correspondant au format du fichier dans laquelle l'image résultat sera sauvegardée.
Le format doit être présent dans la liste suivante : bmp, dib, jpeg, jpg, jpe, jp2, png, pbm, pgm, ppm, sr, ras, tiff, tif.
Taille des cases
Un entier positif supérieur à 0 sur une ligne correspondant à la taille des cases de la grille en nombre de pixels.
### Définition cible
Deux entiers supérieurs à 0 séparés par un espace et sur une ligne, correspondant à la définition de l'image résultat.
La première valeur est la largeur en nombre de pixels et la seconde est la hauteur en nombre de pixels.
Les deux valeurs du paramètres doivent être divisibles par la taille des cases.
### Section tailles des pochettes
Cette section est composée de 0 à N lignes et se termine par une ligne vide. Chaque ligne est composée de deux entiers positifs séparés par un espace.
- La première valeur correspond à une taille que chaque pochette peut prendre sur la grille, par exemple si cette valeur vaut 5 alors les pochettes sur la grille peuvent avoir une taille de 5*5 cases sur la grille. 
Cette valeur doit être supérieure à 0.
- La seconde valeur correspond au nombre maximum de pochettes pouvant prendre cette taille.
Cette valeur doit être supérieure à 1.

Si une ligne de cette section est invalide alors elle est ignorée.

### Section poids des pochettes
Cette section peut être composée de 0 à N lignes. Chaque ligne est composée de deux valeurs séparées par un espace :
- une chaîne de caractères (sans espaces et en ASCII) correspondant à un nom de fichier d’une pochette d’album.
- un entier supérieur à 1 correspondant au poids de cette pochette d’album. Plus cette valeur est grande, plus la pochette à une probabilité élevée d’avoir une grande taille sur la grille.

Si une ligne de cette section est invalide alors elle est ignorée.

# Gestion des pochettes
## Récupération
Tous les fichiers dans le dossier des pochettes qui ne sont pas des images sont ignorés.

Si le programme n’a pas les droits de lecture sur une image alors il l’ignore et affiche un avertissement mais si à la fin de la récupération des pochettes aucune image n’a été lue alors le programme affiche un message d’erreur et se termine avec le code de retour 2.

Chaque image doit être de préférence un carré.
## Ordre des pochettes
La liste des pochettes est tirée en fonction des poids des pochettes (voir paramètre section poids des pochettes) mais les pochettes de même poids sont placées aléatoirement dans la liste.

La liste :
- [(a, 8), (b, 1), (c, 8), (d, 8), (e, 3), (f, 3), (g, 1), (h, 1), (i, 3), (j, 5)] 

peut par exemples être une fois triée :
- [(a, 8), (d, 8), (c, 8), (j, 5), (i, 3), (f, 3), (e, 3), (g, 1), (b, 1), (h, 1)]
- [(d, 8), (a, 8), (c, 8), (j, 5), (f, 3), (e, 3), (i, 3), (h, 1), (g, 1), (b, 1)]
- [(c, 8), (d, 8), (a, 8), (j, 5), (i, 3), (e, 3), (f, 3), (b 1), (h, 1), (g, 1)]
