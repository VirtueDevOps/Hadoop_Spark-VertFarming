# Hadoop_Spark-VertFarming

Another whacky idea. What if we can help determine how much more food would be available world wide if existing office buildings in major cities were converted into vertical farming centers, and used sustainable energy sources to power them.

This script uses Spark to read in data on office buildings in major cities, calculate the total square footage of office space, and estimate the amount of food that could be produced by converting that space into vertical farming centers. You can customize this script with your own data and assumptions about food production to get a more accurate estimate of the potential impact of converting office buildings into vertical farming centers.
Hadoop is not used directly. Instead, the script uses Spark, which is a distributed computing platform that can run on top of Hadoop. Hadoop can be used to store and manage the data that is processed by Spark, as well as to provide a distributed computing platform for Spark to run on. In this way, Hadoop and Spark can be used together to perform large-scale data processing tasks efficiently.

This script includes a section to estimate the potential savings on utilities if the vertical farming centers used sustainable energy sources like solar, geothermal, and hydro. The script assumes that these sources are 50% cheaper than traditional electricity and calculates the savings based on the total square footage of office space and an assumed electricity consumption rate of 5 kilowatt-hours per year per square foot.
