def define_env(env):
    "Hook function"

    @env.macro
    def image(url, caption=""):
        return "![" + caption + "](" + url + ")"
