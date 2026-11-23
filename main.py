from view import SuspeitoView
from presenter import SuspeitoPresenter


if __name__ == "__main__":
    view = SuspeitoView()
    presenter = SuspeitoPresenter(view)
    view.set_presenter(presenter)
    view.iniciar_loop()