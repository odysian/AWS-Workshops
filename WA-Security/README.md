# Security

- Created [permBoundary.json](permBoundary.json) to restrict EC2 and Lambda actions to us-east-1 and us-west-1
- Created [devPolicy.json](devPolicy.json) for developer role to allow developers to create policies and roles with prefix app1 only if the [`permBoundary`](permBoundary.json) policy is attached.
- Created [iamReadList.json](iamReadList.json) to allow IAM list and read actions