from Wizard import Wizard
# harry class inherits from the wizard and add the extra spells
class harry(Wizard):
    def __init__(self):
        super().__init__()
        self._spells["Reducto"] = 60
        self._spells["Fiendfyre"] = 50
        self._spells["Nebulus"] = 40