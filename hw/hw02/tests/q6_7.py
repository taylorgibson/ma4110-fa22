test = {   'name': 'q6_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> # Your table doesn't have all 3 columns\n>>> remaining_inventory.num_columns\n3", 'hidden': False, 'locked': False},
                                   {'code': ">>> # You forgot to subtract off the sales\n>>> remaining_inventory.column('count').item(0) != 45\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> remaining_inventory.where('fruit name', 'grape')\nbox ID | fruit name | count\n57930  | grape      | 162", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
