from tiles import Tiles


def test_constructor():
    table = [[1, 2]]
    new_tiles = Tiles(100, table)
    assert new_tiles.GRID == 100
    assert new_tiles.table == table
    assert new_tiles.centre == 50
