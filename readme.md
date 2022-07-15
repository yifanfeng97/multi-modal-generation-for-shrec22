# Introduction
In our paper "SHREC'22: Open-Set 3D Object Retrieval", we have released two datasets for open-set 3D object retrieval. The two datasets are generated based on the [Modelnet40](https://modelnet.cs.princeton.edu/) dataset. Here, we release the core code for multi-modal data generation including **Voxel Modality Generation**, **Pointcloud Modality Generation**, and **24 Images Modality Generation**.

# Settings for generating voxel and pointcloud modalities
- python 3.8
- open3d
- pillow
- numpy

### Usage
Run the following code. The generated voxel and pointcloud will be stored in the `out` direction.
```bash
python generate_voxel_pointcloud.py
```

## Settings for generating 24 images modality
- blender 3.0

### Usage
Open `generate_24_images.blend` with blender 3.0, then run the code. Then, rendered 24 images can be found in the `out` folder.

# Note
The fully datasets can be download [here](https://www.moon-lab.tech/shrec22). Examlpe code and evaluation metrics can be found [here](https://github.com/yifanfeng97/OS-MN40-Example).
