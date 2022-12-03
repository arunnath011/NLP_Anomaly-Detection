
# Fall 2022 Final Project for w207

This project aims is to predict COVID19 mortality through panel data and images.

## Project Location

Our project is located in https://github.com/FirmwareDS/W266-FinalProject

##  Dataset

The raw data for the project can be obtained from  
`https://github.com/logpai/loghub`.

You can have to manually download the log file and they are huge (~27GiB) each and save them in a new folder named `dataset`. These instructions can be used to download Windows files and split

> wget https://zenodo.org/record/3227177/files/Windows.tar.gz?download=1
> tar -xvf Windows.tar.gz
> split -dl 100000 --additional-suffix=.txt Windows.log wrd

#### Before attempting to run any models. Please run the parser notebooks in the following folder.

Go to `/parser/` and run `jupyter-lab` on `W266_final_BERT_BGL_datacleaning.ipynb` for BGL parsing, `W266_final_BERT_Tbird_datacleaning.ipynb` for Tbird parsing and `W266_final_BERT_Windows_datacleaning.ipynb` for Windows parsing.


#### Running the Baseline Models
* Run`jupyter-lab` and walk through the code to run the baseline models in.

**BGL Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/baseline/W266_project_baseline_BGL.ipynb*
**Tbird Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/baseline/W266_project_baseline_Tbird.ipynb*
**Windows Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/baseline/W266_project_baseline_windows.ipynb*

#### Running the notebook


