# get-current-time

Uses Terraform to stand up a simple AWS lambda that when executed, returns the current timestamp in JSON format.

A GHA workflow is included that runs some simple tests for both the lambda response and the infrastructure configuration. The action can be run manually, in addition to automatically on `push`.
