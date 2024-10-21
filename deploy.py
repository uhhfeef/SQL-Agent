import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

# Initialize a SageMaker session
sess = sagemaker.Session()

# Specify the IAM role ARN
role = 'arn:aws:iam::390403862568:role/SageMakerExecutionRole_Llama3_Sql' 

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'defog/llama-3-sqlcoder-8b',
	'SM_NUM_GPUS': json.dumps(1)
}



# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	image_uri=get_huggingface_llm_image_uri("huggingface",version="2.2.0"),
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1,
	instance_type="ml.g5.2xlarge",
	container_startup_health_check_timeout=300,
  )
  
# send request
predictor.predict({
	"inputs": "Hey my name is Julien! How are you?",
})