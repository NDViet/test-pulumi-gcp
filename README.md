To create a Pulumi project for provisioning a virtual machine in Google Cloud, follow these steps:  

Install Pulumi CLI: If you haven't already, install the Pulumi CLI.

```bash
curl -fsSL https://get.pulumi.com | sh
```

Install Google Cloud SDK

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

Authenticate and configure the Google Cloud SDK
```bash
gcloud init
```

Create a new Pulumi project:

```bash
pulumi new gcp-python --force --name gcp-vm --description "Create a virtual machine in Google Cloud" --stack gcp --yes
```

Install required Python packages:

```bash
pip install pulumi pulumi-gcp
```

Create resources on target cloud provider:

```bash
pulumi up
```

Once the resources are created, you can check the status of the resources using the following command:

```bash
pulumi stack output
```

To destroy the resources created, use the following command:

```bash
pulumi destroy
```