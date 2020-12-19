from tile import Tile


def test_constructor():
    new_tile = Tile(100, 50)
    assert new_tile.x == 100
    assert new_tile.y == 50
