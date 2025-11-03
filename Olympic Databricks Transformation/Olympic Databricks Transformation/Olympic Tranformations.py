# Databricks notebook source
# MAGIC %md
# MAGIC # `This is Just A Simple Project`

# COMMAND ----------

# MAGIC %md
# MAGIC ### `Everything is done in one file`

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@olympicfarazstfg.dfs.core.windows.net/Athletes/athletes.csv")
coaches = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@olympicfarazstfg.dfs.core.windows.net/Coaches/coaches.csv")
entriesgender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@olympicfarazstfg.dfs.core.windows.net/EntriesGender/entriesGender.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@olympicfarazstfg.dfs.core.windows.net/Medals/medals.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@olympicfarazstfg.dfs.core.windows.net/Teams/teams.csv")

# COMMAND ----------

entriesgender = entriesgender.withColumn("Female",col("Female").cast(IntegerType()))\
    .withColumn("Male",col("Male").cast(IntegerType()))\
    .withColumn("Total",col("Total").cast(IntegerType()))

# COMMAND ----------

# Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold", ascending=False).select("Team_Country","Gold").show()

# COMMAND ----------

# Calculate the average number of entries by gender for each discipline
average_entries_by_gender = entriesgender.withColumn(
    'Avg_Female', entriesgender['Female'] / entriesgender['Total']
).withColumn(
    'Avg_Male', entriesgender['Male'] / entriesgender['Total']
)
average_entries_by_gender.show()

# COMMAND ----------

athletes.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/tokyoolymic/transformed-data/athletes")

# COMMAND ----------

# ✅ Writing back using ABFSS paths
coaches.repartition(1).write.mode("overwrite").option("header", "true") \
    .csv("abfss://silver@olympicfarazstfg.dfs.core.windows.net/transformed-data/Coaches")

entriesgender.repartition(1).write.mode("overwrite").option("header", "true") \
    .csv("abfss://silver@olympicfarazstfg.dfs.core.windows.net/transformed-data/EntriesGender")

medals.repartition(1).write.mode("overwrite").option("header", "true") \
    .csv("abfss://silver@olympicfarazstfg.dfs.core.windows.net/transformed-data/Medals")

teams.repartition(1).write.mode("overwrite").option("header", "true") \
    .csv("abfss://silver@olympicfarazstfg.dfs.core.windows.net/transformed-data/Teams")