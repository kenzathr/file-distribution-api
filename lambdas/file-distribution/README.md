# File Distribution API - AWS Serverless

## 📋 Project Overview

A complete serverless architecture on AWS for secure distribution of large files (3D renders).

**Project Name:** Axeon File Distribution  
**Author:** [Your Name]  
**Deadline:** March 28, 2025  
**Status:** In Progress

## 🏗️ Architecture
```
Client (HTTP Request)
    ↓
API Gateway (REST API)
    ↓
Lambda Function (FileDistributionPresignedUrl)
    ├→ S3 (Generate Presigned URL)
    ├→ DynamoDB (Log Downloads)
    └→ CloudWatch (Monitoring)
```

## 🚀 AWS Services

| Service | Purpose | Status |
|---------|---------|--------|
| **S3** | File Storage | ✅ Created |
| **Lambda** | Serverless Compute (Presigned URL Generation) | ✅ Coded |
| **API Gateway** | REST API Endpoint | ⏳ Next |
| **DynamoDB** | NoSQL Database (Download Logs) | ⏳ Week 2 |
| **CloudWatch** | Logging & Monitoring | ⏳ Week 2 |
| **CloudTrail** | API Audit Trail | ⏳ Week 2 |
| **IAM** | Access Control | ⏳ Week 2 |
| **KMS** | Encryption | ⏳ Week 2 |

## 📁 Project Structure
```
file-distribution-api/
├── lambdas/
│   └── file-distribution/
│       └── index.py          # Lambda function code
├── docs/                      # Documentation
├── tests/                     # Unit tests
├── README.md                  # This file
└── .git/                      # Git repository
```

## 📅 Project Timeline

### Week 1: Core Implementation ✅ In Progress
- [x] Day 1: Installation & Setup
- [x] Day 2: S3 Bucket Creation
- [x] Day 2: Lambda Code Development (with GitHub Copilot)
- [ ] Day 3: Deploy Lambda to AWS
- [ ] Day 4: API Gateway Configuration
- [ ] Day 5-7: DynamoDB & CloudWatch Integration

### Week 2: Infrastructure & DevOps
- [ ] Day 8-10: AWS CDK (Infrastructure as Code)
- [ ] Day 11-12: GitHub Actions (CI/CD Pipeline)
- [ ] Day 13-14: Testing & Performance Validation

### Week 3: Final Report & Submission
- [ ] Day 15-17: Report Writing (40-50 pages)
- [ ] Day 18-19: Review & Finalization
- [ ] Day 20: Submission

## 🔧 Technology Stack

| Component | Technology |
|-----------|-----------|
| Cloud Provider | AWS |
| Compute | AWS Lambda (Python 3.11) |
| Storage | Amazon S3 |
| Database | Amazon DynamoDB |
| API | Amazon API Gateway |
| IaC | AWS CDK (Python) |
| CI/CD | GitHub Actions |
| Version Control | Git / GitHub |
| IDE | Visual Studio Code |
| AI Assistant | GitHub Copilot |

## 📝 Key Features

✅ **Presigned URL Generation**
- Secure, time-limited URLs for file downloads
- 1-hour expiration for security
- Error handling for missing files

✅ **Serverless Architecture**
- No server management required
- Auto-scaling capabilities
- Pay-per-use pricing model

✅ **Security**
- IAM-based access control
- S3 bucket encryption (KMS)
- API authentication
- CloudTrail audit logging

✅ **Monitoring & Logging**
- CloudWatch metrics & logs
- Download activity tracking
- Real-time alerting

## 🚀 Getting Started

### Prerequisites
- AWS Account with Free Tier
- AWS CLI configured
- Git installed
- Python 3.11+

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/file-distribution-api.git
cd file-distribution-api

# Install AWS CLI (if not already installed)
pip install awscli

# Configure AWS credentials
aws configure
```

## 📊 Bucket Information

**S3 Bucket Name:** `axeon-distribution-fichiers-2026`

## 🔐 Environment Variables

When deploying Lambda, set:
```
BUCKET_NAME=axeon-distribution-fichiers-2026
```

## 📝 Notes

- Using AWS Free Tier (No costs)
- All credentials stored securely (never committed to Git)
- Code follows professional Python standards
- Regular commits to GitHub for version control
- GitHub Copilot used for code generation assistance

## 📧 Contact & Support

For questions or feedback about this project, please reach out.

## 📜 License

This project is part of a graduation thesis (PFE - Projet de Fin d'Études).

---

**Last Updated:** March 10, 2025  
**Next Milestone:** Deploy Lambda to AWS (Day 3)