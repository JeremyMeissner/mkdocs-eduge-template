def define_env(env):
    "Hook function"

    @env.macro
    def image(url, pWidth, caption="" ):
        return "![" + caption + "](" + url + "){: style=\"widht:" +  pWidth +"px\"}"
