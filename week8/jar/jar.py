class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Jar is full")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        counter = 0
        return_str = ""
        while counter < self.size:
            return_str = return_str + "🍪"
            counter += 1
        return return_str


    def deposit(self, n):
        self.size += n
        if self.size > 12:
            raise ValueError("Jar is full")


    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Jar is empty")

    #Getter
    @property
    def capacity(self):
        return self._capacity

    #Setter
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    #Getter
    @property
    def size(self):
        return self._size

    #Setter
    @size.setter
    def size(self, size):
        self._size = size

def main():
    num_cookies = int(input("Input Number of Cookies: "))
    jar = Jar()
    jar.withdraw(num_cookies)
    print(jar)


if __name__ == "__main__":
    main()
