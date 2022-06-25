import csv
import numpy


def csv_writer(matrix):
    with open('vectors.csv', 'w') as file:
        writer = csv.writer(file)
        for vector in matrix:
            writer.writerow(vector)


def data_maker(n, m):
    vectors_array = numpy.random.uniform(-1, 1, (n, m))
    return vectors_array


def file_creator(n, m):
    vector_matrix = data_maker(n, m)
    try:
        csv_writer(vector_matrix)
    except Exception as e:
        raise Exception(f'We got some exception: {e}')
