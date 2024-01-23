import boto3
import traceback
import os

# AWS認証情報
ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
# リージョン
AWS_REGION = os.environ['REGION']


def s3_upload():
    # S3バケット名
    bucket_name = os.environ['PRACTICE_BUCKET_NAME']
    # オブジェクトキー
    object_key = os.environ['PRACTICE_OBJECT_KEY']
    # ローカルダウンロードパス
    file_name = os.environ['DOWNLOAD_FILE_NAME']

    try:
        s3 = boto3.resource('s3')
        s3_resource = s3.Bucket(bucket_name)

        s3_resource.download_file(object_key, file_name)
        print("s3バケットからのファイルアップロードが完了しました")

    except Exception as e:
        print('error occuer!!!')
        print(e)
        print(traceback.format_exc())


def sample_func():
    # S3バケットとオブジェクトキーを指定

    # s3 = boto3.client('s3',
    #                   aws_access_key_id=ACCESS_KEY,
    #                   aws_secret_access_key=SECRET_KEY)

    # s3.download_file(bucket_name, object_key, file_name)
    s3_upload()
    return 'download ok'
