from abc import ABC, abstractmethod

class Stages(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def run(self):
        pass