class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._name = name
        self._house = house

        def __str__(self):
            return f"{self.name} from {self.house}"

        @classmethod
        def get(cls):
            name = input("Name: ")
            house = input("House: ")
            return cls(name, house)

def main():
    student = Student.get()
    print(student) 

if __name__ == "__main__":
    main()
