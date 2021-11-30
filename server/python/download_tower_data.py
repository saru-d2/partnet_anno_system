import numpy as np
import json
import sys
import os
from subprocess import call

from jio_filestore.io.azure_filestore import ObjectStoreFactory
from .configs import file_store_config
fs = ObjectStoreFactory(file_store_config)
# connect to database


# list all items in file store
items = fs.list()
# 