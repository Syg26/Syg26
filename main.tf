provider "aws" {
  region = "ap-south-1"  # Free tier is available in most regions, this is safe
}

resource "aws_instance" "free_tier_ec2" {
  ami           = "ami-02d26659fd82cf299" # Amazon Linux 2 AMI (HVM), SSD Volume Type (for us-east-1)
  instance_type = "t2.micro"             # Free-tier eligible

  tags = {
    Name = "FreeTierEC2"
  }
}
