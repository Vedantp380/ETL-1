from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("ReadFinancialData") \
    .getOrCreate()

# Define JDBC URL for the database
jdbc_url = "jdbc:mysql://your_database_host:3306/your_database"

# Define connection properties
connection_properties = {
    "user": "your_username",
    "password": "your_password",
    "driver": "com.mysql.jdbc.Driver"
}

# Read the SQL table into a DataFrame
df = spark.read.jdbc(url=jdbc_url, table="financial_data", properties=connection_properties)

# Register the DataFrame as a temporary view
df.createOrReplaceTempView("financial_data")

# Revenue trends over quarters and years
revenue_trends = spark.sql("""
    SELECT
        year,
        quarter,
        SUM(revenue) AS total_revenue
    FROM
        financial_data
    GROUP BY
        year,
        quarter
    ORDER BY
        year,
        quarter
""")

# Show the results
revenue_trends.show()

# Expense analysis by category
expense_analysis = spark.sql("""
    SELECT
        JSON_EXTRACT(expenses_by_category, '$.marketing') AS marketing_expense,
        JSON_EXTRACT(expenses_by_category, '$.operations') AS operations_expense,
        JSON_EXTRACT(expenses_by_category, '$.sales') AS sales_expense
    FROM
        financial_data
""")

# Show the results
expense_analysis.show()

# Profit margins
profit_margins = spark.sql("""
    SELECT
        year,
        quarter,
        (SUM(revenue) - SUM(expenses)) / SUM(revenue) AS profit_margin
    FROM
        financial_data
    GROUP BY
        year,
        quarter
    ORDER BY
        year,
        quarter
""")

# Show the results
profit_margins.show()

# Product performance analysis
product_performance = spark.sql("""
    SELECT
        product_id,
        SUM(revenue) AS total_revenue
    FROM
        financial_data
    GROUP BY
        product_id
    ORDER BY
        total_revenue DESC
""")

# Show the results
product_performance.show()


# Save revenue trends to a CSV file
revenue_trends.write.csv("s3a://your_bucket/revenue_trends.csv", header=True)

# Save expense analysis to a CSV file
expense_analysis.write.csv("s3a://your_bucket/expense_analysis.csv", header=True)

# Save profit margins to a CSV file
profit_margins.write.csv("s3a://your_bucket/profit_margins.csv", header=True)

# Save product performance analysis to a CSV file
product_performance.write.csv("s3a://your_bucket/product_performance.csv", header=True)

