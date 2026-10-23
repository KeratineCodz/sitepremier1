# 📒 Mon carnet de bord

**Nom :** 

**Prénom :** 

**Adresse de mon site :** https://______.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code est stocké sur GitHub et déployé sur PythonAnywhere, où l'application Flask s'exécute pour afficher le site web.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que le site est hébergé sur un serveur accessible par Internet. Il suffit d'avoir un navigateur web et le lien du site pour y accéder, sans rien installer sur son ordinateur.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est www.google.com et le chemin est /maps.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Le message Not Found signifie que la page demandée n'a pas été trouvée. Il est généralement envoyé par le serveur avec le code HTTP 404.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ En Python, la deuxième définition remplace la première association avec ce nom. Si les routes Flask ont des noms de points de terminaison identiques, cela peut également provoquer un conflit. Il est préférable d'utiliser des noms de fonctions uniques.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du code HTML et le navigateur interprète ce code pour afficher une page avec des titres, des paragraphes, des listes et des images

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ <h1> sert à afficher le titre principal.

<p> sert à créer un paragraphe.

<ul> sert à créer une liste à puces.

<li> sert à afficher un élément de la liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ L'image est hébergée sur un serveur externe. Le navigateur utilise l'adresse indiquée dans l'attribut src pour la télécharger et l'afficher.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Cela permet de rendre le projet plus clair et plus facile à modifier. Le développeur peut travailler sur le code Python tandis que le graphiste peut modifier la présentation HTML sans toucher à la logique du programme.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Ils sont remplacés par le serveur grâce au moteur de templates Jinja de Flask, avant l'envoi de la page au navigateur. Je l'ai vérifié avec Ctrl + U : le code source affiche directement mon prénom et mon nom à la place des variables {{ prenom }} et {{ nom }}.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML définit la structure et le contenu de la page, tandis que le CSS définit son apparence, comme les couleurs, les polices, les marges et la mise en page.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Il télécharge au minimum deux ressources du site : le document HTML généré par Flask et le fichier CSS static/style.css. Si l'image externe s'affiche, il télécharge également cette image depuis son serveur.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Parce que le navigateur peut conserver une ancienne version du fichier CSS dans son cache. Ctrl + F5 force son rechargement.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur envoie une requête au serveur et le serveur renvoie une réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ La page déclenche au minimum une requête pour le document HTML /presentation et une autre pour le fichier CSS /static/style.css. Le navigateur peut également demander la favicon et le logo Python hébergé sur un serveur externe. Le nombre exact dépend des requêtes observées dans l'onglet Réseau.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code HTTP 200 signifie que la requête a réussi. Le code 404 signifie que la ressource demandée n'a pas été trouvée, par exemple si le site ne possède pas de favicon.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Parce que ces modifications sont locales à mon navigateur. Elles ne modifient pas les fichiers enregistrés sur le serveur et disparaissent généralement lorsque je recharge la page.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le nom du paramètre est search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le serveur plante parce que la fonction int() ne peut pas convertir le texte bonjour en nombre entier. Pour éviter cette erreur, il faut vérifier les données reçues et utiliser try/except pour gérer les valeurs incorrectes.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Parce qu'un utilisateur peut envoyer du code HTML ou JavaScript malveillant. Si le serveur l'affiche directement dans la page, le navigateur peut interpréter ce code. Cela peut provoquer une faille appelée XSS (Cross-Site Scripting).

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ 

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ 

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ 

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ 

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ 

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
