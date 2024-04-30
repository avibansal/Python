import boto3

def delete_all_objects(s3_resource,bucket_name):
    res = []
    bucket=s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print("####### Resources to be deleted")
    print(res)
    if len(res) !=0:
        bucket.delete_objects(Delete={'Objects': res})
    else:
        print("This is an empty bucket!!")
    print("All objects in ", bucket_name , ' deleted!')

s3_resource = boto3.resource('s3', region_name='ap-south-1')
print("Let's delete ALL (Empty or Non-Empty) buckets:")
for bucket in s3_resource.buckets.all():
    print("delete all objects in a bucket", bucket.name)
    delete_all_objects(s3_resource,bucket.name)
    print("Deleting the bucket : ", bucket.name)
    s3_resource.Bucket(bucket.name).delete()