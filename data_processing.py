import csv
import matplotlib.pyplot as plt
import numpy as np
from math import *


def get_max_distance(vectors: list):
    max_dist = .0
    graph = []
    couple_max = tuple()
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            distance = np.sqrt(sum(pow(a-b, 2) for a, b in zip(vectors[i], vectors[j])))
            graph.append(distance)
            if distance >= max_dist:
                max_dist = distance
                couple_max = (i, j)

    return max_dist, couple_max, graph


def get_min_distance(vectors: list, max_dist: float):
    min_dist = max_dist
    couple_min = tuple()
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            distance = np.sqrt(sum(pow(a-b, 2) for a, b in zip(vectors[i], vectors[j])))
            if distance < min_dist:
                min_dist = distance
                couple_min = (i, j)

    return min_dist, couple_min


def euclidean_distance(vectors: list):
    max_distance, couple_max, graph = get_max_distance(vectors)
    min_distance, couple_min = get_min_distance(vectors, max_distance)
    return max_distance, couple_max, min_distance, couple_min, graph


def csv_reader():
    with open('vectors.csv', 'r') as file:
        vectors = []
        reader = csv.reader(file)
        for line in reader:
            line_vector = []
            for i in line:
                line_vector.append(float(i))
            vectors.append(line_vector)
        return vectors


def histogram(dots, max_dist):
    bins = []
    new_range = [round(x * 0.1, 1) for x in range(round(max_dist) * 10)]
    for i in new_range:
        bins.append(i)
    plt.ylabel('Частота распределений')
    plt.xlabel('Евклидовы расстояния')
    plt.hist(dots, bins=bins)
    plt.title('Распределение расстояний')
    plt.show()
