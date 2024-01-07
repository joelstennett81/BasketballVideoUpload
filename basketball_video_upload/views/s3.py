import boto3
from django.conf import settings


def get_url_for_video(request, video_name):
    url = 'https://' + settings.AWS_STORAGE_BUCKET_NAME + '.s3.us-east-2.amazonaws.com/' + request.user.profile.first_name + '_' + request.user.profile.last_name + '/' + video_name
    return url


def get_presigned_url_for_video(request, object_name):
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    params = {
        'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
        'Key': str(object_name),
    }
    response = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=3600)
    return response


def upload_video_to_s3(request, file, video_name):
    s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    key = f'{request.user.profile.first_name}_{request.user.profile.last_name}/{video_name}'
    s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).put_object(Key=key, Body=file)
