from random import randint
from PIL import Image, ImageDraw
import os


def random_matrix(height, width):

    matrix = [0 for _ in range(width)]
    matrix = [matrix.copy() for _ in range(height)]

    for h in range(height):
        for w in range(width):
            if w < width / 2:
                matrix[h][w] = randint(0, 1)
            else:
                matrix[h][w] = matrix[h][width - w - 1]

    return matrix


def gen_squares(mtx, size=600):

    cell = size // ((len(mtx) + 1) * 2)
    squares = []

    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if mtx[i][j]:
                x = j * cell * 2 + cell
                y = i * cell * 2 + cell
                squares.append([(x, y), (x + cell * 2, y + cell * 2)])

    return squares


def visualize_squares(squares, avasize=600, filename='avatars/avatar.png'):

    color = tuple([randint(0, 255) for _ in range(4)])
    image = Image.new('RGB', (avasize, avasize), color='white')
    draw = ImageDraw.Draw(image)

    for square in squares:
        draw.rectangle(square, outline=color, fill=color)

    image.save(filename)

    # image.show()


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def get_new_filename(filename):
    base, extension = os.path.splitext(filename)
    suffix = 0
    while os.path.exists(f"{base}_{suffix}{extension}"):
        suffix += 1

    new_filename = f"{base}_{suffix}{extension}"
    return new_filename


if __name__ == '__main__':
    pass
