# Databricks notebook source
from glob import glob
import os
import datetime
import time


def get_latest_folder(dir_path):
    directory_list_dict = {}
    directories = glob(f"{dir_path}/*")
    date_list = []
    for d in directories:
        latest_file_key = max(glob(f"{d}/*"), key=os.path.getctime)
        file_arr_time = time.strftime(
            "%m/%d/%Y", time.gmtime(os.path.getmtime(latest_file_key))
        )
        date_val = datetime.datetime.strptime(file_arr_time, "%m/%d/%Y")
        directory_list_dict[date_val] = latest_file_key
        date_list.append(date_val)
    max_date = max(date_list)
    latest_file = directory_list_dict[max_date]
    latest_directory = latest_file.rsplit("/", 1)[0]
    return latest_directory

# COMMAND ----------

latest_folder = get_latest_folder('/dbfs/mnt/file_access_mount_point/blog_folder')
os.environ['LATEST'] = latest_folder
print(os.getenv('LATEST'))

# COMMAND ----------

# MAGIC %sh
# MAGIC cp $LATEST/* /dbfs/blog_folder

# COMMAND ----------


