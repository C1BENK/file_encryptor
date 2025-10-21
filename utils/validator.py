import os
import re
import secrets
import string
import hashlib

class Validator:
    def __init__(self):
        pass
    
    def file_exists(self, file_path: str) -> bool:
        """Check if file exists"""
        return os.path.isfile(file_path)
    
    def folder_exists(self, folder_path: str) -> bool:
        """Check if folder exists"""
        return os.path.isdir(folder_path)
    
    def is_readable(self, file_path: str) -> bool:
        """Check if file is readable"""
        return os.access(file_path, os.R_OK)
    
    def is_writable(self, file_path: str) -> bool:
        """Check if file is writable"""
        return os.access(file_path, os.W_OK)
    
    def is_strong_password(self, password: str) -> bool:
        """Check if password is strong"""
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        # At least 3 of 4 criteria
        criteria_met = sum([has_upper, has_lower, has_digit, has_special])
        return criteria_met >= 3
    
    def check_password_strength(self, password: str) -> dict:
        """Comprehensive password strength analysis"""
        analysis = {
            'length': {'passed': len(password) >= 8, 'score': min(len(password) * 2, 20)},
            'uppercase': {'passed': any(c.isupper() for c in password), 'score': 10},
            'lowercase': {'passed': any(c.islower() for c in password), 'score': 10},
            'numbers': {'passed': any(c.isdigit() for c in password), 'score': 10},
            'special_chars': {'passed': any(c in string.punctuation for c in password), 'score': 10},
            'common_patterns': {'passed': not self._is_common_pattern(password), 'score': 20}
        }
        
        total_score = sum(item['score'] for item in analysis.values() if item['passed'])
        
        if total_score >= 70:
            rating = "Very Strong"
        elif total_score >= 50:
            rating = "Strong"
        elif total_score >= 30:
            rating = "Moderate"
        else:
            rating = "Weak"
        
        analysis['overall'] = {'score': total_score, 'rating': rating}
        return analysis
    
    def generate_password(self, length: int = 12, include_symbols: bool = True, include_numbers: bool = True) -> str:
        """Generate a strong random password"""
        characters = string.ascii_letters
        
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        if not characters:
            characters = string.ascii_letters + string.digits
        
        while True:
            password = ''.join(secrets.choice(characters) for _ in range(length))
            if self.is_strong_password(password):
                return password
    
    def generate_hash(self, password: str) -> str:
        """Generate SHA-256 hash of password"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _is_common_pattern(self, password: str) -> bool:
        """Check for common password patterns"""
        common_patterns = [
            r'^[0-9]+$',  # All numbers
            r'^[a-zA-Z]+$',  # All letters
            r'^[a-z]+$',  # All lowercase
            r'^[A-Z]+$',  # All uppercase
            r'123456',  # Sequential numbers
            r'password',  # Common words
            r'qwerty',  # Keyboard patterns
        ]
        
        password_lower = password.lower()
        return any(re.search(pattern, password_lower) for pattern in common_patterns)
