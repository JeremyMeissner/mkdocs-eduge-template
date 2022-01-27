# Food Creator 


<!-- {{ image("1024.jpg", "tanos    jff j", "50") }} -->


<!-- {{ image("NewTux.svg", "fsddfffjf    jff j", "65") }} -->
*FoodCreator&copy;* est un assistant robotique qui réalise des plats.

Il y a un certain nombre de recette possible par défaut : 

- Hamburger
- Frites
- Salade
- Pizza
- Sandwich 

## Lexique

Poudre : La poudre est le seul type d'ingrédient non-liquide que l'assistant peut prendre.

<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>
 
<!-- INCLUE
<img
    src="NewTux.svg"
    alt="un triangle aux trois côtés égaux"
    height="87px"
    width="100px" />


END -->


## snippets
``` python
def coucou()
    return 10

```

``` clojure

(defn coucou [] 2)

```

``` csharp

public int coucou() {
    return 42;
}

```

## keys 
++ctrl+alt+delete++





## inlinehilite
Here is some code: `#!py3 import pymdownx; pymdownx.__version__`.

The mock shebang will be treated like text here: ` #!js var test = 0; `.





## superfences
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


## caret
H^2^0

text^a\ superscript^
  

## tilde
~~Delete me~~

CH~3~CH~2~OH

text~a\ subscript~



## emoji 
:smile: :heart: :thumbsup:


## magiclink
- Just paste links directly in the document like this: https://google.com.
- Or even an email address: fake.email@email.com. 



## mark

==mark me==

==smart==mark==



## progress bar  
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





## task list
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











## Arithmatex
`non fonctionnel`


$$
E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
$$

\[3 < 4\]

\begin{align}
    p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
    p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
\end{align}
