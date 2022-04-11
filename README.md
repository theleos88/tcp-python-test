# First test

##############################

## LAUNCH A NEW TERMINAL
- From the new terminal, execute the server

sudo ip netns exec machine2 python tcp-server.py


## LAUNCH A SECOND TERMINAL
- From this second terminal, execute the client

sudo ip netns exec machine1 python tcp-client.py



**Enjoy one-shot communication**
