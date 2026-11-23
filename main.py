from view_model import SuspeitoViewModel
from view import SuspeitoView
from log_view import LogAuditoriaView


if __name__ == "__main__":
    vm = SuspeitoViewModel()
    view_principal = SuspeitoView(vm)
    view_auditoria = LogAuditoriaView(vm)

    view_principal.iniciar()