class Parent:

    def __init__(self, fName, lName, age, gender, height, eyeColor, hairColor, talents1, talents2, talents3): 
        self.fName = fName 
        self.lName = lName 
        self.age = age 
        self.gender = gender 
        self.height = height 
        self.eyeColor = eyeColor 
        self.hairColor = hairColor 
        self.talents1 = talents1 
        self.talents2 = talents2 
        self.talents3 = talents3 

dad = Parent("Bob", "Smith", 40, "Male", 6.9, "brown", "rainbow", "basket ball", "freestyling", "crochet") 

mom = Parent("Linda", "Smith", 28, "female", 4.20, "blue", "green", "tap dancing", "racing", "singing") 

parentz = [mom, dad] 

def greetParents(): 
    for parents in parentz: 
        print("Hello, my name is " + parents.fName + " " +  parents.lName + ". I am " + str(parents.age) + " years old, I have " + parents.eyeColor + " eyes, my height is " + str(parents.height) + ", I have " + parents.hairColor + " colored hair, and " + parents.hairColor + " colored hair. My 3 main talents are " + parents.talents1 + ", " + parents.talents2 + ", and " + parents.talents3) 

greetParents() 

import random 

momTalents = ["Tap dancing", "racing", "singing"]
dadTalents = ["basket ball", "freestyling", "crochet"]
parentThirdTalent = ["Tap dancing", "racing", "singing, basket ball", "freestyling", "crochet"]
parentsGender = ["Female", "Male"]
parentHeight = [4.20, 6.9]
parentEyeColor = ["Blue", "Brown"]
parentHairColor = ["Green", "Rainbow"]

childTalents = random.choice(momTalents) 
childTalents2 = random.choice(dadTalents)
childThirdTalent = random.choice(parentThirdTalent)
childGender = random.choice(parentsGender) 
childHeight = random.choice(parentHeight)  
childEyeColor = random.choice(parentEyeColor) 
childHairColor = random.choice(parentHairColor)  

print("My name is Jesse Smith, I'm a " + childGender + " and I'm good at " + childTalents + ",", childTalents2 + ", and " + childThirdTalent + ". I am " + str(childHeight) + "'', my eyes are colored " + childEyeColor + ", and my hair is colored " + childHairColor + ".")

childTalents = random.choice(momTalents) 
childTalents2 = random.choice(dadTalents)
childThirdTalent = random.choice(parentThirdTalent)
childGender = random.choice(parentsGender) 
childHeight = random.choice(parentHeight)  
childEyeColor = random.choice(parentEyeColor) 
childHairColor = random.choice(parentHairColor) 

print("My name is Charlie Smith, I'm a " + childGender + " and I'm good at " + childTalents + ",", childTalents2 + ", and " + childThirdTalent + ". I am " + str(childHeight) + "'', my eyes are colored " + childEyeColor + ", and my hair is colored " + childHairColor + ".")

childTalents = random.choice(momTalents) 
childTalents2 = random.choice(dadTalents)
childThirdTalent = random.choice(parentThirdTalent)
childGender = random.choice(parentsGender) 
childHeight = random.choice(parentHeight)  
childEyeColor = random.choice(parentEyeColor) 
childHairColor = random.choice(parentHairColor) 

print("My name is Kameran Pat Smith, I'm a " + childGender + " and I'm good at " + childTalents + ",", childTalents2 + ", and Chemistry. " + "I am " + str(childHeight) + "'', my eyes are colored " + childEyeColor + ", and my hair is colored " + childHairColor + ".")

