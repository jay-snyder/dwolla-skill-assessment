run "valid_source_file_path" {
  command = plan

  assert {
    condition     = data.archive_file.lambda.source_file == "src/get_current_time.py"
    error_message = "Lambda file path did not match expected"
  }
}

run "valid_function_name" {
  command = plan

  assert {
    condition     = aws_lambda_function.lambda.function_name == "get_current_time"
    error_message = "Lambda function name did not match expected"
  }
}
