
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Sarah Gale, Googlefu"

import timeit
import cProfile
import pstats
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def inner(src):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(src)
        profiler.disable()

        ps = pstats.Stats(profiler).sort_stats('cumulative')
        ps.print_stats(10)
        return result
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    # title = title.lower()
    # for movie in movies:
    #     if movie.lower() == title.lower():
    #         return True
    # return False
    if title in movies:
        return True
    else:
        return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # bring funct into timer obj
    t = timeit.Timer(
        stmt="find_duplicate_movies('movies.txt')",
        setup="from __main__ import find_duplicate_movies"
    )
    t.unit = 'sec'
    # best time on a per function basis
    result = min(t.repeat(repeat=7, number=3))/3.0
    # print(result)
    print(
        'Best time across 7 repeats of 3 runs per repeat: {:.3f} secs.'.format(result))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    # timeit_helper()
