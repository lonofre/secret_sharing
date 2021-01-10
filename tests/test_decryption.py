import pytest
from secret_sharing.lagrange import interpolation, basis

@pytest.mark.parametrize(["points", "single_point"],
[
    ([(1, 13), (2, 38), (3, 93), (4, 190)], (0,6)),
    ([(3, 2151), (2, 1078), (-8, 9928), (11, 83743), (0, 0)], (1,433)),
    ([(23, 107032831),(9, 6459533),(16, 36105912), (7, 3049551)], (0, 8)),
    ([(30, 103492800),(56, 2280380058),(73, 8516759882),
    (-6, -19188),(23, 27899982), (35, 221794830)], (0, -30))
])
def test_interpolation(points, single_point):
    x, expected = single_point
    assert interpolation(x, points) == expected

@pytest.mark.parametrize(["points", "evaluation" ,"index", "expected"],
[
    ([(1,3),(2,7),(3,8)], 0, 1, -3),
    ([(1,13),(2,38),(3,93),(4,190)], 0, 1, -6)
])
def test_basis(points, evaluation, index, expected):
    assert basis(evaluation, points, index) == expected
