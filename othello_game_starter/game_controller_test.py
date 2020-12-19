from game_controller import GameController


def test_constructor():
    gc = GameController(200, 100)
    assert gc.WIDTH == 200
    assert gc.HEIGHT == 100
    assert gc.FILE_NAME == "scores.txt"
    assert gc.black_wins is False
    assert gc.white_wins is False
    assert gc.game_ends is False
    assert gc.tie is False
    assert gc.player_name is False
    assert gc.num == 0
    assert gc.black == 0
