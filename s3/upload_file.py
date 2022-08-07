import boto3

import os
import glob

#s3 = boto3.client("s3")
#s3.upload_file(
#    Filename = "beach.jpg",
#    Bucket = "fade-tobi-08032022",
#    Key = "uploadtest.jpg")
#How to uploading multiple files
cwd = os.getcwd()
cwd = cwd + "/index/"
files = glob.glob(cwd + "*.jpg")
##print(files)

for file in files:
    s3 = boto3.client("s3")
    s3.upload_file(
    Filename = file,
    Bucket = "fade-tobi-08022022",
    Key = file.split("/")[-1])