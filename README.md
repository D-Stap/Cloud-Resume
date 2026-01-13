
[![Live Resume](https://img.shields.io/badge/Live%20Resume-grey?style=flat&labelColor=red&logo=readthedocs)](https://dafantestapletonresume.link)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-grey?style=flat&labelColor=0A66C2&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dafante-stapleton/)
[![GitHub](https://img.shields.io/badge/Profile-grey?style=flat&labelColor=181717&logo=github&logoColor=white)](https://github.com/D-Stap)
[![Credly](https://img.shields.io/badge/Credly-grey?style=flat&labelColor=FF6B00&logo=credly&logoColor=white)](https://www.credly.com/users/dafante-stapleton)
[![Email](https://img.shields.io/badge/Email-grey?style=flat&labelColor=EA4335&logo=gmail&logoColor=white)](mailto:dafante.e.stapleton.com)

# Cloud-Resume
# 🧠 Cloud Resume Challenge — Dafante Stapleton

This is my implementation of the Cloud Resume Challenge using AWS.  
The goal: build a secure, cloud-hosted, serverless resume application and automate deployment.

---

## 🔗 Live Project

👉 https://dafantestapletonresume.link

---

## 🏗️ Architecture

- **S3** — Static site hosting  
- **CloudFront** — CDN + HTTPS enforcement  
- **Route 53** — Custom DNS domain  
- **API Gateway** — API endpoint for visitor counter  
- **AWS Lambda (Python)** — Backend logic for counter  
- **DynamoDB** — Stores unique visitor count  
- **AWS SAM** — Infrastructure as Code  
- **GitHub Actions** *(coming)* — Automated deployment + cache invalidation  

---

## 📊 Visitor Counter

Tracks unique visitors using:
- LocalStorage to prevent duplicate counting
- Lambda function updates DynamoDB table
- Count returned to frontend via API

---

## 🔐 Security Highlights

- HTTPS required everywhere through CloudFront
- IAM least-privilege role for Lambda
- Backend code serverless — no servers exposed

---

## 🚀 Next Steps

- Add CI/CD with GitHub Actions
- Add screenshots of desktop + mobile views
- Publish blog write-up on lessons learned

---
🔗 LinkedIn: https://www.linkedin.com/in/dafantestapleton
