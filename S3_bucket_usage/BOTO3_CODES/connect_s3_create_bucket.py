import boto3
import random
import string
import uuid
def create_valid_bucket_name(bucket_prefix,
    min_size=3,max_size=63):
    # The generated bucket name must be 
    #between 3 and 63 chars long
    bname = ''.join([bucket_prefix, 
        str(uuid.uuid4())])
    if max_size > len(bname) > min_size:
        size=len(bname)
    elif len(bname) < min_size :
        bname += random.choices(
            string.ascii_lowercase 
            + string.digits, 
            max_size - len(bname))
    return bname[:max_size]


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    print("Current region is ", session.region_name, 
        type(session.region_name))
    current_region = session.region_name
    bucket_name = create_valid_bucket_name(bucket_prefix)
    print("Bucket name is ", bucket_name)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response


if __name__ == '__main__':

    s3_connection = boto3.resource('s3', 
        region_name='ap-south-1')
    create_bucket('boto',s3_connection)
    print("Hello, Amazon S3! Let's list your buckets:")
    for bucket in s3_connection.buckets.all():
        print("Name of the bucket is : ", bucket.name)

