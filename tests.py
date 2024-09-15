def test_extract_emails():
    # Sample text with emails
    text = "Here are some emails: test@example.com, admin@website.co.uk, user.name@company.org"
    
    # Expected output
    expected_emails = ["test@example.com", "admin@website.co.uk", "user.name@company.org"]
    
    # Call the extract_emails function
    extracted_emails = extract_emails(text)
    
    # Assert that the extracted emails match the expected result
    assert extracted_emails == expected_emails, f"Expected {expected_emails}, but got {extracted_emails}"
