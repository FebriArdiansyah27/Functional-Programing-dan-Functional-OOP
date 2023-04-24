# Membuat kelas "Person"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(
            f"Hallo, nama saya {self.name} dan saya berusia {self.age} tahun.")
        return


# Membuat objek "person1"
person1 = Person("M. Febri Ardiansyah", 19)
person2 = Person("Anny", 23)

# Memanggil metode "greet" pada objek "person1"
person1.greet()
person2.greet()
