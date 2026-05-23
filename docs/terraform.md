# Terraform Infrastructure as Code

## Objective

Automate AWS infrastructure provisioning using Terraform.

---

# Why Terraform Is Important

Manual cloud provisioning:
- is error-prone
- difficult to reproduce
- hard to scale
- operationally inefficient

Terraform enables:
- declarative infrastructure
- version-controlled infrastructure
- reproducible deployments
- automated provisioning

---

# Terraform Components

## provider.tf

Defines AWS provider configuration.

---

## variables.tf

Stores reusable infrastructure variables.

---

## main.tf

Defines:
- EC2 instance
- security groups
- networking rules

---

## outputs.tf

Displays infrastructure outputs such as public IP.

---

# Terraform Workflow

## Initialize Terraform

```bash
terraform init
```

---

## Validate Configuration

```bash
terraform validate
```

---

## Preview Infrastructure Changes

```bash
terraform plan
```

---

## Create Infrastructure

```bash
terraform apply
```

---

## Destroy Infrastructure

```bash
terraform destroy
```

---

# Infrastructure Provisioned

- Ubuntu EC2 server
- HTTP access
- SSH access
- security groups

---

# Concepts Learned

- Infrastructure as Code
- declarative infrastructure
- automated provisioning
- Terraform state management
- cloud automation
- reproducible infrastructure