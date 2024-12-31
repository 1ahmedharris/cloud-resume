## **AWS HOSTED RESUME WEBSITE <br> (CLOUD RESUME CHALLENGE)** <samp><img src="frontend/images/cloud1.ico" width="24" height="22" border="10"/></samp>


Check it out here: [ahmedharrisdevops.com](https://ahmedharrisdevops.com) 


## **Overview**
This project is my resume built with AWS S3 static website hosting, and AWS serverless architecture. inspired by the Cloud Resume Challenge. 



## **Technologies/Tools used**
* AWS S3
* AWS DynamoDB
* AWS Lamba
* AWS CloudFront CDN
* AWS CloudFormation IaC Templates 
* Git
* Github Actions CI/CD Pipeline
* Python
* HTML, CSS, & JavaScript



## ** Frontend **
* Website hosted in S3 bucket with CloudFront CDN providing HTTPS, global caching and low-latency delivery.
* GitHub Actions CI/CD pipeline automatically deploys changes to HTML, CSS, and images to S3 bucket and refreshes CloudFront caches.
* Route 53 manages custom domains, routing traffic securely through the CloudFront distribution.



## ** Backend **
* API Gateway triggers Python Lambda function, which to updates and increments visitor countser in DynamoDB. 
* GitHub Actions CI/CD pipeline automatically deploys Python Lamba Function & DynamoDB.



## **Planned Features**
* Add Profile Page
* Terraform IaC
