import os
import sys
# from geometry_utils import *
import trimesh
from progressbar import ProgressBar
import numpy as np
import json
import pdb

input_dir = sys.argv[1]

def load_obj(fn):
    fin = open(fn, 'r')
    lines = [line.rstrip() for line in fin]
    fin.close()

    vertices = []; faces = []
    for line in lines:
        if line.startswith('v '):
            vertices.append(np.float32(line.split()[1:4]))
        elif line.startswith('f '):
            faces.append(np.int32([item.split('/')[0] for item in line.split()[1:4]]))

    # mesh = dict()
    face_arr = np.vstack(faces) - 1
    vertex_arr = np.vstack(vertices)

    return {'faces': face_arr, 'vertices': vertex_arr}

def export_obj(out, v, f):
    with open(out, 'w') as fout:
        for i in range(v.shape[0]):
            fout.write('v %f %f %f\n' % (v[i, 0], v[i, 1], v[i, 2]))
        for i in range(f.shape[0]):
            fout.write('f %d %d %d\n' % (f[i, 0], f[i, 1], f[i, 2]))


bar = ProgressBar()
for item in bar(os.listdir(input_dir)):
    print (item)
    if not item.startswith('.'):
        cur_dir = os.path.join(input_dir, item)
        in_dir = os.path.join(cur_dir, 'leaf_part_obj')
        out_dir = os.path.join(cur_dir, 'leaf_part_obj_normalized')
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        # try:
            
        with open(os.path.join(cur_dir, 'leaf_part_ids.json'), 'r') as fin:
            part_list = json.load(fin)

        f_list = []; v_list = []; tot_v = 0;
        ff_list = []; vv_list = []; part_name_list = []
        for part_id in part_list:
            mesh = load_obj(os.path.join(in_dir, str(part_id)+'.obj'))
            f = mesh['faces']
            v = mesh['vertices']
            v_list.append(v)
            vv_list.append(v)
            f_list.append(f+tot_v)
            ff_list.append(f)
            part_name_list.append(part_id)
            tot_v += v.shape[0]

        f_arr = np.vstack(f_list)
        v_arr = np.vstack(v_list)
        # pdb.set_trace()

        msh = trimesh.Trimesh(v_arr, f_arr)
        # msh.export("tmp", "obj")

        # pts,_  = trimesh.sample.sample_surface(msh, label=None, num_points=200)
        # TODO
        # pts,_  = trimesh.sample.sample_surface(msh, count=np.min([100000, v_arr.shape[0]]))
        pts,_  = trimesh.sample.sample_surface(msh, count=2000)

        center = np.mean(pts, axis=0)
        pts -= center
        scale = np.sqrt(np.max(np.sum(pts**2, axis=1)))
        
        with open(os.path.join(cur_dir, 'normalization_params.txt'), 'w') as fout:
            fout.write('%f %f %f\n' %(center[0], center[1], center[2]))
            fout.write('%f' % scale)

        # vv_list = (np.array(vv_list) - center )/ scale
        vv_list = [(i-center)/scale for i in vv_list[0]]
        vv_list = np.array(vv_list)
        for i in range(len(part_name_list)):
            
            out_fn = os.path.join(out_dir, '1'+'.obj')

            print(vv_list.shape, center.shape, (vv_list[i]-center[None, ...]))
            # assert()
            msh = trimesh.Trimesh(vv_list, ff_list[i] )
            msh.export(out_fn, "obj")
            # export_obj(out_fn, (vv_list[i]-center)/scale, ff_list[i])
            # export_obj(out_fn, vv_list[i], ff_list[i])

            # print(out_fn)
        # except Exception as e:
        #     print ('ERROR', e)

