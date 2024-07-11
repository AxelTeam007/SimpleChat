import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Télécharger les ressources nécessaires
nltk.download('punkt')
nltk.download('stopwords')

def lire_connaissances(dossier):
    connaissances = {}
    for fichier in os.listdir(dossier):
        if fichier.endswith(".txt"):
            chemin_fichier = os.path.join(dossier, fichier)
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                connaissances[fichier] = contenu
    return connaissances

def traiter_contenu(contenu):
    tokens = word_tokenize(contenu)
    mots_vides = set(stopwords.words('french'))
    tokens = [mot for mot in tokens if mot.isalnum() and mot not in mots_vides]
    return tokens

def repondre(question, corpus):
    tokens_question = traiter_contenu(question)
    reponses_potentielles = {}
    
    for fichier, tokens in corpus.items():
        correspondance = len(set(tokens_question).intersection(tokens))
        if correspondance > 0:
            reponses_potentielles[fichier] = correspondance
    
    if not reponses_potentielles:
        return "Je suis désolé, je ne sais pas répondre à cette question."
    
    meilleur_fichier = max(reponses_potentielles, key=reponses_potentielles.get)
    return connaissances[meilleur_fichier]

dossier_connaissances = 'knowledge'
connaissances = lire_connaissances(dossier_connaissances)
corpus = {fichier: traiter_contenu(contenu) for fichier, contenu in connaissances.items()}

print("Bienvenue au SimpleChat. Tapez 'quit' pour quitter. GitHub : https://github.com/AxelTeam007")

while True:
    question = input("Vous : ")
    if question.lower() == 'quit':
        print("Merci d'avoir utilisé SimpleChat. Au revoir !")
        break
    reponse = repondre(question, corpus)
    print("SimpleChat : " + reponse)
