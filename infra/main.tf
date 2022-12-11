# stateful AWS resources

resource "random_id" "suffix" {
  keepers = {
    name = "chalice-example"
  }
  byte_length = 8
}

provider "aws" {
  max_retries = 10
}

resource "aws_s3_bucket" "chalice" {
  bucket = "chalice-example-${random_id.suffix.hex}"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

resource "aws_s3_bucket_public_access_block" "block" {
  bucket = aws_s3_bucket.chalice.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
