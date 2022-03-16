# Fonctionalités normales de mkdocs

## Plusieurs niveaux de titres sont possibles
texte du titre niveau 2
### Title3
texte du titre niveau 3
#### Title4
texte du titre niveau 4
##### Ttitle 5
texte du titre niveau 5
###### Jusqu'à Title 6
texte du titre niveau 6 (le maximum autortisé)

## On peut aussi diviser le markdown en plusieurs fichiers

`01.md` Sera le premier qui prendra le titre de son `# Titre 1`

`02.md` Sera le second qui prendra le titre de son `# Titre 1 du deuxsième fichier`

## Il y a des listes

+ One
    + 1.1
    + 1.2
+ Two
    + 2.1
    + 2.2
+ Three


a

- One
    - 1.1
    - 1.2
- Two
    - 2.1
    - 2.2
- Three

b

* item 1
* Item 2

Mais il faut séprarer les types de listes, sinon ça continue sur la première

1. Ordered list element one
1. Ordered list element two


## Des bloques de code

`Inline` ou
```
Multi
lignes
```

## Des citations

    Avec des tabs
    avant

> ou avec des >
> avant

> This is blockquote text
> This is the second line of text
>> This is nested blockquotes content


> #### Heading in blockquotes text
> **bold text**
> _italic text_
> ~~strikethrough text~~
> `code element`

## Des propriétés de text

*Italic* 

**Bold** __Bold__ 

_Souligné_

~~Baré~~

## Des liens web

[Lien](https://en.wikipedia.org/wiki/URL)

[Lien avec alt-text](https://en.wikipedia.org/wiki/URL "Alt text")

## Des tables

|Header1 |Header2  | Header3|
--- | --- | ---|
|data1|data2|data3|
|data11|data12|data13|

|Header1 |Header2  | Header3|
|--- | --- | ---|
|**bold style**| `code block`|data3|
|\|escape pipe|\`backtick|data13|

|Header1 |Header2  | Header3|
|:--- | ---: | :---:|
|Align left| Align right|center text|
|cell data1|cell data2|cell data3|

## et des commentaires

``` html
<!---
comments syntax
--->
```

<!---
comments syntax
--->
