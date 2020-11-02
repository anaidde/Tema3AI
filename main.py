from collections import deque


class ArcConsistency:

    def __init__(self, name): # Constructor
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
            current = queue.popleft()
            if self.__remove_colors(current):
                for neighbour in self.neighbours[current[0]]:
                    queue.append([neighbour, current[0]])

    def __remove_colors(self, current):
        removed = False
        for color in self.colors[current[0]]:
            if color in self.colors[current[1]] and len(self.colors[current[1]]) == 1:
                removed = True
                self.colors[current[0]].remove(color)
        return removed

    def get_result(self):
        self.__get_info()
        self.__arc_consistency()
        print(f'Pentru fisierul " {self.name_file} "')
        ok = False
        for value in self.colors.values():
            if len(value) != 1:
                ok = True
        if ok:
            print("Colorarea este imposibila")
        else:
            print("Colorarea:")
            for key, values in self.colors.items():
                print(f'Culoarea pentru nodul {key} este {values}')


if __name__ == "__main__":
    instanta1 = ArcConsistency('instanta1')
    instanta1.get_result()
    instanta2 = ArcConsistency('instanta2')
    instanta2.get_result()
