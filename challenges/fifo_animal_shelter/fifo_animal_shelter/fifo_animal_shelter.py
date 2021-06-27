class Animal :
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,name,type):
        """
        Add to the front og the Queue
        """
        new_animal = Animal(name,type)
        if self.front:
            self.rear.next = new_animal
            self.rear = new_animal
        else:
            self.front = new_animal
            self.rear = new_animal


    def dequeue(self,pref):
        """
        Remove the front node from the Queue
        Returns it`s value
        """
        if self.front.type == pref:
        # if self.front == None:
        #     raise AttributeError('Shelter is Empty')
        # else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.name
        else :
            current =self.front
            while self.front.type != pref :
                current = current.next
            return current.name




shelter = AnimalShelter()
shelter.enqueue('spike','dog')
shelter.enqueue('sahsa','cat')
shelter.enqueue('spike2','dog')
shelter.enqueue('cherry','cat')
shelter.dequeue('dog')
print(shelter.front.name)