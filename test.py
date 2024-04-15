from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ETL-pipeline-using-Airflow-and-AWS-EMR-cluster").getOrCreate()

# Set shuffle partitions
spark.conf.set("spark.sql.shuffle.partitions", 20)

# Read CSV files from S3 and cache them for optimization
items = spark.read.csv("olist_order_items_dataset.csv", header=True, inferSchema=True).cache()
orders = spark.read.csv("olist_orders_dataset.csv", header=True, inferSchema=True).cache()
products = spark.read.csv("olist_products_dataset.csv", header=True, inferSchema=True)

# Join datasets to get order/seller/product info for orders where the seller missed the deadline to deliver the shipment to the carrier
orders_info = items.join(orders, items.order_id == orders.order_id) \
    .join(products, items.product_id == products.product_id) \
    .select(items.order_id, items.seller_id, items.shipping_limit_date, items.price, items.freight_value,
            products.product_id, products.product_category_name, orders.customer_id, orders.order_status,
            orders.order_purchase_timestamp, orders.order_delivered_carrier_date, orders.order_delivered_customer_date,
            orders.order_estimated_delivery_date)

# Print the schema
orders_info.printSchema()

# Write the output to S3
orders_info.coalesce(3).write.csv(r"path to your s3", header=True)
