## **AWS HOSTED RESUME WEBSITE <br> (CLOUD RESUME CHALLENGE)** <samp><img src="frontend/images/cloud1.ico" width="24" height="22" border="10"/></samp>


Check it out here: [ahmedharrisdevops.com](https://ahmedharrisdevops.com) 


## **Overview**
This project is my resume written in HTML and hosted with AWS S3 static website hosting. Inspired by the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/). The challenge was a great way for me to get hands on experience designing CI/CD workflows, configuring and deploying cloud infrastructure and cloud native applications.



## **Technologies/Tools used**
* Cloud: AWS, Route53, CloudFront CDN, S3, DynamoDB, Lamba, 
* IaC: AWS CloudFormation
* Version Control: Git
* CI/CD: GitHub Actions
* Languages: Python, JavaScript, HTML, CSS 



## **Architecture** 
* Route 53 manages custom domains, routing traffic securely through CloudFront distribution.
* Website stored in S3, with CloudFront CDN providing HTTPS, global caching, and low-latency delivery.
* API Gateway triggers Python Lambda function, updating and incrementing visitor counter in DynamoDB.
* GitHub Actions CI/CD frontend pipeline automatically deploys changes to HTML, CSS, and images; into S3 bucket and refreshes CloudFront caches.
* GitHub Actions CI/CD backend pipeline automatically deploys Python Lamba Function & DynamoDB.



## **Planned Features**
* Add Profile Page
* Terraform IaC
