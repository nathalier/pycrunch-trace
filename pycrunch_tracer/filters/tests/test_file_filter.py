from pycrunch_tracer import config
from pycrunch_tracer.filters import DefaultFileFilter


def test_included():
    sut = DefaultFileFilter()
    assert sut.should_trace(config.absolute_path)

def test_not_included():
    sut = DefaultFileFilter()
    assert not sut.should_trace('/crap/module/x.py')
