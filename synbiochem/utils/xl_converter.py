'''
SYNBIOCHEM-DB (c) University of Manchester 2017

SYNBIOCHEM-DB is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import os
import sys

import pandas as pd
import xlrd


def convert(xl_filename):
    '''Convert Excel file.'''
    dir_name, _ = os.path.splitext(xl_filename)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    workbook = xlrd.open_workbook(xl_filename)

    for sheet in workbook.sheets():
        columns = None
        data = []

        for row_num in xrange(sheet.nrows):
            row_data = sheet.row_values(row_num)
            if not columns:
                columns = row_data
            else:
                data.append(row_data)

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(os.path.join(dir_name, sheet.name + '.csv'),
                  index=False,
                  encoding='utf-8')

    return dir_name


def main(args):
    '''main method.'''
    print convert(args[0])


if __name__ == '__main__':
    main(sys.argv[1:])
