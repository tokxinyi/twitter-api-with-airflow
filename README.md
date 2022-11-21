# How to use this project
1. Create a EC2 instance in AWS or an equivalent on other cloud providers.
	- Instance details
		1. t3.large
		2. 30GiB of storage, encrypted
		3. Ubuntu
2. SSH into the EC2 instance and install Docker using this [guide](https://docs.docker.com/engine/install/ubuntu/)
3. Follow this [guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) to install Apache Airflow.
4. Replace the `docker-compose.yaml` downloaded from previous step with the one in this repository in the EC2 instance.
5. Copy the python files into EC2's dag folder.
6. Run `sudo docker compose up` to start the Airflow cluster.
7. Go to `<EC2 public ipv4 address>:8080` to access the Airflow UI. You should see the DAG in it.

# Challenges
- Understanding DAG's structure and the decorators.
- Getting accustomed to the Airflow UI.
- Figuring out the instance details and AWS products and features
    - Inbound rules, IAM roles and policies

# Takeaways from this project
- Understand how to deploy an Apache Airflow cluster with `docker-compose.yaml` file
- Learning how to write a simple DAG
- Running the pipeline using AWS EC2 instance and S3 bucket with Ubuntu as the operating system
- Enable  `Stop - Hibernate` behaviour before launching the EC2 instance (under Advanced details) so that we can hibernate the instance, and store any files that are in the VM ([source](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)) 
	- To use the `hibernate` feature, need to encrypt the volumes (under Configure Storage > click on Advanced > under EBS Volumes > click Show details > change the encryption to Encrypted)
	- Free tier has 30GB of EBS General Purpose (SSD) or Magnetic storage
- Tasks should be indempotent (result produced should be the same no matter how many times you run the tasks)


# Possible improvements for this project
1. To write a Dockerfile to install additional python packages instead of using PIP_ADDITIONAL_REQUIREMENTS environment variable.
2. Create a data pipeline that is more complicated
	- email notification for failed tasks
	- extract raw data to database > read from database to do data processing > processed data to data warehouse
3. Enable `flower` to do monitoring of the Airflow cluster
