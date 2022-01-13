def define_env(env):
    "Hook function"

    @env.macro
    def image(url, caption="", width_percentage='50'):
        return '<figure style="width: ' + width_percentage + '%" > <img alt="' + caption + '" src="1024.jpg"> <figcaption>' + caption + '</figcaption></figure>'
