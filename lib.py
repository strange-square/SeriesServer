import random


class Series:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.next_ep = 1
        self.raiting = None


class SeriesList:
    def __init__(self):
        self.to_see = set()
        self.watched = set()
        self.names = {}

    def add_series(self, name, size):
        self.names.update([(name, Series(name, int(size)))])

    def add_to_see(self, name):
        if name in self.to_see:
            return "double"
        if name in self.names:
            self.to_see.add(name)
            return "ok"
        else:
            return "not at list"

    def add_watched(self, name):
        if name in self.watched:
            return "double"
        if name in self.names:
            self.watched.add(name)
            return "ok"
        else:
            return "not at list"

    def get_to_see(self):
        return self.to_see

    def get_watched(self):
        return self.watched

    def get_next_ep(self, name):
        if name in self.names:
            return str(self.names[name].next_ep)
        else:
            return "There is no such series"

    def watch_episode(self, name, num):
        if name in self.names:
            if self.names[name].next_ep <= self.names[name].size:
                self.names[name].next_ep += num
            return "ok"
        else:
            return "There is no such series"

    def set_raiting(self, name, raiting):
        if name in self.names:
            self.names[name].raiting = raiting
            return "ok"
        else:
            return "There is no such series"

    def get_raiting(self, name):
        if name in self.names:
            return str(self.names[name].raiting)
        else:
            return "There is no such series"

def generator_series(series):
    try:
        return str(random.choice(list(series.get_to_see())))
    except:
        return ""
