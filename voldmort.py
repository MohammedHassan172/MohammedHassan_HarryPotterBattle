from Wizard import Wizard
# voldmort class inherits from the wizard and add the extra spells
class voldmort(Wizard):
    def __init__(self):
        super().__init__()
        self._spells["Taboo"] = 80
        self._spells["Expulso"] = 60
        self._spells["Confringo"] = 55