import numpy as np
import open3d as o3d
from pathlib import Path

def mesh2stdmesh(obj_path, out_path=None):
    obj_path = Path(obj_path)
    if out_path is None:
        out_path = obj_path.with_name(f'std_{obj_path.name}').with_suffix('.ply')
    else:
        out_path = Path(out_path)
    mesh = o3d.io.read_triangle_mesh(str(obj_path))
    center = (mesh.get_max_bound()+mesh.get_min_bound()) / 2
    mesh.translate(-center)
    mesh.scale( 1/np.max(mesh.get_max_bound()-mesh.get_min_bound()), center=(0, 0, 0))
    o3d.io.write_triangle_mesh(str(out_path), mesh, write_ascii=False)

def mesh2pt(obj_path, n_pt, out_path=None):
    obj_path = Path(obj_path)
    if out_path is None:
        out_path = obj_path.with_name(f'pts_{n_pt}_{obj_path.name}').with_suffix('.pts')
    else:
        out_path = Path(out_path)

    mesh = o3d.io.read_triangle_mesh(str(obj_path))
    mesh.translate(-mesh.get_center())
    mesh.scale(1/np.max(mesh.get_max_bound()-mesh.get_min_bound()), center=mesh.get_center())
    pts = mesh.sample_points_poisson_disk(n_pt)
    o3d.io.write_point_cloud(str(out_path), pts, write_ascii=False)

def mesh2vox(obj_path, vox_size, out_path=None):
    obj_path = Path(obj_path)
    if out_path is None:
        out_path = obj_path.with_name(f'vox_{obj_path.name}').with_suffix('.ply')
    else:
        out_path = Path(out_path)

    mesh = o3d.io.read_triangle_mesh(str(obj_path))
    mesh.translate(-mesh.get_center())
    mesh.scale(vox_size/np.max(mesh.get_max_bound()-mesh.get_min_bound()), center=mesh.get_center())
    voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=1)
    o3d.io.write_voxel_grid(str(out_path), voxel_grid, write_ascii=False)
