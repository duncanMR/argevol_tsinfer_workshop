# `tsinfer` + `tsdate` workshop
## ArgEvol 2025 Conference - Day 2

Welcome - you can find all the files required to run through the workshop Jupyter notebook.
Windows users will need to install Windows Subsystem for Linux (WSL) to create a Linux environment.

## Setup instructions

In `bash`/`zsh` environment, in your chosen folder to install, run:

```
git clone https://github.com/duncanMR/argevol_tsinfer_workshop
cd argevol_tsinfer_workshop
```
If you are using `conda` or its variants, run

```
conda env create -f environment.yml
conda activate tsinfer-workshop
```
If you prefer to use `venv`, you need python 3.11+ installed, then you can do as follows:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Either way, you should be able to run the notebook with

```
jupyter lab
```

## Workshop outline

We will cover the following topics:

1. Convert the VCF to Zarr format  
2. Create the ancestral allele array  
3. Inference with `tsinfer`  
   3.1. Loading the data  
   3.2. Generate ancestors  
   3.3. Match ancestors
   3.4. Match samples  
4. Dating the ARG with `tsdate`  
5. Quality control with `tsbrowse`