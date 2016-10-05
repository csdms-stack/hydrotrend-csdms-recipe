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
    print(csdms.__path__)

try:
    print('import csdms.Hydrotrend')
    import csdms.Hydrotrend
except ImportError:
    print(os.listdir(csdms.__path__))
    raise
else:
    print(Hydrotrend())

try:
    print('from pymt.components import Hydrotrend')
    from pymt.components import Hydrotrend
except ImportError:
    raise
else:
    ht = Hydrotrend()

for default in ht.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1], units=val[2]))
