from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()

# {
#     "name": "Maicon",
#     "surName": "Moreira",
#     "age": 23,
#     "contacts": {
#         "email": "maicon.moreira@gmail.com",
#         "phone": "4798769876"
#     }
# }

schema = StructType(
    [
        StructField("name", StringType(), nullable=False),
    ]
)

df = spark.read.json("sample.json", schema, multiLine=True)

df.show()

df.write.text("bla.txt")
