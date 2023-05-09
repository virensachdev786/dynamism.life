
## Project Title: Networked Swap Space: A New Approach to Memory Hierarchy

Memory hierarchy is a critical component of modern computer systems. One important layer of the memory hierarchy is swap space, which is a reserved area of a hard disk or other storage device that is used to temporarily store data that cannot be held in RAM. In this project, we present a new approach to memory hierarchy that involves connecting swap space over the network to increase processing power and physical resources.

## Product Overview

We propose a new product that enables the sharing of swap space over the network, allowing multiple computers to share resources and greatly increase processing power and physical resources. By leveraging the power of multiple computers, our product can help reduce processing times and improve the overall performance of computing systems. Our approach is particularly suited for use in distributed computing environments, where resources may be spread across different locations.

## Design and Implementation

We present a detailed design and implementation of our product, including:

The network protocol used to connect computers and share swap space
The software used to manage swap space and distribute data between computers
The algorithms used to optimize resource allocation and minimize latency
Our product has been designed to be scalable and flexible, and can be easily integrated into existing computing environments.

## Experimental Results

We have conducted extensive experiments to evaluate the effectiveness of our product in increasing processing power and physical resources. Our experiments demonstrate that our product can significantly improve the performance of computing systems in a variety of scenarios, including:

Running memory-intensive applications on a single computer with limited RAM
Distributing computing tasks across multiple computers with varying levels of processing power and memory capacity
Improving the performance of virtualized environments by reducing the need for dedicated RAM resources

## Conclusion

Our product offers a new approach to memory hierarchy that can help to overcome many of the limitations of traditional memory hierarchy, and enable the development of more powerful and efficient computing systems. By sharing swap space over the network, our product can help to reduce processing times, increase processing power and physical resources, and improve the overall performance of computing systems.

We believe that our product has the potential to revolutionize the way that memory hierarchy is managed in modern computer systems, and we are excited to continue developing and improving it in the future.

## Sharing a Swapfile using Network File Server

This section describes the steps for sharing a swapfile using Network File Server (NFS).

### Step 1: Install NFS on both machines

```
sudo apt-get install nfs-kernel-server nfs-common
```

### Step 2: Create a shared directory on the machine that will provide the swap file

```
sudo mkdir /swap_share 
sudo chmod 777 /swap_share
```

### Step 3: Edit NFS exports file on the machine that will provide the swap file

```
sudo nano /etc/exports
```

Add the following line at the end of the file:

```
/swap_share(rw,sync,no_subtree_check)
```

### Step 4: Start NFS server

```
sudo systemctl start nfs-kernel-server
```

### Step 5: Check NFS server status

```
sudo systemctl status nfs-kernel-server
```

### Step 6: Create directory on second machine

```
sudo mkdir /swap_mount
```

### Step 7: Mount shared directory

```
sudo mount <ip-address-of-the-provider-machine>:/swap_share /swap_mount
```

## Sharing folder between host machine and virtual machine

This section describes the steps for sharing a folder between a host machine and a virtual machine.

### Step 1: Turn off the virtual machine

### Step 2: Add a shared folder in the virtual machine's settings

Go to `Settings > Shared Folders` and add the folder path.

### Step 3: Start the virtual machine

### Step 4: Mount the shared folder in the virtual machine

```
sudo mount -t vboxsf <folder_name>  <mount_point>
cd  /<mount_point>
```

## Automating the setup process

To automate the setup process, you can use the following script:

```
echo "Y" | apt-get install nfs-kernel-server nfs-common

# Create Shared Folder
mkdir /swap_share
chmod 777 /swap_share

# Edit Exports File
echo "/swap_share 192.168.1.239(rw,sync,no_subtree_check)" >> /etc/exports

# Start Network File System Servers
systemctl start nfs-kernel-server

# Get IP Address of Server Machine
ifconfig | grep inet | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'
```

This script installs NFS, creates a shared folder, edits the exports file, starts the NFS server, and gets the IP address of the server machine. You can modify the script to suit your specific needs.

