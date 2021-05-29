'''Tests the RetVal class'''

from retval.retval import RetVal, ErrOK, ErrBadParameterValue

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

	r.set_error(ErrBadParameterValue)
	assert r.error() == ErrBadParameterValue, '''instance not set to correct error state'''


def test_count():
	'''Tests count()'''
	
	r = RetVal()
	assert r.count() == 0, '''Unused instance is not empty'''
	
	r['foo'] = 'bar'
	assert r.count() == 1, '''Incorrect item count in instance'''
	
	r.empty()
	assert r.count() == 0, '''Emptied instance is not empty'''
