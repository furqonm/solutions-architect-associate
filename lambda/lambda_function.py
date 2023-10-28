import boto3, os, json, time

sns = boto3.resource('sns')
rekognition_client = boto3.client('rekognition')

def lambda_handler(event, context):

    # fetch the data from the event
    sourceBucket = event['Records'][0]['s3']['bucket']['name']
    sourceKey = event['Records'][0]['s3']['object']['key']
    print("Initiating amazing image rekognition for key {} in bucket {}".format(sourceKey, sourceBucket))

    # Invoke Rekognition API and read label
    response = rekognition_client.detect_labels(Image={'S3Object': {'Bucket':sourceBucket, 'Name':sourceKey}}, MaxLabels=10)
    labels = []
    for label in response['Labels']:
        labels.append("{}: {:.2f}".format(label['Name'], label['Confidence']))
        
    result = {
       "Bucket": sourceBucket,
       "Name": sourceKey,
       "Labels": labels
    }
        
    # Publish the results to an SNS topic
    topic = sns.Topic(os.environ['SNS_TOPIC'])
    response = topic.publish(
        Message=json.dumps(result)
    )
    return result