test = {   'name': 'q2_1',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {   'code': '>>> # Your resample should have the same number of rows as the original sample\n>>> simulate_resample(observations).num_rows\n17',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Your function should work with different sized tables\n'
                                               ">>> simulate_resample(Table().with_column('test data', make_array(1,2,3,4,5)))\n"
                                               'test data\n'
                                               '3\n'
                                               '3\n'
                                               '2\n'
                                               '1\n'
                                               '1',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> simulate_resample(observations).labels[0] == observations.labels[0]\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
