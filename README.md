# Mini Local E-Certificate Issuance & Verification System

![Project Banner](https://via.placeholder.com/800x200?text=E-Certificate+Blockchain+System)

## 📋 Project Overview

The Mini Local E-Certificate Issuance & Verification System is a blockchain-based solution for creating, managing, and verifying academic certificates using Hyperledger Fabric. The system connects three organizations (University, Student, and Verifier) in a trusted network that ensures certificate authenticity and prevents forgery.

### 🎯 Core Features

- **Certificate Issuance**: Universities can create and issue digital certificates with cryptographic proof
- **Certificate Viewing**: Students can access and view their certificates
- **Certificate Verification**: Third parties can verify the authenticity of certificates
- **Secure Storage**: All certificate data is stored on an immutable blockchain
- **Easy API Access**: FastAPI provides a simple interface to interact with the blockchain
- **Local Network**: Deploy across multiple computers in a LAN environment

## 🏗️ Architecture

The system uses a combination of:

- **Hyperledger Fabric**: Enterprise-grade blockchain framework
- **FastAPI**: High-performance API framework
- **PostgreSQL**: Relational database for application data
- **Docker**: Containerization for consistent deployment

### 👥 Organizations

1. **University Organization**: Issues certificates with digital signatures
2. **Student Organization**: Views and manages received certificates
3. **Verifier Organization**: Validates certificate authenticity

## 🛠️ Project Structure

```
├── api/                         # FastAPI application 
│   ├── v1/                      # API version 1 endpoints
│   │   ├── endpoints/           # API route handlers 
│   │   │   ├── certificates.py  # Certificate management endpoints
│   │   │   ├── auth.py          # Authentication endpoints
│   │   │   ├── blockchain.py    # Blockchain interaction endpoints
│   │   │   └── users.py         # User management endpoints
│   │   ├── deps.py              # Dependency injection
│   │   └── router.py            # API router configuration
│   ├── core/                    # Core application modules
│   │   ├── config.py            # Application configuration
│   │   ├── security.py          # Security utilities
│   │   └── exceptions.py        # Custom exceptions
│   ├── db/                      # Database 
│   │   ├── models/              # SQLAlchemy models
│   │   ├── session.py           # Database session management
│   │   └── repositories/        # Database access layer
│   ├── schemas/                 # Pydantic schemas for request/response validation
│   │   ├── certificates.py      # Certificate schemas
│   │   ├── users.py             # User schemas 
│   │   └── blockchain.py        # Blockchain operation schemas
│   └── main.py                  # FastAPI application entry point
├── blockchain/                  # Hyperledger Fabric integration
│   ├── chaincode/               # Smart contract definitions
│   │   ├── certificates/        # Certificate management smart contracts 
│   │   │   ├── src/             # Source code for the chaincode
│   │   │   ├── Dockerfile       # Docker build for chaincode
│   │   │   └── package.json     # Dependencies for Node.js chaincode
│   │   └── utils/               # Shared utilities for chaincode
│   ├── network/                 # Fabric network configuration
│   │   ├── crypto-config/       # Certificates and keys
│   │   ├── channel-artifacts/   # Channel configuration 
│   │   └── configtx.yaml        # Network config for channels/orgs
│   ├── scripts/                 # Network management scripts
│   │   ├── start-network.sh     # Script to start the network
│   │   ├── stop-network.sh      # Script to stop the network
│   │   └── deploy-chaincode.sh  # Script to deploy chaincode
│   └── sdk/                     # Fabric SDK integration layer
│       ├── connection.py        # Connection management
│       ├── gateway.py           # Fabric Gateway integration
│       └── transactions.py      # Transaction submission utilities
├── services/                    # Business logic services
│   ├── certificate_service.py   # Certificate management service
│   ├── auth_service.py          # Authentication service
│   ├── user_service.py          # User management service
│   └── blockchain_service.py    # Blockchain interaction service
├── utils/                       # Shared utility functions
│   ├── logging.py               # Logging configuration
│   ├── security.py              # Security utilities
│   └── validators.py            # Custom validators
├── tests/                       # Test suite
│   ├── api/                     # API endpoint tests
│   ├── blockchain/              # Blockchain integration tests
│   ├── services/                # Service unit tests
│   └── conftest.py              # Test configuration
├── docker/                      # Docker configurations
│   ├── api/                     # FastAPI service Dockerfile
│   ├── blockchain/              # Blockchain service Dockerfile
│   └── nginx/                   # API gateway configuration
├── frontend/                    # Simple web interface
│   ├── university/              # University portal
│   ├── student/                 # Student portal
│   └── verifier/                # Verifier portal
├── deployment/                  # Deployment configurations
│   ├── local/                   # Local network deployment
│   │   ├── university/          # University node config
│   │   ├── student/             # Student node config
│   │   └── verifier/            # Verifier node config
│   └── cloud/                   # Cloud deployment templates (future)
├── docker-compose.yaml          # Docker compose for local development
├── docker-compose.prod.yaml     # Docker compose for production
├── .env.example                 # Example environment variables
├── requirements.txt             # Python dependencies
├── alembic.ini                  # Database migration configuration
├── migrations/                  # Database migrations
│   └── versions/                # Migration versions
└── README.md                    # Project documentation
```

## 📚 Research & Development Plan

### Phase 1: Research & Planning (2 weeks)

- [x] **Define certificate structure and metadata**
  - Certificate ID, student details, course information, grades, date
  - Digital signature standards and verification methods
  
- [x] **Design blockchain network architecture**
  - Organization structure (University, Student, Verifier)
  - Channel configuration for privacy
  - Endorsement policies

- [x] **API design**
  - Define endpoints for all stakeholders
  - Authentication and authorization strategy
  - Document API specifications

### Phase 2: Core Development (4 weeks)

- [ ] **Blockchain network setup**
  - Configure Hyperledger Fabric components
  - Set up organizations and channels
  - Develop and test connection profiles

- [ ] **Smart contract development**
  - Certificate issuance chaincode
  - Certificate viewing chaincode
  - Certificate verification chaincode

- [ ] **API development**
  - FastAPI endpoint implementation
  - Integration with blockchain SDK
  - Database schema and migrations

### Phase 3: Integration & Testing (3 weeks)

- [ ] **Integrate components**
  - Connect API with blockchain network
  - Implement authentication and authorization
  - Develop simple frontend interfaces

- [ ] **Testing**
  - Unit testing for services and API endpoints
  - Integration testing for blockchain interaction
  - End-to-end testing across organizations

### Phase 4: Deployment & Documentation (3 weeks)

- [ ] **Local network deployment**
  - Docker container configuration
  - Network setup across multiple computers
  - Performance and stress testing

- [ ] **Documentation**
  - API documentation with Swagger/ReDoc
  - Deployment guides for all organizations
  - User manuals for different user types

- [ ] **Cloud-ready preparation**
  - Kubernetes manifests (optional)
  - Automated CI/CD pipeline setup
  - Security hardening

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.9+
- Node.js 16+ (for chaincode development)
- Multiple computers connected on same LAN (for multi-node testing)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/e-certificate-system.git
cd e-certificate-system
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

3. Start the development environment:
```bash
docker-compose up -d
```

4. Initialize the blockchain network:
```bash
./blockchain/scripts/start-network.sh
```

5. Deploy the chaincode:
```bash
./blockchain/scripts/deploy-chaincode.sh
```

6. Access the API documentation:
```
http://localhost:8000/docs
```

## 🌐 Deployment Across Multiple Nodes

### University Node Setup

1. Configure the university node:
```bash
cd deployment/local/university
./setup.sh
```

2. Start university services:
```bash
docker-compose -f docker-compose.university.yaml up -d
```

### Student Node Setup

1. Configure the student node:
```bash
cd deployment/local/student
./setup.sh
```

2. Start student services:
```bash
docker-compose -f docker-compose.student.yaml up -d
```

### Verifier Node Setup

1. Configure the verifier node:
```bash
cd deployment/local/verifier
./setup.sh
```

2. Start verifier services:
```bash
docker-compose -f docker-compose.verifier.yaml up -d
```

## 📝 Technical Implementation Details

### Certificate Lifecycle

1. **Creation**: University staff creates a certificate with student data
2. **Issuance**: Certificate is signed and committed to the blockchain
3. **Storage**: Certificate metadata and hash are stored on-chain
4. **Access**: Students can view certificates assigned to them
5. **Verification**: Third parties can verify authenticity through the verifier API

### Smart Contract Functions

- `IssueCertificate(id, data, signature)`
- `GetCertificate(id)`
- `VerifyCertificate(id, hash)`
- `GetCertificateHistory(id)`
- `GetCertificatesByStudent(studentId)`

### API Endpoints

- **University API**: `/api/v1/certificates/issue`, `/api/v1/certificates/revoke`
- **Student API**: `/api/v1/certificates/my-certificates`, `/api/v1/certificates/{cert_id}`
- **Verifier API**: `/api/v1/certificates/verify/{cert_id}`
- **Authentication**: `/api/v1/auth/login`, `/api/v1/auth/register`

## 🔒 Security Considerations

- All communications between nodes are encrypted using TLS
- Certificate private keys are stored securely
- Role-based access control for all API endpoints
- Audit logging for all certificate operations
- Digital signatures ensure certificate authenticity

## 📊 Project Roadmap

### Current Version (v0.1)
- Basic certificate issuance and verification
- Local network deployment
- Simple web interface

### Future Enhancements
- Mobile application for students
- QR code integration for easy verification
- Integration with student information systems
- Certificate templates and customization
- Multi-signature certificates requiring approval from multiple authorities
- Cloud deployment with Kubernetes

## 👥 Contributors

- [Your Name](https://github.com/yourusername) - Project Lead

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.