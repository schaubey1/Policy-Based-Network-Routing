# Policy-Based-Network-Routing
Python program to configure policy­ based (firewall) routing between devices on different subnets.

Configuration is as follows:

Host 1 10.0.1.1/24 h1
Host 2 10.0.1.2/24 h2
Host 3 10.0.2.1/24 h3
Host 4 10.0.2.2/24 h4
Host 5 10.0.3.1/24 h5
Host 6 10.0.3.2/24 h6
Host 7 10.0.4.1/24 h7

Policy Description
1 Allow hosts from each subnet to communicate with hosts within the same
subnet.
2 Allow hosts on subnet 10.0.1.0/24 can communicate ONLY with hosts on
subnet 10.0.3.0/24 and vice versa.
Any other traffic should be dropped.
Allow hosts on subnet 10.0.2.0/24 can communicate ONLY with hosts on
subnet 10.0.4.0/24 and vice versa.
Any other traffic should be dropped.

#Dependencies
https://github.com/noxrepo/pox
https://github.com/mininet/mininet
