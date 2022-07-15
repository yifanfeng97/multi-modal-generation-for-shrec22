import random
from pathlib import Path
from rich.progress import track
from trans import mesh2pt, mesh2vox, mesh2stdmesh

if __name__ == "__main__":
    n_pt = 1024
    d_vox = 32
    random.seed(2022)
    data_root = Path(f"data")
    out_root = Path(f"out")
    out_root.mkdir(exist_ok=True, parents=True)
    obj_list = sorted([str(p) for p in data_root.glob("*.ply")])
    for obj_path in track(obj_list):
        obj_path = Path(obj_path)
        obj_name = obj_path.stem
        cur_root = out_root / obj_name
        cur_root.mkdir(exist_ok=True, parents=True)
        cur_pt = cur_root / 'pointcloud'
        cur_vox = cur_root / 'voxel'
        cur_pt.mkdir(exist_ok=True, parents=True)
        cur_vox.mkdir(exist_ok=True, parents=True)
        # generate std mesh
        cur_std_obj = data_root / f"{obj_path.stem}.ply"
        cur_std_obj.parent.mkdir(parents=True, exist_ok=True)
        if not cur_std_obj.exists():
            mesh2stdmesh(obj_path, cur_std_obj)
        # generate point cloud
        cur_pt_obj = cur_pt / f'pt_{n_pt}.pts'
        if not cur_pt_obj.exists():
            mesh2pt(cur_std_obj, n_pt, cur_pt_obj)
        # generate voxel grid
        cur_vox_obj = cur_vox / f'vox_{d_vox}.ply'
        if not cur_vox_obj.exists():
            mesh2vox(cur_std_obj, d_vox, cur_vox / f'vox_{d_vox}.ply')
    print(f'Done!')
