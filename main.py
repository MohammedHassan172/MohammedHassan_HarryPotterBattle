from harry import harry
from voldmort import voldmort

if __name__ == '__main__':
    # creating the wizards
    harry1 = harry()
    voldmort1=voldmort()
    # loop until one of them is dead
    while not (harry1.isdead()) and not(voldmort1.isdead()):
        print("Enter the two spells(harry then voldmort)")
        # take the spells
        Harry_Spell, Voldmort_Spell = input().split(" ")
        # saves the spells to search for them in the dictionary
        Harry_Spell_Power = harry1.energy_sheild_dec(Harry_Spell)
        Voldmort_Spell_Power = voldmort1.energy_sheild_dec(Voldmort_Spell)
        # decide which one to be damaged
        if Harry_Spell_Power > Voldmort_Spell_Power:
            voldmort1.health_dec(Harry_Spell_Power, Voldmort_Spell_Power)
        else:
            harry1.health_dec(Voldmort_Spell_Power, Harry_Spell_Power)
        # print the result of the spells
        print("\t","  Harry","\t\t","Voltmort")
        print("Health :",harry1.show_health(),"         ",voldmort1.show_health())
        print("Energy :",harry1.show_energy(),"         ",voldmort1.show_energy())
    # finally check which one is dead
    if harry1.isdead() and not(voldmort1.isdead()):
        print("\t","Voldemort is the winner!")
    # if both of them ran out of energy at the same time
    elif harry1.isdead() and voldmort1.isdead():
        print("No body won!")
    else:
        print("\t","Harry is the winner!")