## **AWS HOSTED RESUME WEBSITE <br> (CLOUD RESUME CHALLENGE)** <samp><img src="frontend/images/cloud1.ico" width="24" height="22" border="10"/></samp>


Check it out here: [ahmedharrisdevops.com](https://ahmedharrisdevops.com) 


## **Overview**
This project is my resume written in HTML and hosted with AWS S3 static website hosting. Inspired by the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/). 



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



## **Architecture** 
* Route 53 manages custom domains, routing traffic securely through CloudFront distribution.
* Website stored in S3, with CloudFront CDN providing HTTPS, global caching, and low-latency delivery.
* API Gateway triggers Python Lambda function, updating and incrementing visitor counter in DynamoDB.
* GitHub Actions CI/CD frontend pipeline automatically deploys changes to HTML, CSS, and images; into S3 bucket and refreshes CloudFront caches.
* GitHub Actions CI/CD backend pipeline automatically deploys Python Lamba Function & DynamoDB.



## **Planned Features**
* Add Profile Page
* Terraform IaC
