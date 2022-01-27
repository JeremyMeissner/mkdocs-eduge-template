def define_env(env):
    "Hook function"

    @env.macro
    def image(url, caption="", width_percentage='50'):
        return '<figure style="width: ' + width_percentage + '%" > <img alt="' + caption + '" src="'+ url +'"> <figcaption><b>' + caption + '</b></figcaption></figure>'
