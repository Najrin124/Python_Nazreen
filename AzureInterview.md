
--- azure administration - 1

resource groups - is a logical container that holds azure resources.

resource groups helps u to maange, orgniase , apply permissions, delete services together

aws - no equivalent

storage accounts

storage accounts stores data - images, videos, backups, logs, documenst, etc

storage account provides blob storage(it can store pdf, jpg, mp4), file storage, queue storage(kafka - messages), table storage

azure - aws

blob storage - s3, it stores unstructured data
file share - EFS
queue storage - SQS
table storage - Dynamo DB(no sql db)

virtual machines - aws ec2 instance


networking - vnet, subnet, nsg

vnet - virtual network - private network

aws - vpc

subnet - smaller network inside vnet

nsg - network security group - azure firewall.

aws - security group

puprupose if nsg - filter the network traffic

nsg and firewall - difference

nsg filters at network level

firewall provides centralised advanced filtering 

azure sql - rrlational db, azure maanges os, patch, backup, security.

azure sql - aws rds sql server


--- azure administration - 1

- resource groups - is a logical container that holds azure resources.

- resource groups helps u to maange, orgniase , apply permissions, delete services together

aws - no equivalent

storage accounts

storage accounts stores data - images, videos, backups, logs, documenst, etc

storage account provides blob storage(it can store pdf, jpg, mp4), file storage, queue storage(kafka - messages), table storage

azure - aws

blob storage - s3, it stores unstructured data
file share - EFS
queue storage - SQS
table storage - Dynamo DB(no sql db)

virtual machines - aws ec2 instance


networking - vnet, subnet, nsg

vnet - virtual network - private network

aws - vpc

subnet - smaller network inside vnet

nsg - network security group - azure firewall.

aws - security group

puprupose if nsg - filter the network traffic

nsg and firewall - difference

nsg filters at network level

firewall provides centralised advanced filtering 

azure sql - rrlational db, azure maanges os, patch, backup, security.

azure sql - aws rds sql server



azure sql database - done

Day 2

Azure app service - is a fully managed web hosting platform, it is a PaaS service(platform asa  service)
 lets say u built flask and react based application

usually the process is - buy a server -> install OS -> configure nginx -> configure SSL certiifcates -> configure firewall

option 2 - azure app service where ti handles everything - u just upload the code it manges evything

AWS - Elastic beanstalk(azure app service)

Azure or any cloud provider manages Server, OS, patching, scaling, ssl, u have to only manage code


azure fucntions - it manages or it runs when needed, means serverless manageemnt platform

AWS lambda - it is the alternative like azure functions

when do u use azure functions - when you have event driven workloads, then we will use function apps

azure load balancer - load balancer distributes traffic

AWS ELB - Azure load balancer

public - internet facing and private - private traffic

azure application gateway - it tells you what application and under which ports it will be accessible, it understands url, http, https, cookies, etc

AWS - application load balancer

features are ssl termination, url routing, web application firewall as well

difference between laod balancer - operates in layer 4 and application gateway - operate sin layer 7

microsoft entra id(azure ad) - azure active directory

it stores all users details

entra id - means it is an identity and access manageemnt system

sso - single sign on

AWS - IAM identity center

RBAC - role based access controls
azure key vault - store passwords, secrets, tokens, etc

AWS - Secrets manager


azure monitor and application insights

azure monitor is like cloud watch in aws - which monitors and displays teh graphs of all services

application insights - is like xray of all the applications

