class Linked_list:
    def __init__(self, element):
        self.element = element
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def search(self):
        low = 0
        high = len(self.arr) - 1
        while True:
            middle = (low + high) // 2
            if self.arr[middle] == self.element:
                print(f"Listo encontramos el elemento {self.arr[middle]}")
                break
            elif self.arr[middle] < self.element:
                high = middle - 1
            elif self.arr[middle] > self.element:
                low = middle + 1
while True:
    element = int(input("Ingrese elemento del 1 al 11 incluidos: "))
    if 0 < element < 17:
        object_link = Linked_list(element)
        object_link.search()
        break
    else:
        continue