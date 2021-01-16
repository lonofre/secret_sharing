import pytest
from secret_sharing.lagrange import Lagrange
from secret_sharing.decryption import decrypt

prime = 208351617316091241234326746312124448251235562226470491514186331217050270460481

@pytest.mark.parametrize(["points", "single_point"],
[
    ([(1, 13), (2, 38), (3, 93), (4, 190)], (0,6)),
    ([(3, 2151), (2, 1078), (-8, 9928), (11, 83743), (0, 0)], (1,433)),
    ([(23, 107032831),(9, 6459533),(16, 36105912), (7, 3049551)], (0, 8)),
    ([(7, 26376330922020999534938862460707141553067266641573305170045544756114590441911),
    (12, 26376330922020999534938862460707141553067266641573305170046166714623772042731),
    (42, 26376330922020999534938862460707141553067266641573305170057816861817436296651),
    (9, 26376330922020999534938862460707141553067266641573305170045752532979986042979)], 
    (0, 26376330922020999534938862460707141553067266641573305170045231911149830907963)),
])
def test_interpolation(points, single_point):
    lagrange = Lagrange(prime)
    x, expected = single_point
    assert lagrange.interpolation(x, points) == expected

@pytest.mark.parametrize(["points", "mod", "evaluation" ,"index", "expected"],
[
    ([(1,3),(2,7),(3,8)], 11, 0, 1, 8),
    ([(1,13),(2,38),(3,93),(4,190)], 13, 0, 0, 4)
])
def test_basis(points, mod, evaluation, index, expected):
    lagrange = Lagrange(mod)
    assert (lagrange.basis(evaluation, points, index) % mod ) == expected

@pytest.mark.parametrize(["message", "points", "expected"],
[
    (b'\x85\xa6\xcb\x8e\xf5*j\xcca)\x94\xc8A\x82\x0bj\x1f(!i\x0f\x0f\xab\xb0',
    [(7, 26376330922020999534938862460707141553067266641573305170045544756114590441911),
    (12, 26376330922020999534938862460707141553067266641573305170046166714623772042731),
    (42, 26376330922020999534938862460707141553067266641573305170057816861817436296651),
    (9, 26376330922020999534938862460707141553067266641573305170045752532979986042979)],
    b'a 500...'),
])
def test_decryption(message, points, expected):
    result = decrypt(message, points)
    assert result.decode('utf-8') == expected.decode('utf-8')
    
