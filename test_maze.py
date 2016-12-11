
from maze import MazeGame, MazePath, MazeError
import pytest

# Valid mazes
MICRO_MAZE = '''B   E'''

SMALL_MAZE = '''
##########
#        #
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

@pytest.mark.parametrize(
    'data,width,height', [
        (MICRO_MAZE, 5, 1),
        (SMALL_MAZE, 10, 5),
        (LARGE_MAZE, 27, 15),
        (DEAD_END_MAZE, 10, 5)
    ])
def test_create_from_string(data, width, height):
    "Test creation from string"
    game = MazeGame.fromString(data)
    assert game is not None
    assert type(game) is MazeGame
    assert game.getSize() == (width, height)


NO_DATA = "\n"
NO_START = '#  E#'
NO_END = '''
#####
#B  #
#####
'''
TWO_STARTS = "#BEB#"
MORE_ENDS = "#EEEE ##B"

@pytest.mark.parametrize(
    'data', [NO_DATA, NO_START, NO_END, TWO_STARTS, MORE_ENDS])
def test_create_invalid_from_string(data):
    "Invalid input should raise exception"
    with pytest.raises(MazeError):
        game = MazeGame.fromString(data)

@pytest.mark.parametrize('data',
        [MICRO_MAZE, SMALL_MAZE, LARGE_MAZE])
def test_can_pass(data):
    "Test solution exists"
    game = MazeGame.fromString(data)
    solution = game.getSolution()
    assert type(solution) is MazePath
    solution_length = solution.length()
    assert solution_length > 1

@pytest.mark.parametrize(
    'maze,expected_length',
    [
        (MICRO_MAZE, 5),
        (SMALL_MAZE, 12),
        (LARGE_MAZE, 49),
    ])
def test_length_validity(maze, expected_length):
    "Test solution length & validity"
    game = MazeGame.fromString(maze)
    solution = game.getSolution()
    assert type(solution) is MazePath
    solution_length = solution.length()
    assert solution_length == expected_length
    #
    last_x,last_y = None,None
    start_position = game.getStart()
    end_position = game.getEnd()
    for x,y in solution:
        if last_x is None:
            assert (x,y) == start_position
        else:
            step_length = abs(last_x-x) + abs(last_y-y)
            assert step_length == 1
        last_x,last_y = x,y
    assert (last_x,last_y) == end_position


@pytest.mark.parametrize('data', [DEAD_END_MAZE])
def test_cant_pass(data):
    "Test maze with no solution"
    game = MazeGame.fromString(data)

    with pytest.raises(MazeError):
        solution = game.getSolution()
