from mural_app.app import mensagem_boas_vindas


def test_mensagem_boas_vindas():
    assert mensagem_boas_vindas() == {
        "esquadrao": "Bem vindo!",
        "status": "Online",
    }
