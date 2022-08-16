test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> full_data.num_rows == 562\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Double check the way you are combining the tables.\n'
                                               '>>> # Order is important here (in terms of the arguments)\n'
                                               '>>> # Saying, "except \'Name\' column" is a hint at the\n'
                                               '>>> # order in which you should combine the tables.\n'
                                               ">>> list(full_data.labels)[0] == 'Player'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> full_data.select(sorted(full_data.labels)).sort(4).take(range(3))\n'
                                               '2P   | 3P   | PTS  | Player         | Salary\n'
                                               '0.6  | 0    | 1.7  | Tyler Cook     | 50000\n'
                                               '0    | 0    | 0    | William Howard | 50000\n'
                                               '2    | 0    | 6    | Eric Mika      | 50752',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
