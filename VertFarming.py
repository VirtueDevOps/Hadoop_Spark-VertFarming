from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as pyspark_sum

# Initialize Spark context and Spark SQL
sc = SparkContext()
spark = SparkSession.builder.appName("Vertical Farming Estimation").getOrCreate()

# Read in data on office buildings in major cities
df = spark.read.csv("office_buildings.csv", header=True, inferSchema=True)

# Calculate the total square footage of office space in major cities
total_sqft = df.agg(pyspark_sum(df["square_footage"])).collect()[0][0]

# Estimate the amount of food that could be produced by converting office space into vertical farming centers
# Assume that each square foot of space can produce 10 pounds of food per year
food_production = total_sqft * 10

# Estimate the savings on utilities if the vertical farming centers used sustainable energy
# Assume that the average cost of electricity is $0.12 per kilowatt-hour and that each square foot of space uses 5 kilowatt-hours per year
# Also assume that sustainable energy sources like solar, geothermal, and hydro are 50% cheaper than traditional electricity
savings = total_sqft * 0.12 * 5 * 0.5

# Print the results
print(f"If all office buildings in major cities were converted into vertical farming centers, they could produce approximately {food_production} pounds of food per year.")
print(f"Using sustainable energy sources could save approximately ${savings} per year on utilities.")

# Stop Spark context
sc.stop()

