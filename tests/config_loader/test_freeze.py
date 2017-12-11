import os.path

import pytest

import config_loader


mutable_dict = {
    'list': ['foo', 'foo', 'bar'],
    'set': {'foo', 'bar'},
    'tuple': ('foo', 'foo', 'bar')
}


def test_freeze():
    # language=rst
    """Freeze something complex and mutable."""
    FROZEN = config_loader.freeze(mutable_dict)
    assert len(FROZEN) == len(mutable_dict)
    for k in mutable_dict:
        assert k in FROZEN
    with pytest.raises(TypeError):
        FROZEN['foo'] = 'bar'

    l = FROZEN['list']
    assert len(l) == len(mutable_dict['list'])
    assert l.count('foo') == 2
    assert l.count('bar') == 1
    with pytest.raises(AttributeError):
        l.append('bar')

    s = FROZEN['set']
    assert len(s) == len(mutable_dict['set'])
    for k in mutable_dict['set']:
        assert k in s
    with pytest.raises(AttributeError):
        s.add('bar')

    t = FROZEN['tuple']
    assert len(t) == len(mutable_dict['tuple'])
    assert t.count('foo') == 2
    assert t.count('bar') == 1
    with pytest.raises(AttributeError):
        t.append('bar')

    assert FROZEN['tuple'] == mutable_dict['tuple']
