# Databricks notebook source
# MAGIC %sh ls ./

# COMMAND ----------

# DBTITLE 1,For .py within Repos Folder
# MAGIC %sh cd /Workspace/Users/vishesh.arya@databricks.com/playgames/python-files
# MAGIC ls ./

# COMMAND ----------

import sys
# sys.path.append("/dbfs/FileStore/Users/vishesh.arya@databricks.com")
sys.path.append("/Workspace/Users/vishesh.arya@databricks.com/playgames/python-files")

# COMMAND ----------

import vacustom

# COMMAND ----------

for path in sys.path:
  print(path)

# COMMAND ----------

sys.path.pop()

# COMMAND ----------


