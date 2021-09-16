#coding:utf-8

import pickle


class Players:
    def __init__(self, name, level) -> None:
        self.name=name
        self.level=level
    def whoami(self):
        print(f'{self.name} [{self.level}]')

p1=Players('mekki', 10)

print(p1.whoami())