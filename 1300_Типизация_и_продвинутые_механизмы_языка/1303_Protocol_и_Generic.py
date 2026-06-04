"""
1303_Protocol_и_Generic
"""

def process(stream):
    return stream.read()

class Reader:
    def read(self) -> str:
        return "data"
    
from typing import Protocol

class Readable(Protocol):
    def read(self) -> str: ...
    
def process(stream: Readable) -> str:
    return stream.read()


class FileLike:
    def read(self) -> str:
        return "file data"
    
obj = FileLike()

class Sized(Protocol):
    def size(self) -> int: ...
    
    
def analyze(stream: Readable) -> int:
    data = stream.read()
    return len(data)

class AdvancedStream(Readable, Sized, Protocol):
    pass

from abc import ABC, abstractmethod

class Reader(ABC):
    @abstractmethod
    def read(self) -> str: ...
    
def load_data(source: Readable) -> str:
    return source.read()

f = open('file.txt')
load_data(f)

class Socket:
    def read(self) -> str:
        return "socket data"
    
class Fake:
    def read(self) -> str:
        return "fake data"
    

class Named(Protocol):
    name: str
    
class User:
    def __init__(self, name: str):
        self.name = name
        
        
#from typing import TypeVar
#T = TypeVar('T', bound=Named)

class Resource[T](Protocol[T]):
    def get(self, id: int) -> T: ...    
    
class UserRepository:
    def get(self, id: int) -> User:
        return User("Alice")
    
def load_user(repo: Resource[User], id: int) -> User:
    return repo.get(id)

class Callable(Protocol):
    def __call__(self, x: int) -> int: ...
    
def square(x: int) -> int:
    return x * x

def apply(func: Callable, value: int) -> int:
    return func(value)

class MockDB:
    def get(self, id: int) -> User:
        return User("MockUser")