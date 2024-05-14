import pytest
import User_Registration_Problem as user_registration

class TestUserRegistration:
    def test_first_name(self):
        result= user_registration.validate_first_name("Tejas")
        assert result == True

    def test_last_name(self):
        result= user_registration.validate_last_name("Tonpe")
        assert result == True

    def test_email(self):
        result= user_registration.validate_email("tejas.tonpe@contractpod.com")
        assert result == True

    def test_mobile_no(self):
        result= user_registration.validate_mobile_no("917414927068")
        assert result == False

    def test_password(self):
        result= user_registration.validate_password("tonpe@12345")
        assert result == True

if __name__=="__main__":
    pytest.main()

