from datetime import datetime
import os

class LogAuditoriaView:
    def __init__(self, view_model, nome_arquivo="auditoria.log"):
        self.vm = view_model
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)
        self.vm.registrar_observador(self.registrar_log)

    def registrar_log(self):
        """Grava no arquivo de log sempre que o estado do ViewModel muda."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linha = (
            f"[{timestamp}] "
            f"Status: {self.vm.status_sistema} | "
            f"Casos: {self.vm.total_casos} | "
            f"Risco Médio: {self.vm.media_periculosidade:.1f}/10\n"
        )
        with open(self.caminho_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)