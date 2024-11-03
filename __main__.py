import pulumi
from pulumi_gcp import compute

# Global configuration
global_config = pulumi.Config("gcp")

# Project configuration
config = pulumi.Config()
firewall_ports = config.require_object("firewall_ports")

# Create a network
network = compute.Network("network")

# Create a firewall rule
firewall = compute.Firewall("firewall",
    network=network.self_link,
    allows=[{
        "protocol": "tcp",
        "ports": firewall_ports,
    }],
    source_ranges=["0.0.0.0/0"]
)

# Create an instance
instance = compute.Instance("instance",
    machine_type=config.require("machine_type"),

    zone=global_config.require("zone"),

    boot_disk={
        "initializeParams": config.require_object("initializeParams"),
    },

    network_interfaces=[{
        "network": network.id,
        "access_configs": [{
            "nat_ip": compute.Address("instance-ip").address,
        }],
    }]
)

# Export the instance name and IP address
pulumi.export("instance_name", instance.name)
pulumi.export("instance_ip", instance.network_interfaces[0]["access_configs"][0]["nat_ip"])