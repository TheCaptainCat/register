from bolinette import Bolinette, Extensions


def create_app():
    return Bolinette().use(Extensions.WEB)
