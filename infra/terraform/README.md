# Infrastructure (M6)

Pick ONE cloud. Suggested files:

| File | Contents |
|------|----------|
| `main.tf` | provider, remote state backend (S3 + DynamoDB lock / GCS bucket) |
| `network.tf` | VPC, private subnets for DB + Redis, public for the load balancer |
| `database.tf` | managed Postgres 16 with pgvector enabled, automated backups |
| `cache.tf` | managed Redis |
| `storage.tf` | private bucket for documents, CORS for presigned GETs |
| `compute.tf` | API service + worker service from the same image, different command |
| `secrets.tf` | provider API keys + JWT secret in the cloud secret manager, never in tfvars |
| `outputs.tf` | API URL, bucket name |

Budget option: one small VM running `docker compose` + nightly `pg_dump` to the bucket.
Document the managed version as the scale-up path. Set a billing alert first.
