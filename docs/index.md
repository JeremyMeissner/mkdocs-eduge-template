---
auteur : 
    - Albadri
    - Cotture
    - Meissner
    - Pfister

my_var : hello world
---


# Template MkDocs Eduge
Ce document ainsi que cette configuration a été produite par {{ array_to_string( page.meta.auteur ) }} 

Ci-dessous se trouve notre travail d'atelier, fait dans le cours ***Atelier Tech 1 et Tech 2*** de 2021-2022

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

Vous avez la possibilité d'imprimer le contenu de toute vos variables grâce à `page.meta`

{{ page.meta }}

Vous êtes obligés d'utiliser `page.meta` si vous voulez utilisez des fonctions python avec comme paramètre des variables présentes dans votre fichier .md
 
autrement vous avez la possibilité de mettre directement entre double {} le nom de votre variable afin que son contenu soit affiché. `{{ my_var }}`  

## Pymdownx
https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/ 

C'est l'extension la plus pratique et la plus complète que nous avons trouvé.

Tout ce que nous vous proposons ci-dessous fonctionnent aussi dans le PDF.

Le contenu n'est pas "documenté", mais il est suffisemment compréhensible pour savoir à quoi sert chaque partie.
 

### snippets
``` python
# Python
def NumberOfLife()
    return 42

```

``` clojure
;; Clojure
(defn number-of-life [] 42)

```

``` csharp
// C#
public int NumberOfLife() {
    return 42;
}

```

### keys 
++ctrl+alt+delete++





### inlinehilite
Here is some code: `#!py3 import pymdownx; pymdownx.__version__`.

The mock shebang will be treated like text here: ` #!js var test = 0; `.





### superfences
``` {linenums="10"}
"""Some file."""
import foo.bar
import boo.baz
import foo.bar.baz
```
 
```{.py3 hl_lines="1-2 5 7-8" linenums="10"}
import foo
import boo.baz
import foo.bar.baz

class Foo:
   def __init__(self):
       self.foo = None
       self.bar = None
       self.baz = None
```

```{.py3 title="My Cool Header"}
import foo.bar
import boo.baz
import foo.bar.baz
```


### caret
H^2^0

text^a\ superscript^
  

### tilde
~~Delete me~~

CH~3~CH~2~OH

text~a\ subscript~



### emoji 
:smile: :heart: :thumbsup:


### magiclink
- Just paste links directly in the document like this: https://google.com.
- Or even an email address: fake.email@email.com. 



### mark

==mark me==

==smart==mark==



### progress bar  
`non fonctionnel`

[=0% "0%"]
[=5% "5%"]
[=25% "25%"]
[=45% "45%"]
[=65% "65%"]
[=85% "85%"]
[=100% "100%"]

[=85% "85%"]{: .candystripe}
[=100% "100%"]{: .candystripe .candystripe-animate}

[=0%]{: .thin}
[=5%]{: .thin}
[=25%]{: .thin}
[=45%]{: .thin}
[=65%]{: .thin}
[=85%]{: .thin}
[=100%]{: .thin}





### task list
`non fonctionnel sur le pdf`
Task List

- [X] item 1
    * [X] item A
    * [ ] item B
        more text
        + [x] item a
        + [ ] item b
        + [x] item c
    * [X] item C
- [ ] item 2
- [ ] item 3

[ ] item 2
[X] item 2











### Arithmatex
`nécéssite intenren`


$$
E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
$$

\[3 < 4\]

\begin{align}
    p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
    p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
\end{align}

<!-- 
## AUTRES

Task List

- [X] item 1
    * [X] item A
    * [ ] item B
        more text
        + [x] item a
        + [ ] item b
        + [x] item c
    * [X] item C
- [ ] item 2
- [ ] item 3

<ul class="task-list">
    <li class="task-list-item">
        <label class="task-list-control">
            <input type="checkbox" disabled checked="">
            <span class="task-list-indicator"></span>
        </label>
        item 1
    </li>
</ul>

| Tables super long title  |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  1 | $1600 |
| col 2 is |    2   |   $12 |
| col 3 is | 3 |    $1 |

<ul class="task-list">
<li class="task-list-item"><input checked="" disabled="" type="checkbox"> item 1<ul class="task-list">
<li class="task-list-item"><input checked="" disabled="" type="checkbox"> item A</li>
<li class="task-list-item"><input disabled="" type="checkbox"> item B
    more text<ul class="task-list">
<li class="task-list-item"><input checked="" disabled="" type="checkbox"> item a</li>
<li class="task-list-item"><input disabled="" type="checkbox"> item b</li>
<li class="task-list-item"><input checked="" disabled="" type="checkbox"> item c</li>
</ul>
</li>
<li class="task-list-item"><input checked="" disabled="" type="checkbox"> item C</li>
</ul>
</li>
<li class="task-list-item"><input disabled="" type="checkbox"> item 2</li>
<li class="task-list-item"><input disabled="" type="checkbox"> item 3</li>
</ul>

... -->


<!-- 

# Title1
1
## Title2
2
### Title3
3
#### Title4
4
##### Ttitle 5
5
###### Title 6
6 -->

## Images

Nous avons programmé des fonctions python permettant :

- Insérer une image
- Mettre une légende
- Numéroté les figures
- Lui fixer une taille en pourcentage de la page

{{ fig("img/NewTux.svg", "Linux", 65) }}

{{ fig("img/logo.png", "CFPT", 35) }}

{{ fig("img/1024.jpg", "thanos", 100) }}




vous avez la possibilité de faire une référence direct sur une image 


{{ figRef(1) }}

{{ figListing() }}



{{ ref("NAME 00", "blib blo texto") }}

{{ ref("NAME 20", "boooo") }}


{{ ref("NAME 00") }}


## Listing REF
{{ refListing() }}


{{ lex("NAME 00", "blib blo texto") }}

{{ lex("NAME 100", "blib2222") }}


{{ lex("NAME 00") }}


## Listing LEXIQUE
{{ lexListing() }}
