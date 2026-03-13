@"
# Unit tests for file validation
# Test valid and invalid file_ids
# Test dangerous characters
import pytest
from lambdas.file_distribution.validators import validate_file_id, validate_user_ip

def test_valid_file_id():
    assert validate_file_id("valid_file_id") == True        

def test_invalid_file_id():
    assert validate_file_id("") == False
    assert validate_file_id("invalid../file_id") == False
    assert validate_file_id("invalid/file_id") == False
    assert validate_file_id("invalid\\file_id") == False

def test_valid_user_ip():
    assert validate_user_ip("192.168.1.1") == True

def test_invalid_user_ip():
    assert validate_user_ip("") == False
    assert validate_user_ip("256.0.0.1") == False
    assert validate_user_ip("192.168.1") == False
"@ | Out-File -FilePath tests/test_validators.py