import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Object_Detection'

list_of_files = [
    'models/__init__.py',
    'sources/__init__.py',
    'outputs/__init__.py',
    'research/__init__.py',
    'utils/__init__.py',
    'variables/__init__.py',
    'app.py',
    'setup.py',
    'requirements.txt'
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating  empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists at {filepath}')