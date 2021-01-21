import pytest
from secret_sharing.encryption import get_terms
from secret_sharing.encryption import polynomial_value
from secret_sharing.encryption import get_points

@pytest.mark.parametrize(["K", "t"],
[    
    (108165236279178312660610114131826512483935470542850824183737259708197206310322, 4),
])

def test_get_terms(K, t):
    terms = get_terms(K, t)
    assert t == len(terms) and terms[0] == K    

@pytest.mark.parametrize(["K", "t"],
[
    (108165236279178312660610114131826512483935470542850824183737259708197206310322, 4),
])    
def test_polynomial_value(K, t):
    terms = get_terms(K, t)
    y = polynomial_value(terms, 0)
    assert y == K
    
@pytest.mark.parametrize(['K', 't', 'n'],
[
    (100, 3, 6),
    (108165236279178312660610114131826512483935470542850824183737259708197206310322, 4, 10)
])
def test_get_points(K, t, n):
    terms = get_terms(K, t)
    points = get_points(n, terms)
    correct = []
    for point in points:
        x = point[0]
        if point[1] == polynomial_value(terms, x):
            correct.append(1)
    assert len(correct) == n
    

    
