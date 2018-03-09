import pytest
from main import distance

def test_distance():
    a =[1,0]
    b =[2,2]
    x = distance(a,b)
    assert x == 1
