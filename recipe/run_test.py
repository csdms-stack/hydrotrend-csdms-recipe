#! /usr/bin/env python
import os

os.mkdir('_testing')
os.chdir('_testing')

from pymt.babel import setup_babel_environ

setup_babel_environ()
print(os.environ)

try:
    print('import csdms')
    import csdms
except ImportError:
    raise
else:
    print(csdms.__path__[0])

try:
    print('import csdms.Hydrotrend')
    import csdms.Hydrotrend
except ImportError:
    print('contents of {dir}:'.format(dir=csdms.__path__[0]))
    for fn in os.listdir(csdms.__path__[0]):
        print('- {fn}'.format(fn=fn))
    raise
else:
    print(csdms.Hydrotrend.Hydrotrend())

try:
    print('from pymt.components import Hydrotrend')
    from pymt.components import Hydrotrend
except ImportError:
    raise
else:
    ht = Hydrotrend()

for default in ht.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1][0], units=default[1][1]))
