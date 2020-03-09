#  File: RPG.py
#  Description: Homework 2 - Creates Weapons, Armor, and RPG characters (Wizard/Fighter) that can engage in combat
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 2/11/19
#  Date Last Modified: 2/11/19

class Weapon:

    #All Weapons must have a type in order to exist; Each type is given its own damage output
    #The default type is "none"
    def __init__(self, WType = "None"):
        self.Type = WType
        if (self.Type == "dagger"):
            self.damage = 4
        elif (self.Type == "axe"):
            self.damage = 6
        elif (self.Type == "staff"):
            self.damage = 6  
        elif (self.Type == "sword"):
            self.damage = 10
        elif (self.Type == "none"):
            self.damage = 1


class Armor:

    #All Armor must have a type in order to exist; Each type is given its own Armor Class (AC)
    #The default type is "none"
    #AC is not really used for anything besides for showmanship
    def __init__(self, AType = "none"):
        self.Type = AType
        if (self.Type == "plate"):
            self.AC = 2
        elif (self.Type == "chain"):
            self.AC = 5
        elif (self.Type == "leather"):
            self.AC = 8  
        elif (self.Type == "none"):
            self.AC = 10

#Generic/Parent Class            
class RPGCharacter:

    #All Characters must have a name in order to exist
    def __init__(self, Name):
        self.NAME = Name                        #All Characters will have a name
        self.WEAPON = Weapon()                  #And a Weapon
        self.ARMOR = Armor()                    #And some Armor
        self.maxHealth = 99                     #And a maxHealth; 99 is a dummy variable to be overwritten
        weaponsAllowed = ['']                   #And a list of weapons able to be equipped; Also to be overwritten
        armorAllowed = ['']                     #And a list of armor able to be equipped; Also to be overwritten
        
    def __str__(self):
        #Prints the name + current status of the Character
        return (
            "\n"
            + self.NAME
            + "\n\tCurrent Health: "
            + str(self.CURRENTHEALTH)
            + "\n\tCurrent Spell Points: " + str(self.Spell_Points)
            + "\n\tWielding: "
            + self.WEAPON.Type
            + "\n\tWearing: "
            + self.ARMOR.Type
            + "\n\tArmor Class: "
            + str(self.ARMOR.AC)
            + "\n\n"
            )

        
    def wield(self, Weapon):
        
        #Equips a new weapon if allowed
        if (Weapon.Type in self.weaponsAllowed):
            print (self.NAME + " is now wielding a(n) " + Weapon.Type)
            self.WEAPON = Weapon
            
        #Shows an error if not allowed
        else:
            print ("Weapon not allowed for this character class.")
        
    def unweild(self):
        
        #Sets weapon to "none"
        print (self.NAME + " is no longer wielding anything")
        self.WEAPON = Weapon()
        
    def putOnArmor(self, Armor):

        #Equips a new armor if allowed
        if (Armor.Type in self.armorAllowed):
            print (self.NAME + " is now wearing " + Armor.Type)
            self.ARMOR = Armor
        #Shows an error if not allowed
        else:
            print ("Armor not allowed for this character class.")

    def takeOffArmor(self):
        
        #Sets armor to "none"
        print (self.NAME + " is no longer wearing anything")
        self.ARMOR = Armor()
        
    def fight(self, OPPONENT):
        #Calculates physical combat

        #self Character causes OPPONENT character to lose health by an amt equal to his weapon's stated damage
        print (self.NAME + " attacks " + OPPONENT.NAME + " with a(n) " + self.WEAPON.Type)
        OPPONENT.CURRENTHEALTH -= self.WEAPON.damage
        print (self.NAME + " does " + str(self.WEAPON.damage) + " damage to " + OPPONENT.NAME)
        #Prints status of opponent's health
        print (OPPONENT.NAME + " is now down to " + str(OPPONENT.CURRENTHEALTH) + " health")
        #Checks if opponent has reached 0 health
        self.checkForDefeat(OPPONENT)

    def checkForDefeat(self, Character):

        #If the character has reached 0 health, state that he's been defeated.
        if (Character.CURRENTHEALTH <= 0):
            print (Character.NAME + " has been defeated!")
        

class Fighter(RPGCharacter):

    #All Fighters have a max health stat of 40 
    maxHealth = 40
    CURRENTHEALTH = maxHealth                                       #All chars start w/ max health at initiation
    Spell_Points = 0                                                #Fighters have no SP
    weaponsAllowed = ["dagger", "axe", "staff", "sword", "none"]    #Fights can equip/wear anything
    armorAllowed = ["plate", "chain", "leather", "none"]

class Wizard (RPGCharacter):

    #All Wizards have a max health stat of 16
    maxHealth = 16
    CURRENTHEALTH = maxHealth                       
    Spell_Points = 20                               #Wizards start w/ 20 SP
    weaponsAllowed = ["dagger", "staff", "none"]    #Wizards can't use axes or swords
    armorAllowed = ["none"]                         #Wizards can't wear armor


    def castSpell(self, SpellName, TARGET):

        #Wizards can also cast spells
        #Fireballs cost 3 SP, but deal 5 dmg
        if (SpellName == "Fireball"):
            cost = 3
            effect = 5

            #If there's not enough SP, don't do any damage/fail-cast and print a relevant error message
            if (cost > self.Spell_Points):
                print ("Insufficient spell points")
                return

            #If there is enough SP, cast the spell on the target and reduce the wizard's SP
            else:
                self.Spell_Points -= cost
                TARGET.CURRENTHEALTH -= effect

                #Dialogue for successful cast - similar to melee battle dialogue
                print (self.NAME + " casts " + SpellName + " at " + TARGET.NAME)
                print (self.NAME + " does " + str(effect) + " damage to " + TARGET.NAME)
                print (TARGET.NAME + " is now down to " + str(TARGET.CURRENTHEALTH) + " health")
                self.checkForDefeat(TARGET)

        #Lightning bolt is basically a fireball, but costs 10 SP and deals 10 dmg
        elif (SpellName == "Lightning Bolt"):
            cost = 10
            effect = 10

            if (cost > self.Spell_Points):
                print ("Insufficient spell points")
                return

            else:
                self.Spell_Points -= cost
                TARGET.CURRENTHEALTH -= effect
                
                print (self.NAME + " casts " + SpellName + " at " + TARGET.NAME)
                print (self.NAME + " does " + str(effect) + " damage to " + TARGET.NAME)
                print (TARGET.NAME + " is now down to " + str(TARGET.CURRENTHEALTH) + " health")
                self.checkForDefeat(TARGET)

        #Heals heal a target, and so increase their health by 6, at the cost of 6 SP
        elif (SpellName == "Heal"):
            cost = 6
            effect = -6

            #If there's not enough SP...
            if (cost > self.Spell_Points):
                print ("Insufficient spell points")
                return

            else:
                self.Spell_Points -= cost
                TARGET.CURRENTHEALTH -= effect

                #Successful heal dialogue 
                print (self.NAME + " casts " + SpellName + " at " + TARGET.NAME)
                print (self.NAME + " heals " + TARGET.NAME + " for " + str(abs(effect)) + " health points.")
                print (TARGET.NAME + " is now at " + str(TARGET.CURRENTHEALTH) + " health")

        #If another spell is attempted, return an error for unknown spell
        else:
            print ("Unknown spell name. Spell failed.")
            return

#Bulko's Test Method
def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
