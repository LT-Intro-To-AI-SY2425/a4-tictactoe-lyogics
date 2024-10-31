# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "canis lupis familiaris"
    def __init__(self, n = "no name", a = 0):
        self.name = n
        self.age = a
        self.fetch_count = 0
    
    def __str__(self) -> str:
        s = f"{self.name} is {self.age} years old"
        return s

    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch

    def play_fetch_once(self):
        self.fetch_count += 1
    def reset_fetch(self):
        self.fetch_count = 0

# instances of the Dog class
logan = Dog("logan", 8)
cookie = Dog()
maple = Dog("maple", 1)

print(logan.fetch_count)
# print(cookie)
# print(maple)

logan.play_fetch(4)

print(logan.fetch_count)

logan.play_fetch(8)

print(logan.fetch_count)