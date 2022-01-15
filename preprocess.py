import pandas as pd 
from glob import glob
import consts as c
import mysql.connector
import mysql_utils as ms
import queries as q
import logging
import csv
import argparse

    

def main():

    parser = argparse.ArgumentParser()
    # parser.add_argument('--db', default=c.DB)
    # create complete database or selected database
    parser.add_argument('--reduced', default=True, type=lambda x: (str(x).lower() == 'true'))
    args = parser.parse_args()

    log = logging.getLogger('edtoday')
    logfmt = '%(asctime)s %(name)-12s: %(levelname)-8s %(message)s'
    logging.basicConfig(
    level=logging.DEBUG,
    format=logfmt, 
    datefmt='%Y-%m-%d %H:%M',
    handlers=[
        logging.FileHandler(filename=f'create_mysql_db2.log', mode='a'), # mode='w+' overwrite 'a' append 
        logging.StreamHandler()
    ])

    log.info('creating database and tables ...')

    if args.reduced:
        ms.create_schema(q.CREATE_TABLES_REDUCED)
    else:
        ms.create_schema(q.CREATE_TABLES)

    # files = glob(c.DATA)

    for file in c.FILES:
        idx = 0
        # name = file.split('/')[-1].split('.')[0]
        file_path = c.DATA + file + '.txt'
        
        for data in pd.read_csv(file_path, delimiter='\t', names=c.SCHEMA[file]['cols'], chunksize=c.SCHEMA[file]['size'], quoting=csv.QUOTE_NONE):
            log.info('insert data entries into table {} {} ...'.format(file, idx))
            idx += 1
            cols = c.REDUCED_SCHEMA[file]['cols'] if args.reduced else c.SCHEMA[file]['cols']
            data = data[cols]
            ms.insert(c.DB, file, data)



if __name__ == '__main__':
    main()