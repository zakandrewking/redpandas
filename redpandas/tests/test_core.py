# -*- coding: utf-8 -*-

from redpandas.core import Database

import pandas as pd

def test_frame():
    """Return a random DataFrame."""
    return pd.DataFrame(randn(8, 3),
                        columns=pd.Index([('foo', 'bar'), ('baz', 'qux'),
                                          ('peek', 'aboo')], name=['sth', 'sth2']))

def test_Database():
    """Basic Database creation."""
    frames = {key: test_frame(key) for key in ['a', 'b', 'c']}
    db = Database(frames)
    db_copy = Database(frames, copy=True)
    assert db.frames['a']

def test_Database_attribute():
    """Test attribute access."""
    frames = {key: test_frame(key) for key in ['a', 'b', '1c']}
    db = Database(frames)
    assert db.a is frames['a']
    assert db.b is frames['b']
    assert getattr(db, '1c', None) is None
    assert db['1c'] is frames['1c']
