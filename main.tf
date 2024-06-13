locals {
  lambda_name   = "get_current_time"
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "lambda_role" {
  name               = "lambda-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "archive_file" "lambda" {
  source_file = "src/${local.lambda_name}.py"
  output_path = "${local.lambda_name}.zip"

  type        = "zip"
}

resource "aws_lambda_function" "lambda" {
  function_name     = "${local.lambda_name}"
  filename          = data.archive_file.lambda.output_path
  handler           = "${local.lambda_name}.handler"

  role              = aws_iam_role.lambda_role.arn
  runtime           = "python3.9"

  source_code_hash  = data.archive_file.lambda.output_base64sha256
}
