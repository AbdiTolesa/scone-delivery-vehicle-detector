## Background
Image Classifiers are used in the field of computer vision to identify the content of an image and it is used across a broad variety of industries, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms, and even in diagnostic medicine.

This project is about building an image classification model for a scone-delivery-focused logistics company, *Scones Unlimited*, that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

In this project, I have used AWS Sagemaker to build an image classification model that can tell bicycles apart from motorcycles. I have deploye my model, used AWS Lambda functions to build supporting services, and AWS Step Functions to compose my model and services into an event-driven application.

## Project Steps Overview
- Step 1: Data staging
- Step 2: Model training and deployment
- Step 3: Lambdas and step function workflow
- Step 4: Testing and evaluation
- Step 5: Optional challenge
- Step 6: Cleanup cloud resources

## Workspace Instructions
For this project, you will complete the work within the AWS lab provided through the Udacity classroom.

### Sagemaker Studio
You should already have the Sagemaker Studio User created from earlier in the course, so you'll just need to launch the studio.

In case you need a refresher:

- Proceed to open up the AWS console from the AWS Gateway.
- Click through the AWS console to Amazon Sagemaker.
- Click through the main Sagemaker page to Amazon Sagemaker Studio from the left hand toolbar.
- If a user does not exist already in the Sagemaker Studio Control Panel, Add user.
- Select an execution role that has full Sagemaker Access, otherwise you can create a new role.
- Create a role and proceed with creating the user.

### Lambda Functions
You need the Lambda service to complete the project. At this point, you should have already created and deployed a few lambda functions at this point.

In case you want to test it again:

- Proceed to open up the AWS console from the AWS Gateway.
- Click through the AWS console to Amazon Lambda.
- Click to create a lambda function.
- Test the lambda function is working

### Step Function Visual Editor
You should have access to the step function visual editor. If you want to double-check:

- Proceed to open up the AWS console from the AWS Gateway.
- Click through the AWS console to Step Function.
- Click to create a state machine.
- Choose to design your workflow visually
- Create a simple Step function

### Create a Role Instruction (You can skip this if you have a role created)
- Find the SageMaker service page and click the startup button to start configuring your environment
- Select the Quick Start option.
![image](https://user-images.githubusercontent.com/41271840/149580654-d1ab5d37-7f16-4401-b373-28c3259f55b3.png)
- For the required IAM role choose to create a new role - note this role name down for later.
![image](https://user-images.githubusercontent.com/41271840/149580705-9dc9efdb-4b47-40e6-8ab2-cc40222ea3d2.png)
- Leave all default options and create
![image](https://user-images.githubusercontent.com/41271840/149580737-cadb7700-a1a7-4937-bb77-66ec8c7c912e.png)
Hit "Submit" at the bottom of the page to complete your configuration
It may take a few minutes for SageMaker to provision the environment after you complete this workflow.

## About the Dataset
The [CIFAR-10 and CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) are labeled subsets of the [80 million tiny images](http://people.csail.mit.edu/torralba/tinyimages/) dataset. They were collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

### CIRAR-10
The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

### CIFAR-100
This dataset is just like the CIFAR-10, except it has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class. The 100 classes in the CIFAR-100 are grouped into 20 superclasses. Each image comes with a "fine" label (the class to which it belongs) and a "coarse" label (the superclass to which it belongs).

We have used the CIFAR-100 dataset in this project.

### Data Staging

We'll use a sample dataset called CIFAR to simulate the challenges Scones Unlimited are facing in Image Classification. In order to start working with CIFAR we'll need to:

1. Extract the data from a hosting service
2. Transform it into a usable shape and format
3. Load it into a production system

## About Amazon Image Classification Algorithm
We have used the Amazon SageMaker image classification algorithm in this project to train our model.
The [Amazon SageMaker image classification algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification.html) is a supervised learning algorithm that supports multi-label classification. It takes an image as input and outputs one or more labels assigned to that image. It uses a convolutional neural network (ResNet) that can be trained from scratch or trained using transfer learning when a large number of training images are not available.

Our model takes in an image and outputs an array of two values, the predicted probability value for each of your classes (bicycle and motorcycle respectively.) So, for example, a value of `b'[0.91, 0.09]'` indicates the probability of being a bike is 91% and being a motorcycle is 9%.

## Evaluation
The following graph reveals the performance of our model
![image](https://user-images.githubusercontent.com/41271840/149670903-1aef8426-51a6-4bda-b558-d58e48c6d718.png)

## Suggestions for improvement
If you're up for it, you can even go further with these stretch goals:

* Extend your workflow to incorporate more classes: the CIFAR dataset includes other vehicles that Scones Unlimited can identify with this model.
* Modify your event driven workflow: can you rewrite your Lambda functions so that the workflow can process multiple image inputs in parallel? Can the Step Function "fan out" to accomodate this new workflow?
* Consider the test data generator we provided for you. Can we use it to create a "dummy data" generator, to simulate a continuous stream of input data? Or a big paralell load of data?
* What if we want to get notified every time our step function errors out? Can we use the Step Functions visual editor in conjunction with a service like SNS to accomplish this? Try it out!