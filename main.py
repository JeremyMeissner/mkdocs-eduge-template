def define_env(env):
    "Hook function"

    @env.macro
<<<<<<< HEAD
    def image(url, pWidth, caption="" ):
        return "![" + caption + "](" + url + "){: style=\"widht:" +  pWidth +"px\"}"
=======
    def image(url, caption="", width_percentage='50'):
        return '<figure style="width: ' + width_percentage + '%" > <img alt="' + caption + '" src="1024.jpg"> <figcaption>' + caption + '</figcaption></figure>'
>>>>>>> 9f17f6fa79a250a9f7f6db9e32eb3eaf9000febb
