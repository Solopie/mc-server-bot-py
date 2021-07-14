import boto3
from .config import INSTANCE_ID, AWS_DRY


class EC2_Client:
    def __init__(self):
        self.client = boto3.client("ec2")
        self.instance_id = INSTANCE_ID

    def start(self):
        print("[INFO] Starting the server")
        error = ""

        try:
            response = self.client.start_instances(
                InstanceIds=[self.instance_id],
                DryRun=AWS_DRY
            )
        except Exception as e:
            print(e)
            error = "AWS EC2 Client 'start' failed"

        return (response, error)

    def status(self):
        print("[INFO] Checking status of server")
        error = ""

        try:
            response = self.client.describe_instances(
                InstanceIds=[self.instance_id],
                DryRun=AWS_DRY
            )
            status = ""
            for r in response["Reservations"]:
                for i in r["Instances"]:
                    if i["InstanceId"] == self.instance_id:
                        status = i["State"]["Name"]
        except Exception as e:
            print(e)
            error = "AWS EC2 Client 'status' failed"

        return (status, error)
