class Wizard:
    # this is the main class for both(harry and voltmort)
    # here i put the info shared between the two
    def __init__(self):
        self._health = 100
        self._energy = 500
        self._sheild = 4
        # a boolean to indicate if the wizard is dead or (out of energy)
        self._Isdead = False
        self._spells = {
            "AvadaKedavra": 100,
            "Crucio": 40,
            "Imperio": 20,
            "sheild": 0
        }

    # to decrease the energy and the sheild if used
    def energy_sheild_dec(self, spell):
        # get the power of the spell
        energy = self._spells.get(spell)
        # if the wizard's energy is more than the spell energy decrease normally
        if self._energy >= energy:
            self._energy = self._energy - energy
        # if it is not set the spell energy to -1(for not able to use the spell)
        else:
            # self._energy = 0
            energy = -1

        if self._energy == 0:
            self._Isdead = True
        # decrease the sheild
        if energy == 0 and self._sheild != 0:
            self._sheild = self._sheild - 1
        return energy

    # to decrease the health if the sheild is not used or the limit is met
    def health_dec(self, high_e, low_e):
        if low_e == -1 and self._health > (high_e - (low_e+1)):
            self._health = self._health - (high_e - (low_e+1))
        elif (low_e != 0 and self._health >= (high_e - low_e)) or self._sheild == 0:
            self._health = self._health - (high_e - low_e)
        # if the wizard's health was smaller than the the spell power set the health to 0
        elif (low_e != 0 and self._health < (high_e - low_e)) or self._sheild == 0:
            self._health = 0
        if self._health == 0:
            self._Isdead = True
    # just to show the health,energy and the state of the wizard {
    def show_health(self):
        return self._health

    def show_energy(self):
        return self._energy

    def isdead(self):
        return self._Isdead
    # }