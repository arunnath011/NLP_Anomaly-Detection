
# Fall 2022 Final Project for w266 - Log Anomaly Detection using NLP

This project aims is to predict Log Anomaly Detection using NLP models.

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

Its important to move the parsed csv files to Google drive for any of the baseline or project models to runs. 

#### Running the Baseline Models
* Run`jupyter-lab` and either go to `/baseline/` folder or walkthrough the code in GIT in the links below.

**BGL Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/baseline/W266_project_baseline_BGL.ipynb*
**Tbird Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/baseline/W266_project_baseline_Tbird.ipynb*
**Windows Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/baseline/W266_project_baseline_windows.ipynb*

#### Running the models
* Run`jupyter-lab` and either go to `/experiments/` folder or walkthrough the code in GIT in the links below.


**BGL Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/experiments/W266_Logmodelbuilding_BGL.ipynb*
**Tbird Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/experiments/W266_Logmodelbuilding_Tbird.ipynb*
**Windows Baseline Source**: *https://github.com/FirmwareDS/W266-FinalProject/blob/main/experiments/W266_Logmodelbuilding_Windows.ipynb*

All the models were run on google Collab with the parsed files stored in Google drive as mentioned above.

#### Project report

Project report is provided as a PDF in `/final report/` or can be downloaded from *https://github.com/FirmwareDS/W266-FinalProject/tree/main/final%20report* 

