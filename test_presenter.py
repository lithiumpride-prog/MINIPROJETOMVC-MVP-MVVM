import unittest
from model import SuspeitoModel
from presenter import SuspeitoPresenter


class FakeView:
    def __init__(self):
        self.mensagens_sucesso = []
        self.mensagens_erro = []
        self.ultimo_relatorio = []

    def exibir_sucesso(self, msg):
        self.mensagens_sucesso.append(msg)

    def exibir_erro(self, msg):
        self.mensagens_erro.append(msg)

    def mostrar_relatorio(self, linhas, total):
        self.ultimo_relatorio = linhas


class TestSuspeitoPresenter(unittest.TestCase):
    def setUp(self):
        self.fake_view = FakeView()
        self.model_memoria = SuspeitoModel(db_name=":memory:")
        self.presenter = SuspeitoPresenter(self.fake_view, self.model_memoria)

    def test_cadastro_e_classificacao_critica(self):
        self.presenter.ao_solicitar_cadastro("Moriarty", "Conspiração", "9")
        self.assertEqual(len(self.fake_view.mensagens_sucesso), 1)

        self.presenter.ao_solicitar_listagem()
        self.assertIn("🚨 CRÍTICO", self.fake_view.ultimo_relatorio[0])

    def test_bloqueio_periculosidade_invalida(self):
        self.presenter.ao_solicitar_cadastro("Coringa", "Caos", "99")
        self.assertEqual(len(self.fake_view.mensagens_erro), 1)

if __name__ == "__main__":
    unittest.main()

