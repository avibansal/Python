import boto3
import uuid

def create_valid_bucket_name(bucket_prefix,
    min_size=3,max_size=60):
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

def copy_to_bucket(s3_resource,bucket_from_name, 
    bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(
        copy_source)


if __name__ == '__main__':
    s3_resource = boto3.resource('s3', region_name='ap-south-1')
    bucket1_name, bucket_response = create_bucket(
        'shantanu-bucket1', s3_resource)
    bucket2_name, bucket_response = create_bucket(
        'shantanu-bucket2', s3_resource)
    
    print("####################")
    print("Check if buckets created. Following is list all buckets created :")
    for bucket in s3_resource.buckets.all():
        print("Name of the bucket is : ", bucket.name)

    print("####################")
    print("Uploading file to bucket 1 --> ")
    local_file_name = "AWS_S3_info.txt"
    s3_file_name="AWS_S3_info.txt"

    s3_resource.Bucket(bucket1_name).upload_file(
        Filename=local_file_name, Key=s3_file_name)
    print("File uploaded successfully successfully!")

    print("####################")
    print("Copy file from bucket1 to bucket2")

    copy_to_bucket(s3_resource,bucket1_name, bucket2_name, 
        s3_file_name)

    print("####################")
    print("Check all file names in Bucket 2")

    bucket=s3_resource.Bucket(bucket2_name)
    # print("Key","\tStorage_Class", 
    #   "Last Modified", "\t\tVer_id", "Metadata", sep="\t")
    for obj in bucket.objects.all():
        print(obj.key)
    print("Completed!")