
# Fall 2022 Final Project for w207

This project aims is to predict COVID19 mortality through panel data and images.

## Project Location

Our project is located in
`/source/notebook/stonybrooks_predict_mortality.ipynb`

## Cleaned Dataset

The cleaned (resized 256x256) images used for training the ML model are found in
`https://drive.google.com/file/d/1q-35EBD-kKO_dQi5hMecfkMwfTIA6pWg/view?usp=sharing`.

The original images can be found in 
`https://drive.google.com/file/d/1wBkA9Q8J-KaVL8-AQP3pK9oTEV6YwvMV/view?usp=sharing`, 
you can have to manually download this file as it is huge (~10GiB).

Our data is referencing publicly available dataset that can be pfound in
`https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=89096912`

#### Before attempting to run any scripts. Please run the pre-requisite installation step.

Go to `/helper_scripts/` and run `bash install.sh` for initial setup of required packages to run.


#### COVID-19 prediction from images for reference
First, run conda environment via `conda activate w207_final`

DenseNet121 located in `/References/PredictSars/source/DenseNet121`

* Run`jupyter-lab` and walk through the code to train the model using DenseNet121.

**Source**: *https://www.kaggle.com/code/shawon10/covid-19-diagnosis-from-images-using-densenet121/notebook*


#### Running the notebook

Prior to running the notebook you will need to enable lfs on your local repo, otherwise the read_covid_panel_data will read a link
rather than the actual csv file. So you need to do the following commands

> git lfs install
> git lfs fetch --all origin main
> git lfs checkout dataset/StonyBrooks/PanelData/deidentified_overlap_tcia.csv

you should be able to confirm this worked by verifying the size of the csv file eg

> ls -l dataset/StonyBrooks/PanelData/deidentified_overlap_tcia.csv
-rw-rw-rw- 1 codespace root 832908 Jun 10 22:42 dataset/StonyBrooks/PanelData/deidentified_overlap_tcia.csv
