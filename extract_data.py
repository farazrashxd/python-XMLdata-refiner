import gzip
import os

for root, dirs, files in os.walk('data'):
    for file in files:
        with gzip.open(os.path.join(root, file), 'rb') as f_in:
            with open(os.path.join(root, file[:-3]), 'wb') as f_out:
                f_out.write(f_in.read())
