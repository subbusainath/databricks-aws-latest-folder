# Databricks notebook source
# aws s3 bucket name
aws_bucket_name = "databricks-subbu-blog-bucket"
# name of our mount point inside the databricks
mount_name = "file_access_mount_point"
# method to add bucket to the mount point
dbutils.fs.mount(f"s3a://{aws_bucket_name}",f"/mnt/{mount_name}")

# displaying the mount name 
display(dbutils.fs.ls(f"/mnt/{mount_name}"))

# moves from temp to databricks file system(dbfs)
dbutils.fs.mkdirs("dbfs:/blog_folder")

# COMMAND ----------


