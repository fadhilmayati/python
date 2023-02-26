import password_gen

def test_generate_password():
    # Test with length of 8 and no special characters
    assert len(password_gen.generate_password(8, False)) == 8

    # Test with length of 16 and special characters
    assert len(password_gen.generate_password(16, True)) == 16 + 1  # includes one special character
