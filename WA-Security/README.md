# Security
### Permission Boundaries for Role Creation

- Created [permBoundary.json](permBoundary.json) to restrict EC2 and Lambda actions to us-east-1 and us-west-1
- Created [devPolicy.json](devPolicy.json) for developer role to allow developers to create policies and roles with prefix app1 only if the [`permBoundary`](permBoundary.json) policy is attached.
- Created [iamReadList.json](iamReadList.json) to allow IAM list and read actions
- Created developer role with `permBoundary` and `iamReadList` policies, enabled require MFA
- Role ARN: arn:aws:iam::631353662337:role/developer-restricted-iam
- Role Link: https://signin.aws.amazon.com/switchrole?roleName=developer-restricted-iam&account=odysian
- Edited trust policy principal to allow IAM users in my account to switch to the role
- Created second role with [permBoundary](permBoundary.json) as permission boundary.
- Switched to role, checked EC2 dashboard to confirm everything worked correctly ✅
 **Summary: Created policies to restrict access, created developer role that allowed devs to create other roles granting access only to EC2 and Lambda.**