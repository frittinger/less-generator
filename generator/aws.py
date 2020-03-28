"""AWS code"""

import boto3
from botocore.exceptions import ProfileNotFound


def aws_test(profile):
    if profile is None:
        print("# No AWS profile given. Using default profile.\n")
        session = boto3.session.Session()
    else:
        try:
            session = boto3.Session(profile_name=profile)
        except ProfileNotFound:
            print("AWS profile not found.")
            raise AssertionError("AWS profile not found.")

    s3 = session.resource('s3')
    # s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
