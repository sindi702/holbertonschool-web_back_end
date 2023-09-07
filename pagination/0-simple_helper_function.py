#!/usr/bin/env python3
"""Simpler helper function"""


def index_range(page, page_size):
    ''' index range fun'''
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
