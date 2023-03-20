
from dler.__init__ import Manifest

with open('test.csv', 'r') as f:
    manifests = f.readlines().split(',')

for x in manifests:
    Manifest(url=x[1]).save_images()