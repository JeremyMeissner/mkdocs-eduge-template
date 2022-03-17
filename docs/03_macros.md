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

{{ fig("/img/NewTux.svg", "Linux", 65) }}

{{ fig("/img/logo.png", "CFPT", 35) }}

{{ fig("/img/1024.jpg", "thanos", 100) }}


vous avez la possibilité de faire une référence directe sur une image 


Comme ici {{ figRef(4) }}

C'est très pratique pour créer une liste des figures.

Il faut cependant mettre le texte précent la table des figures avant son appel.
Par défaut nous ne lui avons rien indiqué.

#### Tables des figures
{{ figListing() }}


### Références

`TODO mettre un vrai exemple`
Création de référence + insertion {{ ref("NAME 00", "blib blo texto") }}

{{ ref("reference 2", "boooo") }}


Utilisation à nouveau d'une référence {{ ref("NAME 00") }}
 
### Listing des references
Comme pour les figures, il faut ajouter un titre manuellement.

#### Table des références 
{{ refListing() }}



### Lexiques

`TODO mettre un vrai exemple`
{{ lex("NAME 00", "lexico blo texto") }}

{{ lex("NAME 100", "blib2222") }}


{{ lex("NAME 00") }}

 
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

Simple macro pour le faire

{{src('src/code.sql', 'sql')}}

Sans titre
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
``` -->

### Information sur l'environement des macros

{{ macros_info() }}