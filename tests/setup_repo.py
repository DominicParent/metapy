import os

repo="testrepo"
data_stages=["raw", "preproc", "proc", "analysis", "diss"]
datasets=["dataset1", "dataset2", "dataset3", "dataset4"]
years=["2021", "2022"]
months=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for dstage in data_stages:
    for dset in datasets:
        for y in years:
            for m in months:
                os.makedirs(repo + "/" + dstage + "/" + dset + "/" + y + "/" + m)
