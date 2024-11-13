"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2(
  resource_name='my-bucket-0accb434',
  # Setting the bucket name explicitly, so that pulumi doesn't append random string at the end.
  bucket='my-bucket-0accb434' 
)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.bucket)
