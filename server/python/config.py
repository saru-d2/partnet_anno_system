import os

# FILL IN THIS!
# TODO: Fix path to sql volume mounted
file_storage_base_dir = '/usr/src/app/storage'

# DO NOT CHANGE!
anno_dir = os.path.join(file_storage_base_dir, 'annotations')
data_dir = os.path.join(file_storage_base_dir, 'data')
download_dir = os.path.join(file_storage_base_dir, 'downloads')

ori_part_dir = 'leaf_part_obj_normalized'
new_part_dir = 'new_parts'
remesh_part_dir = 'remesh_parts'
anno_result_dir = 'anno_results'
