def define_env(env):
    "Hook function"

    @env.macro
    def image(url, caption="", width_percentage='50'):
        return '<figure style="width: ' + width_percentage + '%" > <img alt="' + caption + '" src="'+ url +'"> <figcaption><b>' + caption + '</b></figcaption></figure>'

    @env.macro
    def array_to_string(array) :
        result = ""
        for i in array :
            result += i + ", "
        return result[0:-2]  
    
    @env.macro
    def inc(path):
        f = open('docs/' + path, "r")
        return f.read()
  
    refIndex = {}
    refValue = {}
    @env.macro
    def ref(refName, refText=False):
        refIndex[refName] = refIndex.get(refName, 0) + 1
        if (refText):
            refValue[refName] = refText
        return '<a class="ref" id="ref' + refName + str(refIndex[refName]) + '" href="#ref' + refName + '" > [' + refName + '] </a>'

    @env.macro
    def refListing():
        listing = list(refValue.items())
        output = ""
        for (key, value) in listing:
            output += '<span class="key" id="ref' + key + '">[' + key + ']: </span>' 
            output += '<span class="value">' + value + '</span> </br>' + "\n"
        return output

    lexIndex = {}
    lexValue = {}
    @env.macro
    def lex(lexName, lexText=False):
        lexIndex[lexName] = lexIndex.get(lexName, 0) + 1
        if (lexText):
            lexValue[lexName] = lexText
        return '<a class="lex" id="lex' + lexName + str(lexIndex[lexName]) + '" href="#lex' + lexName + '" > [' + lexName + '] </a>'

    @env.macro
    def lexListing():
        listing = list(lexValue.items())
        output = ""
        for (key, value) in listing:
            output += '<span class="key" id="lex' + key + '">[' + key + ']: </span>' 
            output += '<span class="value">' + value + '</span> </br>' + "\n"
        return output

    figValue = {}
    figIndex = {'i': 0}

    @env.macro
    def fig(url, caption="", width_percentage='50'):
        figIndex['i'] += 1
        figValue[figIndex['i']] = caption
        return '<figure id="fig' + str(figIndex['i']) + '" style="width: ' + width_percentage + '%" > <img alt="' + caption + '" src="'+ url +'"> <figcaption> <span class="fig">[Fig ' + str(figIndex['i']) + ']:</span> <b>' + caption + '</b></figcaption></figure>'
    
    @env.macro
    def figRef(index):
        return '<a class="ref" href="#fig' + str(index) + '">Fig ' + str(index) + '</a>'
    
    @env.macro
    def figListing():
        listing = list(figValue.items())
        output = ""
        for (key, value) in listing:
            output += '<a class="key" id="' + 'figListing' + str(key) + '" href="#'+'fig'+str(key)+'">[' + 'Fig ' + str(key) + ']: </a>' 
            output += '<span class="value">[' + value + ']</span> </br>' + "\n"
        return output  