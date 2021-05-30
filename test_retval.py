'''Tests the RetVal class'''

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from retval import ErrExceptionThrown, RetVal, ErrOK, ErrBadValue

def test_setvalue():
	'''Tests setvalue()'''
	
	r = RetVal().set_value('foo','bar')
	assert r['foo'] == 'bar', 'failed to properly set instance value'


def test_set_values():
	'''Tests set_values'''

	r = RetVal().set_values({
		'foo' : 'bar',
		'spam' : 'eggs'
	})
	
	assert r['foo'] == 'bar' and r['spam'] == 'eggs', 'failed to set multiple instance values'


def test_hasvalue():
	'''Tests hasvalue()'''

	r = RetVal()
	
	assert r.set_value('foo','bar'), 'failed to set instance value'
	assert r.has_value('foo'), 'failed to find existing instance value'


def test_error():
	'''Tests set_error() and error()'''
	
	r = RetVal()
	assert r.error() == ErrOK, '''instance not initialized to ErrOK state'''

	r.set_error(ErrBadValue)
	assert r.error() == ErrBadValue, '''instance not set to correct error state'''


def test_count():
	'''Tests count()'''
	
	r = RetVal()
	assert r.count() == 0, '''Unused instance is not empty'''
	
	r['foo'] = 'bar'
	assert r.count() == 1, '''Incorrect item count in instance'''
	
	r.empty()
	assert r.count() == 0, '''Emptied instance is not empty'''


def test_wrap_exception():
	'''Tests the wrap_exception() method'''

	r = RetVal()
	try:
		print(5 / 0)
	except Exception as e:
		r = RetVal().wrap_exception(e)
	
	assert r.error() == ErrExceptionThrown, 'instance has incorrect error code'
	assert r.info(), 'instance has empty info field for exception'
	assert isinstance(r['exception'], ZeroDivisionError), 'instance has wrong exception type'
	assert r['exctype'] == 'ZeroDivisionError', 'instance has wrong exception type string'

if __name__ == '__main__':
	test_wrap_exception()
