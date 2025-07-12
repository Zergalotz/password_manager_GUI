import pytest
from unittest.mock import MagicMock, patch
import main
#Note to self: Ensure that the main.py file is in the same directory as this test file or adjust the import accordingly.
#Currently, the tests in this file are failing due to not being able to find Images/logo.png, which is used in main.py.

def test_generate_password_prints_message(capfd):
    main.generate_password()
    out, _ = capfd.readouterr()
    assert "Password generated!" in out

@patch("main.website_input")
@patch("main.email_username_input")
@patch("main.password_input")
def test_add_saved_password_writes_file(mock_password, mock_email, mock_website, tmp_path):
    # Setup mocks
    mock_website.get.return_value = "example.com"
    mock_email.get.return_value = "user@example.com"
    mock_password.get.return_value = "securepassword"
    mock_website.delete = MagicMock()
    mock_email.delete = MagicMock()
    mock_password.delete = MagicMock()
    mock_website.focus = MagicMock()
    mock_email.focus = MagicMock()
    mock_password.focus = MagicMock()

    # Patch open to write to a temp file
    file_path = tmp_path / "passwords.txt"
    with patch("builtins.open", lambda f, m: open(file_path, m)):
        main.add_saved_password()

    with open(file_path) as f:
        content = f.read()
    assert "example.com | user@example.com | securepassword" in content


