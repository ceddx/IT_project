from view.menuview import MenuView
from view.gameview import Gameview
from view.historyview import HistoryView
from view.loginview import LoginView
from view.signupview import SignupView
from view.startview import StartView
from view.updateview import UpdateView
from view.savehistoryview import SaveHistoryView
from view.changeorretry_view import ChangeOrRetryView

dict_view = {
        "Start": StartView,
        "Login": LoginView,
        "Menu": MenuView,
        "SignUp": SignupView,
        "History": HistoryView,
        "Update":UpdateView,
        "PlayGame":Gameview,
        "SaveHistory":SaveHistoryView,
        "Update":UpdateView,
        "RetryOrChange":ChangeOrRetryView
    }

if __name__ == "__main__" :
    view = StartView()
    while view != None:
        view.display_info()
        next = view.make_choice()
        if next == "Quit":
            view = None
        else:
            view = dict_view[next]()