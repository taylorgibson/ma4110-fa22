test = {   'name': 'q1_5',
    'points': [0, 0],
    'suites': [   {   'cases': [   {'code': '>>> type(simulate()) == int\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> # It looks like your simulation isn't random\n>>> np.std([simulate() for _ in range(1000)]) > 0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
