## Hadoop/Spark Vertical Farming Estimator

Welcome to the Hadoop/Spark Vertical Farming Estimator project! This script ventures into the revolutionary concept of transforming existing office buildings in major cities into self-sustained vertical farming centers, leveraging renewable energy sources for operation.

### Concept

Imagine the global food production potential if we could convert metropolitan office spaces into vertical farming centers, substantially boosted with the integration of sustainable energy resources like solar, geothermal, and hydro power. This script aids in conceptualizing this transformation by estimating the food production capacity and potential utility savings that could be achieved.

### Working

The script operates in the following phases:

1. **Data Ingestion**:
   - Reads in data on office buildings in major cities using Apache Spark.
   
2. **Food Production Estimation**:
   - Calculates the total square footage of office space and estimates the prospective amount of food production.

3. **Utility Savings Estimation**:
   - Assumes a 50% cost reduction using sustainable energy sources compared to conventional electricity.
   - Estimates savings based on an assumed electricity consumption rate of 5 kilowatt-hours per year per square foot.

### Customization

Users have the freedom to tailor the script according to their data and assumptions regarding food production to generate more accurate estimates. 

### Prerequisites

To run the script, ensure you have the following set up:

- Hadoop: Although not directly utilized, it provides a potent platform for storing and managing the data processed by Spark.
- Apache Spark: Acts as the computational engine executing data processing tasks.

### Getting Started

1. Install Apache Spark and Hadoop in your working environment.
2. Clone this repository to acquire the script and relevant datasets.
3. Load your data and modify the script to suit your assumptions for a personalized estimation.

### Usage

Run the script to calculate:
- The total square footage available for conversion into vertical farms.
- Estimated food production from the vertical farms.
- Potential utility savings using sustainable energy sources.

### Contributions

Feel free to contribute to this forward-thinking project to foster an era of sustainable and urban agriculture.
