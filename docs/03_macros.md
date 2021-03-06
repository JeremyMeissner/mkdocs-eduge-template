---
auteur : 
    - Albadri
    - Cotture
    - Meissner
    - Pfister

my_var : hello world
---

# Macros préparées

## Macros
Si vous utilisez le plugin macro, comme tout en haut de ce document.

``` yaml
---
# Exemple du contenu en haut de la page md
auteur : 
    - Albadri
    - Cotture
    - Meissner
    - Pfister
---
```

Vous avez la possibilité d'imprimer le contenu de toutes vos variables grâce à `page.meta`

{{ page.meta }}

Vous êtes obligés d'utiliser `page.meta` si vous voulez utiliser des fonctions python avec comme paramètre des variables présentes dans votre fichier .md
 
autrement vous avez la possibilité de mettre directement entre doubles {} le nom de votre variable afin que son contenu soit affiché. `{{ my_var }}`  

### Création de figures, images

Nous avons programmé des fonctions python permettant :

- Insérer une image
- Mettre une légende
- Numéroter les figures
- Fixer une taille en pourcentage de la page


Insère une figure occupant 65% de la largeur 

{{ fig("/img/SVG.svg", "Une image au format SVG à 65% de la largeur.", 65) }}

{{ fig("/img/logo.png", "une image sous format PNG du CFPT à 35% de la largeur.", 35) }}

{{ fig("/img/jpeg.jpg", "Une image au format JPEG à 100% de la largeur.", 100) }}


vous avez la possibilité de faire une référence directe sur une image 


Comme ici {{ figRef(2) }}

C'est très pratique pour créer une liste des figures.

Il faut cependant mettre le texte "Table des figures" ou autre avant l'appel de la fonction.

#### Tables des figures
{{ figListing() }}


### Références
 
Création de référence {{ ref("mkdocs", "Source : https://www.mkdocs.org/") }}


{{ ref("Eduge", "Source : https://eduge.ch/") }}


Utilisation à nouveau d'une référence {{ ref("mkdocs") }}
 
### Listing des references
Comme pour les figures, il faut ajouter un titre manuellement.

#### Table des références 
{{ refListing() }}



### Lexiques
Création de lexique {{ lex(".md", "Extension de fichier markdown") }}


Les couches du modèles {{ lex("OSI", "Open Systems Interconnection") }} sont ...


Utilisation à nouveau d'une référence {{ lex(".md") }}


 
### Listing LEXIQUE 
Comme pour les figures, il faut ajouter un titre manuellement.

#### Table des lexiques
{{ lexListing() }}


### Insertion de code source depuis un fichier
  
``` py linenums="1" title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

Simple macro pour insérer du code avec un titre

{{src('src/code.sql', 'sql')}}

ou sans titre
{{src('src/code.sql', 'sql', False)}}


<!-- 
```
code
sans lignes
```

``` {linenums="1"}
code
avec lignes
```

``` sql
select * from tab;
``` 
-->

### Information sur l'environement des macros

Pour afficher plus d'informations sur les macros d'expansion, utilisez `[[macros_info()]]` mais en replaçant les [] par {}.
