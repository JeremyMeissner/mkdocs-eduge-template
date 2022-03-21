# Fonctionalités normales de mkdocs

## Niveaux de titres
texte du titre niveau 2
### Titre 3
texte du titre niveau 3
La table des matières n'affiche plus à partir de là.

#### Titre 4
texte du titre niveau 4
##### Titre 5
texte du titre niveau 5
###### Jusqu'à Titre 6
texte du titre niveau 6 (le maximum autorisé)

## Assemblage des fichiers
Lors de la compilation, mkdocs va réunir tous les fichiers .md et les fusionner afin d'avoir uniquement un fichier .pdf.
Il va prendre les fichiers dans cette ordre la :

1. index.md
2. [000].md
3. [a-zA-Z].md

Si un fichier ne contient pas de Titre 1, son nom est utilisé afin de créer le titre 1

Donc `fichier_sans_titre.md` deviendra `# Fichier sans titre`

Par défaut, lors du serve, le site va sur la page index.md, si elle n'existe pas, nous nous retrouvons face à une erreur 404. Il suffit de cliquer sur le menu de navigation à gauche afin d'accéder au bon document.


## Différentes syntaxes de listes

N°1

+ One
    + 1.1
    + 1.2
      + 1.2.1
+ Two
    + 2.1
    + 2.2


N°2

- One
    - 1.1
    - 1.2
      - 1.2.1
- Two
    - 2.1
    - 2.2

N°3

* item 1
  * 1.2
    * 1.2.1
* Item 2

Il faut faire attention a bien séparer les différents types de listes, sinon la deuxième va garder la même mise en forme que la première !

On peut aussi créer des listes ordrées :

1. Ordered list element one
   1. test 1.1
1. Ordered list element two
1. Ordered list element three 

Par contre dans ces listes, il n'y a qu'un seul niveau de numérotation, impossible d'avoir 1.1.

## Bloques de code
On peut insérer du code en pleins milieu d'une phrase `Inline` de cette manière. 

Où écrire son texte et afficher le code ensuite.
```
Multi
lignes
```

## Citations

    Avec des tabulations
    avant le texte

> Avec des >
> avant le texte

> This is blockquote text
> This is the second line of text
>> This is nested blockquotes content


> ### Création d'un titre dans une citation
> **bold text**
> _italic text_
> ~~strikethrough text~~
> `code element`

## Propriétés de text

*Italic* 

**Bold** __Bold__ 

_Souligné_

~~Baré~~

## Liens web

[Lien](https://en.wikipedia.org/wiki/URL)

[Lien avec description](https://en.wikipedia.org/wiki/URL "description")

## Tableaux

| Header1 | Header2 | Header3 |
| ------- | ------- | ------- |
| data1   | data2   | data3   |
| data11  | data12  | data13  |

| Header1        | Header2      | Header3 |
| -------------- | ------------ | ------- |
| **bold style** | `code block` | data3   |
| \|escape pipe  | \`backtick   | data13  |

| Header1    |     Header2 |   Header3   |
| :--------- | ----------: | :---------: |
| Align left | Align right | center text |
| cell data1 |  cell data2 | cell data3  |

## Commentaires
Si vous voulez mettre des commentaires qui n'apparaissent pas dans votre pdf où lors d'un serve de mkdocs, il suffit de les mettres dans des balises html.
``` html
<!---
comments syntax
--->
```

<!---
Ainsi vos commentaires ne ressortent, ni dans le rendu html, ni dans le pdf
comments syntax
--->
