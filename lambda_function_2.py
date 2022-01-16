import json
#import sagemaker
import base64
#from sagemaker.serializers import IdentitySerializer

import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2021-12-13-10-29-37-255"

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"])

    # Instantiate a Predictor
    # predictor = sagemaker.endpoint.Predictor(ENDPOINT)
    
    runtime= boto3.client('runtime.sagemaker')
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                ContentType='image/png',
                                       Body=image)

    # For this model the IdentitySerializer needs to be "image/png"
    #predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    #inferences = predictor.predict(image)
    
    # We return the data back to the Step Function    
    #event["inferences"] = inferences.decode('utf-8')
    result = json.loads(response['Body'].read().decode())

    event["inferences"] = result

    return {
        'statusCode': 200,
        'body': event
    }