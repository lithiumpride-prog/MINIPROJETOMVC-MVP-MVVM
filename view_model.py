
from model import SuspeitoModel


class SuspeitoViewModel:
    def __init__(self, model=None):
        self.model = model if model else SuspeitoModel()
        self._observadores = []

        # Estado Observável (State)
        self.lista_suspeitos = []
        self.total_casos = 0
        self.media_periculosidade = 0.0
        self.status_sistema = "Sistema pronto."

        self.sincronizar_estado(notificar=False)

    def registrar_observador(self, callback):
        """Permite que uma ou mais Views escutem mudanças de estado."""
        self._observadores.append(callback)

    def _notificar(self):
        """Dispara automaticamente a atualização em todas as Views inscritas."""
        for callback in self._observadores:
            callback()

    def sincronizar_estado(self, notificar=True):
        dados = self.model.listar_todos()
        self.lista_suspeitos = [
            f"ID #{s[0]:02d} | {s[1]} | Crime: {s[2]} | Perigo: {s[3]}/10"
            for s in dados
        ]
        self.total_casos = len(dados)
        self.media_periculosidade = (
            sum(s[3] for s in dados) / self.total_casos if self.total_casos > 0 else 0.0
        )
        if self.total_casos > 5:
            self.status_sistema = "🚨 ALERTA MÁXIMO: Mais de 5 casos ativos na investigação!"
        if notificar:
            self._notificar()

    def adicionar_suspeito(self, nome, crime, periculosidade):
        try:
            self.model.salvar_suspeito(nome, crime, periculosidade)
            self.status_sistema = f"✅ Suspeito '{nome}' adicionado ao cofre."
            self.sincronizar_estado(notificar=True)
        except ValueError as erro:
            self.status_sistema = f"❌ Erro: {erro}"
            self._notificar()

    def remover_suspeito(self, suspeito_id):
        try:
            if self.model.deletar_suspeito(suspeito_id):
                self.status_sistema = f"🗑️ Registro #{suspeito_id} removido."
            else:
                self.status_sistema = "⚠️ ID não encontrado."
        except ValueError:
            self.status_sistema = "❌ Erro: ID inválido."
        self.sincronizar_estado(notificar=True)