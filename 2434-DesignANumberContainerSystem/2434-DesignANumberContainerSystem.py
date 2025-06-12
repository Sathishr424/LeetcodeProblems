# Last updated: 12/6/2025, 5:38:06 am
class NumberContainers:
    def __init__(self):
        self.container = {}
        self.smallest = defaultdict(lambda: {'arr': {}, 'smallest': -1})

    def change(self, index: int, number: int) -> None:
        if index in self.container:
            # remove this index number from self.smallest
            old_number = self.container[index]
            
            del self.smallest[old_number]['arr'][index]
            
            if len(self.smallest[old_number]['arr']) > 0:
                if index == self.smallest[old_number]['smallest']:
                    new_smallest = float('inf')

                    for old_index in self.smallest[old_number]['arr']:
                        new_smallest = min(new_smallest, old_index)
                
                    self.smallest[old_number]['smallest'] = new_smallest
            else:
                self.smallest[old_number]['smallest'] = -1


        self.container[index] = number

        if len(self.smallest[number]['arr']) > 0:
            self.smallest[number]['smallest'] = min(self.smallest[number]['smallest'], index)
        else:
            self.smallest[number]['smallest'] = index
        self.smallest[number]['arr'][index] = 1

    def find(self, number: int) -> int:
        return self.smallest[number]['smallest']


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)