# Elastic Beanstalk
## Introduction
- It is a platform as a service, which provides a way to quickly deploy and manage web-apps on AWS.
> PaaS: It is a platform that allows customers to develop, run and manage applications without the complexity of building and maintaining the infra. Just like Heroku
	
- EB is **not recommeded** for **"Production"** applications.
- EB does not cost anything on its own buyt the instances that it deploys do cost (RDS, EC2 etc)
-  EB is powered by a CloudFormation template:
	- Elastic load balancer
	- Autoscaling Groupd
	- RDS Database
	- EC2 Instance preconfigured (or custom) platforms
	- Monitoring (CloudWatch, SNS)
	- In-Place and Blue/Green deployment methodoligies
	- Security
	- Can run Dockerized environments

## Supported Languages
![[LanguagesSupported.png]]

## Web VS Worker Environment
an EB application has one of two environmnets:
- Web Environment: Has Auto Scaling Group (ASG) and a Elasictic Load Balancer (ELB)
- Worker Environment: Has an ASG, SQS Queue and has the Sqsd daemon on the EC2 instance. Add or remove instances based on queue size.

On a typical case both are deployed for a web application
![[WebVSWorker.png]]

### Web Environments
Web Environments have two kinds:
![[WebEB.png]]
In Single Instance the IP will point to the server but in the other it points to the load balancer

## Deployment Policies available in EB
| Deployment Policy                                                                 | Load Balanced Env | Single Instance Env |
| --------------------------------------------------------------------------------- | ----------------- | ------------------- |
| All at Once [[Elastic Beanstalk#All at once]]                                     | 🟩                | 🟩                  |
| Rolling [[Elastic Beanstalk#Rolling]]                                             | 🟩                | 🟥                  |
| Rolling with additional batch [[Elastic Beanstalk#Rolling with additional batch]] | 🟩                | 🟥                  |
| Immutable [[Elastic Beanstalk#Immutable]]                                         | 🟩                | 🟩                  |

Rolling and Rolling with additional batch is not available in single instance because a load balancer is needed to attach and detach instances in batches.

### Deployment Method Summary:
| Deployment Policy             | No downtime | No DNS change | Deploy Time | Rollback Process | Code deployed to Instances |
| ----------------------------- | ----------- | ------------- | ----------- | ---------------- | -------------------------- |
| All at once                   | 🟥          | 🟩            | 🕒          | Manual           | Existing                   |
| Rolling                       | 🟩          | 🟩            | 🕒🕒➕      | Manual           | Existing                   |
| Rolling with additional batch | 🟩          | 🟩            | 🕒🕒🕒➕    | Manual           | New and Existing           |
| Immutable                     | 🟩          | 🟩            | 🕒🕒🕒🕒    | Terminate New    | New                        |
| Blue/green                    | 🟩          | 🟥            | 🕒🕒🕒🕒    | Swap URL         | New                        |

Why is In-Place and Blue/Green Missing?

### All at once:
![[AllAtOnce.png]]

### Rolling:
![[Rolling.png]]

### Rolling with additional batch
![[RollingWithAdditionalBatch.png]]

### Immutable
![[Immutable.png]]

### In-Place vs Blue/Green Deployment
- EB by default foes in-place updates
	- In-Place means within the scope of the EB environment (**Exam focuses on this**)
	- In-Place means within the scope of the same server
	- In-Place means within the scope of uninterrupted server

![[BlueGreenvsInplace.png]]

## Configuration Files
EB can be customized by using configuration files:
-	```.ebextensions``` is a hidden folder at the root of your project which contains config files
-	```.config``` is the extension for the config files which needs to be stored in ```.ebextensions```
-	Configuiration files can configure:
	1.	Option settings
	2.	Linux / Windows Server Configuration
	3.	Custom Resources

These files help in transferring configurations to other when they want the same settings in their EB environment

- ```env.yaml``` is the environment manifest which is stored at the root of your project. This file is important to set defaults:
```yaml
AWSConfigurationTemplateVersion: 1.1.0.0
# The name of the environment
EnvironmentName: example-prod+
SolutionStack: Python
# Associating the env links to connect say web and worker env together
EnvironmentLinks:
	"WORKERQUEUE": "worker+"
OptionSettings:
	aws:elb:loadbalancer:
		# Default Configuration for the services
		CrossZone: true
```
The '+' is to give a unique name to it by adding the machine name

- Linux Server Configuration:
	- Packages: Download and install prepackaged applications and components
	```yaml
	packages:
		yum:
			libmemcached: []
			ruby-devel: []
	```
	- Groups: Create Linux/UNIX groups and to assign group IDs
	```yaml
	groups:
		groupAdmin: {}
		groupDev:
			gid: "12"
	```
	- Users: Create Linux/UNIX users
	```yaml
	users:
		akhil:
			groups:
				- groupAdmin
			uid: 69
			homeDir: "/akhil"
	```
	- Files: Create files in the EC2 instace (inline or from URL)
	```yaml
	files:
		"/home/akhil/application.yml":
			mode: "000755"
			owner: "000755"
			group: "000755"
			content: |
				SECRET: blahblah
	```
	- Commands: Execute commands on the EC2 instance before app is setup
	```yaml
	commands:
		1_create_root_dir:
			command: mkdir /var/www/app
		2_create_link:
			command: ln -s /var/www/app /app
	```
	- Services: Define which services should be started or stopeed when the instance is launched
	```yaml
	services:
		sysvinit:
			nginx:
				enabled: true
				ensureRunning : true
	```
	- Container Commands: Execute commands that affect the source code of your application
	```yaml
	container_commands:
		1_run_command:
			command: command
	```
	
## EB CLI
EB CLI is similar to heroku CLI commands. To set it up just git clone the cli code form github
The following are the typical commands:
```bash
eb init			# Configure your project direvtory and the EB CLI
eb create		# Create your first environment
eb status		# See the current status of your environment
eb health		# view the health info of the environments and the state of overall env (use --refresh to update every 10s)
eb events		# See a list of events output by EB
eb logs			# Pull logs from an instance in your EB
eb open			# Open your env's website in a browser
eb deploy		# Once the env is running, deploy an update
eb config		# Show the configuration options available for your running env
eb terminate	# Delete the environment
```

## EB Custom Image
When you create an EB environment, you can specify an AMI to use instead of the standard EB AMI
- A custom AMI can improve provisioning times when instances are launched in your enviroment
- If there are a lot of sogftware that isnt included in the standard EMI we would need custom images in that case
![[CustomAMISteps.png]]







