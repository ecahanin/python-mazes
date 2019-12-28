import algorithms
import grid


def create():
    columns, rows = input('Enter maze size (columns,rows)').split(',')
    columns = int(columns)
    rows = int(rows)

    
    foo = grid.Grid(columns, rows)

    name = input('Name your maze.')
    filename = name + '.png'

    foo = algorithms.wilsons(foo).to_png(filename)




if __name__ == '__main__':
    while True:
        create()
        done = input('Would you like to create another? Y/n')
        if done.lower() == 'n':
            exit()