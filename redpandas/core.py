# -*- coding: utf-8 -*-

import sqlite3

class Database():
    """A container for pandas data frames that writes to SQLite.

    Arguments
    ---------

    frames: (dict) A dictionary where keys are names for the frames and values
    are DataFrames.

    copy: (boolean, default False) Copy input DataFrames.

    """

    def __init__(self, frames=None, copy=False):
        if copy:
            frames = {name: frame.copy() for name, frame in frames}
        self.frames = frames

    @classmethod
    def from_sqlite(filename):
        raise NotImplementedError

    def to_sqlite(self, filename):
        raise NotImplementedError

    def __dir__(self):
        """Override this to allow tab completion of items by key."""
        attributes = dir(self.__class__)
        attributes.append('frames')
        attributes.extend(self.frames.keys())
        return attributes
