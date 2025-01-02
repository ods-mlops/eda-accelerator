# Databricks notebook source
# MAGIC %md
# MAGIC The Data Profiling notebook takes the output DataFrame from the 'Data Load' notebook. This notebook will explorer the Data Types, Summary Statistics, Data Completeness, Uniqueness and Cardinality, Duplication, Value Distribution Analysis. The notebook can be similar to a script if the your data is loaded into a DataFrame named 'df'.

# COMMAND ----------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# COMMAND ----------

df.shape

# COMMAND ----------

df.info()

# COMMAND ----------

df.corr()
