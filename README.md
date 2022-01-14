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
