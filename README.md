# Affordance Highlighting Project

This repository contains the code and resources for the Affordance Highlighting project. The project includes various scripts, data files, and Jupyter notebooks for different phases and tasks.

This work focuses on advancing the 3D Highlighter model, a system capable of automatically localizing fine-grained semantic regions on 3D meshes based on textual descriptions. We extend this model to handle point clouds and real-world 3D scans, integrating the concept of affordance to identify not only parts, but also the potential uses and interactions suggested by an object's shape and characteristics. This expansion overcomes the limitations of previous models that relied exclusively on meshes and demonstrates potential applications in areas such as structural analysis and augmented reality. 


## Project Notebooks

This project contains several Jupyter notebooks for different phases and tasks of the project. Below is a list of all the `.ipynb` files included in this project:

1. **[notebook_base.ipynb](notebook_base.ipynb)**: Base notebook for initial setup and experiments. It refers to the part 1 of the experiments where the 3D Highlither model is used and evaluated, by searching for the best model configuration, tuing hyperparameters.
2. **[mesh_reconstruction.ipynb](mesh_reconstruction.ipynb)**: Notebook for testing the pipeline of the mesh reconstruction starting from point cloud data. It refers to the part 2 of the experiments, starting from meshes in `data` folder.
3. **[pc_to_mesh.ipynb](pc_to_mesh.ipynb)**: Notebook for converting point clouds, from AffordanceNet dataset, to mesh. It refers to the part 3 of experiments where there are two different phases:

    **[eval_phase_notebook.ipynb](eval_phase_notebook.ipynb)**: Notebook for evaluation phase.

    **[test_phase_notebook.ipynb](test_phase_notebook.ipynb)**: Notebook for testing phase.

4. **[extension_notebook.ipynb](extension_notebook.ipynb)**: Notebook for extending functionalities on 3D real-world scans.



## Data Files

The `data` directory contains several `.obj` files used in the first phase of the project:

- **candle.obj**
- **dog.obj**
- **horse.obj**

The `mesh_polycam` directory contains additional `.obj` files used for the extension part and they refers to the mesh obtained with the tool Polycam.


## Scripts

- **[load_dataset.py](load_dataset.py)**: Script for loading datasets.
- **[render.py](render.py)**: Script for rendering 3D models.
- **[utils.py](utils.py)**: Utility functions used throughout the project.
- **[mesh.py](mesh.py)**: Script for handling meshes.

## Normalization

The `Normalization` directory contains scripts for normalizing 3D models:

- **[MeshNormalizer.py](Normalization/MeshNormalizer.py)**
- **[Normalizer.py](Normalization/Normalizer.py)**


