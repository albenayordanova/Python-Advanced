def fill_the_box(height, length, width, *args):
    box = height * length * width
    cubes = 0
    for el in args:
        if el == 'Finish':
            break
        cubes += el
        if box >= el:
            box -= el
        else:
            cubes -= box
            box = 0

    if box > 0:
        return f'There is free space in the box. You could put {box} more cubes.'
    else:
        return f'No more free space! You have {cubes - box} more cubes.'