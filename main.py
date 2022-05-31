import csv

class Animal:
    def __init__(self,list):
        self.name=list[0]
        self.age=list[1]
        self.breed=list[2]
    
    def get_info(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

def find_animal():
    animal=input("Which type of animal are you interested in adopting?")
    animal_list=[]   

    if animal.lower()=="dog" or animal.lower()=="dogs":
        with open('data/dogs.csv', newline="") as csvfile:
            dogreader= csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in dogreader:
                animal_list.append(row)
                

    elif animal.lower()=="cat" or animal.lower()=="cats":
        with open('data/cats.csv', newline="") as csvfile:
            catreader= csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in catreader:
                animal_list.append(row)

    else:
        return f"Sorry we don't have any {animal}'s here"

    answer=f"These are the {animal}'s we have available for adoption: "

    for i, animal in enumerate(animal_list[1:]):
        x=Animal(animal)
        if i!= (len(animal_list[1:])-1):
            answer+=f"{x.get_info()}, "
        else:
            answer+=f"{x.get_info()}."

    return answer

    

print(find_animal())

