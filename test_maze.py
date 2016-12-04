
from maze import MazeGame, MazePath, MazeError
import pytest

MICRO_MAZE = '''B   E'''

SMALL_MAZE = '''
##########
#    #   #
#  # # # #
#B #   #E#
##########
'''

LARGE_MAZE = '''
###########################
#B#             #      #  #
# #                #  #   #
# #           #    #   #  #
# #          #     #  #   #
# #         # #    #   #  #
# #        #  #    #  #   #
#         #   #    #   #  #
# #      #    #    #  #   #
# #     #          #   #  #
# #    #           #  #   #
# #   #            #   #  #
# #  #             #  #   #
#   #              #     E#
###########################
'''

DEAD_END_MAZE = '''
##########
B   #    #
#   #    #
#   #    E
##########
'''

@pytest.mark.parametrize('data',
        [MICRO_MAZE, SMALL_MAZE, LARGE_MAZE, DEAD_END_MAZE])
def test_create_from_string(data):
    "Test creation from string"
    game = MazeGame.fromString(data)
    assert game is not None
    assert type(game) is MazeGame
    
@pytest.mark.parametrize('data',
        [MICRO_MAZE, SMALL_MAZE, LARGE_MAZE])
def test_can_pass(data):
    "Test solution"
    game = MazeGame.fromString(data)
    solution = game.getSolution()
    assert type(solution) is MazePath
    assert solution.length() > 1

@pytest.mark.parametrize('data', [DEAD_END_MAZE])
def test_cant_pass(data):
    "Test maze with no solution"
    game = MazeGame.fromString(data)

    with pytest.raises(MazeError):
        solution = game.getSolution()
    
