test = {   'name': 'q5_3',
    'points': [0, 0, 0, 0],
    'suites': [   {   'cases': [   {'code': '>>> isinstance(precalculus_relative_change, (int, float, np.float, np.float64))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(calculus_relative_change, (int, float, np.float, np.float64))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(multi_relative_change, (int, float, np.float, np.float64))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure your calculations are PERCENTS (0 - 100)\n'
                                               '>>> # not DECIMALS (0 - 1)\n'
                                               '>>> multi_relative_change > calculus_relative_change > precalculus_relative_change > 50\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
