class SuspeitoView:
    def __init__(self, view_model):
        self.vm = view_model
        # Data Binding simulado: a View se inscreve para reagir às mudanças do VM
        self.vm.registrar_observador(self.renderizar)

    def renderizar(self):
        """Desenha o painel automaticamente sempre que o estado do ViewModel muda."""
        print("\n" + "=" * 55)
        print(f"🛰️  PAINEL REATIVO MVVM | Casos: {self.vm.total_casos} | Risco Médio: {self.vm.media_periculosidade:.1f}/10")
        print("=" * 55)
        if not self.vm.lista_suspeitos:
            print("  (Nenhum suspeito registrado)")
        else:
            for item in self.vm.lista_suspeitos:
                print(f"  • {item}")
        print("-" * 55)
        print(f"[STATUS]: {self.vm.status_sistema}")
        print("=" * 55)

    def iniciar(self):
        self.renderizar()  # Renderização inicial
        while True:
            print("\n1. Novo Registro | 2. Remover por ID | 0. Sair")
            op = input("Comando: ")
            if op == '1':
                nome = input("Nome: ")
                crime = input("Crime: ")
                nivel = input("Periculosidade (1-10): ")
                # Alteramos APENAS o ViewModel; a View se atualiza sozinha!
                self.vm.adicionar_suspeito(nome, crime, nivel)
            elif op == '2':
                suspeito_id = input("ID para remover: ")
                self.vm.remover_suspeito(suspeito_id)
            elif op == '0':
                print("Desligando painel...")
                break