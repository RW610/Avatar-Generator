from utils import *


def generate_images(size, number):
    folder_name = f'avatars/avatars{size}x{size}'
    filename = f'{folder_name}/avatar.png'
    create_folder(folder_name)

    img_size = (size + 1) * 100

    for _ in range(number):
        matrix = random_matrix(size, size)
        squares = gen_squares(matrix, img_size)
        new_filename = get_new_filename(filename)
        visualize_squares(squares, img_size, new_filename)


def main(sizes, number):
    if isinstance(sizes, int):
        size_range = (sizes, sizes + 1)
    else:
        size_range = sizes

    for i in range(*size_range):
        generate_images(i, number)


sizes = 7
number = 10

main(sizes, number)
