# CS744_CourseProject


## Cluster Setup

### Local `sshconfig` setup

It is recommended to update your sshconfig to include all the vm running on the cloud. Here is an example: 

```
Host xgboost
	User <your-user-name>
	Port 27810
	Hostname c220g1-030610.wisc.cloudlab.us
	IdentityFile <your-id-file>

Host xgboost1
	User <your-user-name>
	Port 27811
	Hostname c220g1-030610.wisc.cloudlab.us
	IdentityFile <your-id-file>

Host xgboost2
	User <your-user-name>
	Port 27812
	Hostname c220g1-030610.wisc.cloudlab.us
	IdentityFile <your-id-file>

Host xgboost3
	User <your-user-name>
	Port 27813
	Hostname c220g1-030610.wisc.cloudlab.us
	IdentityFile <your-id-file>
```

Notice you will need the `User` and `IdentityFile` variables. In my case,
```
User jchen693
IdentityFile ~/.ssh/id_rsa
```

