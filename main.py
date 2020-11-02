from collections import deque


class ArcConsistency:

    def __init__(self, name):
        self.colors = dict()
        self.neighbours = dict()
        self.name_file = name

    def __get_info(self):
        file = open(self.name_file, 'r')
        for i in file.readlines():
            info = i.split(':')
            data = info[1].split(';')
            self.neighbours[info[0]] = list(data[0].replace('{', '').replace('}', '').replace(' ', '').split(','))
            self.colors[info[0]] = list(data[1].rstrip().replace('{', '').replace('}', '').replace(' ', '').split(','))

    def __get_queue(self):
        data = deque()
        for key, values in self.neighbours.items():
            for value in values:
                data.append([key, value])
        return data

    def __arc_consistency(self):
        queue = self.__get_queue()
        while len(queue) > 0:
            actual = queue.popleft()
            if self.__rm_icons_values(actual):
                for neighbour in self.neighbours[actual[0]]:
                    queue.append([neighbour, actual[0]])

    def __rm_icons_values(self, actual):
        removed = False
        for color in self.colors[actual[0]]:
            if color in self.colors[actual[1]] and len(self.colors[actual[1]]) == 1:
                removed = True
                self.colors[actual[0]].remove(color)
        return removed

    def get_result(self):
        self.__get_info()
        self.__arc_consistency()
        print(f'For the file " {self.name_file} "')
        ok = False
        for value in self.colors.values():
            if len(value) != 1:
                ok = True
        if ok:
            print("The coloring is impossible using this algorithm.")
        else:
            print("The coloring is the following---->")
            for key, values in self.colors.items():
                print(f'The color of the {key} is {values}')


if __name__ == "__main__":
    instanta1 = ArcConsistency('instanta1')
    instanta1.get_result()
    instanta2 = ArcConsistency('instanta2')
    instanta2.get_result()
