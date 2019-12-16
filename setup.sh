#!/bin/bash


## Create a virtual link between two interfaces
sudo ip link add tap1 type veth peer name tap2

## Create two separate namespaces: they will be our client and our server
sudo ip netns add machine1
sudo ip netns add machine2


## Associate each machine with a separate interface
sudo ip link set tap1 netns machine1
sudo ip link set tap2 netns machine2


## Example: connect to the different machines. Do not run these command
#sudo ip netns exec machine1 bash
#sudo ip netns exec machine2 bash


## Bind different IP addresses to the different machines
sudo ip netns exec machine1 ip a add 1.1.1.10/255.255.255.0 dev tap1
sudo ip netns exec machine2 ip a add 1.1.1.20/255.255.255.0 dev tap2

##############################

## LAUNCH A NEW TERMINAL
## From the new terminal, execute the server
#sudo ip netns exec machine2 python tcp-server.py


## LAUNCH A SECOND TERMINAL
## From this second terminal, execute the client
#sudo ip netns exec machine1 python tcp-client.py
