import boto3
from .config import INSTANCE_ID, AWS_DRY


class EC2_Client:
    def __init__(self):
        self.client = boto3.client("ec2")
        self.instance_id = INSTANCE_ID

    async def start(self):
        print("[INFO] Starting the server")
        work = False
        message = ""
        error = ""

        status, mesg, err = await self.status()
        if status != "stopped":
            message = "The server is either already running or shutting down. Please try again later"
            return (work, message, error)

        try:
            response = self.client.start_instances(
                InstanceIds=[self.instance_id],
                DryRun=AWS_DRY
            )
            work = True
        except Exception as e:
            print(e)
            error = "AWS EC2 Client 'start' failed"

        return (work, message, error)

    async def status(self):
        print("[INFO] Checking status of server")
        status = ""
        message = ""
        error = ""

        try:
            response = self.client.describe_instances(
                InstanceIds=[self.instance_id],
                DryRun=AWS_DRY
            )
            for r in response["Reservations"]:
                for i in r["Instances"]:
                    if i["InstanceId"] == self.instance_id:
                        status = i["State"]["Name"]

            if not status:
                raise Exception("Instance couldn't be found")
        except Exception as e:
            print(e)
            error = "AWS EC2 Client 'status' failed"

        return (status, message, error)
