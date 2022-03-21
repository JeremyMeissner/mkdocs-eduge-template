import os.path

def define_env(env):
    "Hook function"

    @env.macro
    def array_to_string(array):
        result = ""
        for i in array:
            result += i + ", "
        return result[0:-2]

    # global dictionary of listing ref and lex used by genericRef &co
    listingDict = {'refIndex': {}, 'refValue': {}, 'lexIndex': {}, 'lexValue': {}}

    # return an HTML string representing a kind of reference
    # kind (string): 'ref' or 'lex'
    # name (string): the name of the reference
    # desc (string): the description of the generic reference
    def genericRef(kind, name, desc=False):
        # set or increment index
        listingDict[kind+'Index'][name] = listingDict[kind+'Index'].get(name, 0) + 1
        # update description when needed
        if (desc):
            listingDict[kind+'Value'][name] = desc
        # Return HTML reference with visual like "[name]"
        return ('<a class="ref" id="'+kind+name+str(listingDict[kind+'Index'][name])+'" ' +
                'href="#'+kind+name+'"> ['+name+'] </a>')

    # return an HTML string representing the listing of a kind of reference (without title)
    # that does not contain link to places where it was used (in contrary of figListing)
    # kind (string): 'ref' or 'lex'
    def genericListing(kind):
        # sorted pair of reference's name and description
        listing = sorted(list(listingDict[kind+'Value'].items()))
        output = ""
        # accumulate HTML output with visual like:
        # [name1]: description1 ...
        # [name2]: description2 ...
        # ...
        for (name, desc) in listing:
            output += '<p> <span class="key" id="ref' + name + '">[' + name + ']: </span>'
            output += '<span class="value">' + desc + '</span> </p>' + "\n"
        return output

    # allows user to create a reference with an description or to refer to a reference
    @env.macro
    def ref(name, desc=False):
        return genericRef('ref', name, desc)

    # allows user to create a reference's listing without the title
    @env.macro
    def refListing():
        return genericListing('ref')

    # allows user to create a lexic with an explanation or to refer to a lexic
    @env.macro
    def lex(name, desc=False):
        return genericRef('lex', name, desc)

    # allows user to create a lexic's listing without the title
    @env.macro
    def lexListing():
        return genericListing('lex')

    # global vars for managing figures
    figValue = {}
    figIndex = {'i': 0}

    # allows the user to output an HTML figure
    # converting svg files to png when detected
    # path (string): relative path of picture (starting at folder docs of this mkdocs template)
    # caption (string): caption of figure
    # widthPercentage (int from 0 to 100): percentage of picture's width filling the page
    @env.macro
    def fig(path, caption="", widthPercentage=50):
        # increment index of figures and update the caption
        figIndex['i'] += 1
        figValue[figIndex['i']] = caption
        # return a figure as a picture with caption
        return ('<figure id="fig' + str(figIndex['i']) +
                '" style="width: ' + str(int(widthPercentage)) + '%" >' + "\n" +
                '<img width="100%" alt="' + caption + '" src="../' + path + '">' + "\n" +
                '<figcaption>' + "\n" +
                '<span class="fig">[Fig ' + str(figIndex['i']) + ']:</span>' +
                '<b>' + caption + '</b> </figcaption>'+"\n" +
                '</figure>')

   # allows the user to output an HTML reference to figure
    @env.macro
    def figRef(index=False,increment=0):
        if (index is False):
            index = figIndex['i']
        index = index + increment
        # HTML visual like "[Fig n]"
        return '<a class="ref" href="#fig' + str(index) + '">[Fig ' + str(index) + ']</a>'

    # allows the user to output an HTML listing of figures (without title)
    @env.macro
    def figListing():
        # sorted listing
        listing = sorted(list(figValue.items()))
        output = ""
        # accumulate HTML output with visual like:
        # [Fig 1]: caption1 ...
        # [Fig 2]: caption2 ...
        # ...
        for (key, value) in listing:
            output += '<p> <a class="key" id="' + 'figListing' + \
                str(key) + '" href="#'+'fig'+str(key)+'">[' + 'Fig ' + str(key) + ']: </a>'
            output += '<span class="value">' + value + '</span> </p>' + "\n"
        return output


    @env.macro
    def src(path,lang="", useTitle=True):
        f = open('docs/' + path, "r")
        options = ' ' + lang + ' linenums="1" '
        if useTitle:
            options = options + 'title="' + os.path.basename(path) + '"'
        return ("```" + options + "\n"
                + f.read()
                + "\n" + '```' + "\n")
    # add macro to Jinja2 macros (before markdown processing)
    env.variables['src'] = src

    # Il faut utiliser {% include 'fichier.md' %} 
    # si on souhaite inserer des fichiers (pour que nos macros puissent etre utilisés sur le fichier inclu)
    # @env.macro
    # def inc(path):
    #     f = open('docs/' + path, "r")
    #     return f.read()
    # # add macro to Jinja2 macros (before markdown processing)
    # env.variables['inc'] = inc

# def on_pre_page_macros(env):
#     "Hook function before markdown directives"

#        # Need test
