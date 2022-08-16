test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # You either didn't add the 'Total Pay ($)' column,\n>>> # or you mislabeled it.\n>>> 'Total Pay ($)' in compensation.labels\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # You have the column in your table,\n'
                                               '>>> # but your values may be wrong.\n'
                                               ">>> t = compensation.sort('Total Pay ($)', descending = True)\n"
                                               ">>> t.column('Total Pay ($)').item(0)\n"
                                               '26039213.0',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
