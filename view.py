class SuspeitoView:
    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def exibir_sucesso(self, mensagem):
        print(f"\n[OK] {mensagem}")

    def exibir_erro(self, mensagem):
        print(f"\n[ERRO] {mensagem}")

    def mostrar_relatorio(self, linhas_formatadas, total):
        print("\n--- 📋 RELATÓRIO DE INVESTIGAÇÃO (MVP) ---")
        if not linhas_formatadas:
            print("Nenhum suspeito cadastrado.")
        else:
            for linha in linhas_formatadas:
                print(linha)
        print(f"--- Total de registros: {total} ---")

    def iniciar_loop(self):
        while True:
            print("\n1. Adicionar Suspeito | 2. Listar Todos | 3. Remover por ID | 0. Sair")
            op = input("Escolha: ")
            if op == '1':
                nome = input("Nome: ")
                crime = input("Crime: ")
                nivel = input("Periculosidade (1-10): ")
                self.presenter.ao_solicitar_cadastro(nome, crime, nivel)
            elif op == '2':
                self.presenter.ao_solicitar_listagem()
            elif op == '3':
                suspeito_id = input("ID para remoção: ")
                self.presenter.ao_solicitar_remocao(suspeito_id)
            elif op == '0':
                print("Encerrando MVP...")
                break
            else:
                self.exibir_erro("Comando inválido.")