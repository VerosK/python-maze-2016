from maze import MazeGame

def main():
    # vytvoříme hru ze souboru
    game = MazeGame.fromString('B  \n  E')
    solution = game.getSolution()
    path_len = solution.length()
    for step,pos in enumerate(solution):
        print("{0}. Step to {1[0]}, {1[1]}".format(step, pos))

if __name__ == '__main__':
    main()

