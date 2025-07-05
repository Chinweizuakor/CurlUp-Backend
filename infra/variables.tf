variable "prefix" {
  default = "curlup"
}

variable "aws_region" {
  default = "us-east-2"
}

variable "instance_type" {
  default = "t2.medium"
}

variable "ami_id" {
  description = "AMI ID for Ubuntu 22.04 in us-east-2"
  type        = string
}

variable "key_name" {
  description = "Name of the key pair"
  type        = string
}
