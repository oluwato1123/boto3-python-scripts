import boto3 
import os
import glob

s3 = boto3.client("s3")

#find all objects in the bucket
objects = s3.list_objects(Bucket = 'fade-tobi-08022022')["Contents"]

#Iteration
for object in objects:
   #print(object["Key"])
    s3.delete_object(Bucket = 'fade-tobi-08022022',
    Key = object["Key"])