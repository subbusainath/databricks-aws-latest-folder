# Databricks notebook source
# MAGIC %sh
# MAGIC ls /dbfs/blog_folder
# MAGIC

# COMMAND ----------

dirs = os.listdir('/dbfs/blog_folder/')
for file in dirs:
	if file.endswith('.zip'):
		unzip_cmd = f"unzip /dbfs/blog_folder/{file} -d /dbfs/blog_folder/extract"
		print(f"The unzip command  {unzip_cmd}")
		os.system(unzip_cmd)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /dbfs/blog_folder/extract

# COMMAND ----------


