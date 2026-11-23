from model import SuspeitoModel


class SuspeitoPresenter:
    def __init__(self, view, model=None):
        self.view = view
        self.model = model if model else SuspeitoModel()

    def ao_solicitar_cadastro(self, nome, crime, periculosidade):
        try:
            self.model.salvar_suspeito(nome, crime, periculosidade)
            self.view.exibir_sucesso("Suspeito fichado com sucesso no cofre.")
        except ValueError as erro:
            self.view.exibir_erro(str(erro))

    def ao_solicitar_listagem(self):
        dados_brutos = self.model.listar_todos()
        linhas_prontas = []
        for s_id, nome, crime, nivel in dados_brutos:
            tag_risco = "🚨 CRÍTICO" if nivel >= 8 else "⚠️ MONITORADO"
            linhas_prontas.append(
                f"ID #{s_id:02d} | {nome.upper()} | Delito: {crime} | Perigo: {nivel}/10 [{tag_risco}]"
            )
        self.view.mostrar_relatorio(linhas_prontas, len(linhas_prontas))

    def ao_solicitar_remocao(self, suspeito_id):
        try:
            if self.model.deletar_suspeito(suspeito_id):
                self.view.exibir_sucesso("Suspeito removido.")
            else:
                self.view.exibir_erro("ID não encontrado.")
        except ValueError:
            self.view.exibir_erro("O ID deve ser numérico.")
