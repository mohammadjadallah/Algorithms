class BubbleSort:
    """
    This class for sort the array with the algorithm
    Bubble sort
    This algorithm will print the list in ascending order
    if you want to make it in descending order you can make the value of
    reverse_array=False instead of True

    """
    def __init__(self, values):
        self.listValues = values

    def bubble_sort(self, reverse_array=True):
        length_of_array = len(self.listValues)
        i = 0
        j = 0
        while i < length_of_array - 1:
            while j < length_of_array - i - 1:
                if self.listValues[j] > self.listValues[j + 1]:
                    temp = self.listValues[j]
                    self.listValues[j] = self.listValues[j + 1]
                    self.listValues[j + 1] = temp
                    # self.listValues[j], self.listValues[j + 1]  = self.listValues[j + 1], self.listValues[j]

                j = j + 1

            i = i + 1

        # To print list
        if reverse_array:
            return self.listValues
        else:
            return self.listValues[::-1]

    # This will print the object as string not list
    def __repr__(self):
        return f'{self.listValues}'


valuesOfList = [10, 45, 789, 16, 42, 23, 78]
bubble = BubbleSort(valuesOfList)
bubble.bubble_sort()
print(bubble.__doc__)
print(bubble)
print(bubble.bubble_sort(reverse_array=False))
