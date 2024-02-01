import boto3
import traceback
import os
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

# AWS認証情報
ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
# リージョン
AWS_REGION = os.environ['REGION']


def pgenerate_signed_url(bucket_name, object_key):
    try:
        # クライアント作成
        s3_client = boto3.client("s3")
        # S3から署名付きURLを取得する
        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=120,
        )
        return url

    except Exception as e:
        # 内部エラー
        log.error(traceback.format_exc())
        return e, 500


def s3_upload():
    # S3バケット名
    bucket_name = os.environ['PRACTICE_BUCKET_NAME']
    # オブジェクトキー
    object_key = os.environ['PRACTICE_OBJECT_KEY']
    # ローカルダウンロードパス
    file_name = os.environ['DOWNLOAD_FILE_NAME']

    try:
        # S3情報チェック,情報がない場合は400エラーを返却
        if not bucket_name or not object_key or not file_name:
            # バケット名、オブジェクトキー、ローカルダウンロードパスが存在しない場合
            log.info("bucket_name: {bucket_name}")
            log.info("object_key: {object_key}")
            log.info("file_name: {file_name}")
            return 'S3情報を確認してください。', 400

        s3 = boto3.resource('s3')
        s3_resource = s3.Bucket(bucket_name)

        s3_resource.download_file(object_key, file_name)
        print("s3バケットからのファイルアップロードが完了しました")

        signed_url = pgenerate_signed_url(bucket_name, object_key)

        return signed_url

    except Exception as e:
        log.error(traceback.format_exc())
        return e, 500


def sample_func():
    url = s3_upload()
    return url, 200
