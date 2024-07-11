# SimpleChat
<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW9sczhqeHk4bmJ4d2U0YTgxYWprcnRra3pxZzh1MWt3aTFmbzMwMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/20NLMBm0BkUOwNljwv/giphy.gif" alt="GIF animé en ligne" id="gif">

## Importations
- **`import os`** : Importe le module os pour interagir avec le système de fichiers.
- **`import nltk`** : Importe le module nltk pour le traitement du langage naturel.
- **`from nltk.tokenize import word_tokenize`** : Importe la fonction word_tokenize pour diviser le texte en mots.
- **`from nltk.corpus import stopwords`** : Importe la liste des stopwords (mots vides) de nltk.
- **`nltk.download('punkt') et nltk.download('stopwords')`** : Télécharge les ressources nécessaires pour la tokenisation et les stopwords.

## Fonction pour Lire les Connaissances
- **`def lire_connaissances(dossier)`** : Déclare une fonction qui lit les fichiers texte dans un dossier.
- **`connaissances = {}`** : Initialise un dictionnaire pour stocker le contenu des fichiers.
- **`for fichier in os.listdir(dossier)`** : Parcourt tous les fichiers du dossier.
- **`if fichier.endswith(".txt")`** : Vérifie que le fichier a une extension .txt.
- **`chemin_fichier = os.path.join(dossier, fichier)`** : Crée le chemin complet du fichier.
- **`with open(chemin_fichier, 'r', encoding='utf-8') as f`** : Ouvre le fichier en mode lecture avec encodage UTF-8.
- **`contenu = f.read()`** : Lit tout le contenu du fichier.
- **`connaissances[fichier] = contenu`** : Stocke le contenu du fichier dans le dictionnaire.
- **`return connaissances`** : Retourne le dictionnaire des connaissances.

## Fonction pour Traiter le Contenu
- **`def traiter_contenu(contenu)`** : Déclare une fonction qui traite le texte en le tokenisant et en filtrant les mots vides.
- **`tokens = word_tokenize(contenu)`** : Divise le contenu en mots (tokens).
- **`mots_vides = set(stopwords.words('french'))`** : Crée un ensemble de mots vides en français.
- **`tokens = [mot for mot in tokens if mot.isalnum() and mot not in mots_vides]`** : Filtre les tokens pour garder seulement les mots alphanumériques qui ne sont pas des mots vides.
- **`return tokens`** : Retourne la liste des tokens filtrés.

## Fonction pour Répondre aux Questions
- **`def repondre(question, corpus)`** : Déclare une fonction qui répond à une question en utilisant le corpus.
- **`tokens_question = traiter_contenu(question)`** : Traite la question pour obtenir les tokens.
- **`reponses_potentielles = {}`** : Initialise un dictionnaire pour stocker les correspondances potentielles.
- **`for fichier, tokens in corpus.items()`** : Parcourt chaque fichier et ses tokens dans le corpus.
- **`correspondance = len(set(tokens_question).intersection(tokens))`** : Calcule le nombre de tokens communs entre la question et le fichier.
- **`if correspondance > 0`** : Si des tokens communs sont trouvés...
- **`reponses_potentielles[fichier] = correspondance`** : Stocke la correspondance dans le dictionnaire.
- **`if not reponses_potentielles`** : Si aucune correspondance n'est trouvée...
- **`return "Je suis désolé, je ne sais pas répondre à cette question."`** : Retourne un message d'excuse.
- **`meilleur_fichier = max(reponses_potentielles, key=reponses_potentielles.get)`** : Trouve le fichier avec le plus de correspondances.
- **`return connaissances[meilleur_fichier]`** : Retourne le contenu du fichier avec le plus de correspondances.

## Boucle Principale pour l'Interaction avec l'Utilisateur
- **`dossier_connaissances = 'knowledge'`** : Définit le dossier contenant les fichiers de connaissances.
- **`connaissances = lire_connaissances(dossier_connaissances)`** : Lit les connaissances à partir du dossier.
- **`corpus = {fichier: traiter_contenu(contenu) for fichier, contenu in connaissances.items()}`** : Traite le contenu de chaque fichier et crée un corpus de tokens.<br>
- **`print("Bienvenue au chatbot. Tapez 'quit' pour quitter.")`** : Affiche un message de bienvenue et les instructions pour quitter.<br>
- **`while True`** : Démarre une boucle infinie pour interagir avec l'utilisateur.<br>
- **`question = input("Vous : ")`** : Lit la question de l'utilisateur.<br>
- **`if question.lower() == 'quit'`** : Si l'utilisateur tape "quit"...<br>
- **`print("Merci d'avoir utilisé le chatbot. Au revoir !")`** : Affiche un message de départ.<br>
- **`break`** : Sort de la boucle.<br>
- **`reponse = repondre(question, corpus)`** : Appelle la fonction repondre avec la question de l'utilisateur.<br>
- **`print("Chatbot : " + reponse)`** : Affiche la réponse du chatbot.