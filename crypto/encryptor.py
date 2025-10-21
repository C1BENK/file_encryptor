import os
import base64
import pyaes
import secrets
import hashlib

class FileEncryptor:
    def __init__(self):
        pass
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive AES key from password using PBKDF2"""
        # Simple key derivation using SHA256
        key = hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode(), 
            salt, 
            100000,  # iterations
            32  # key length for AES-256
        )
        return key
    
    def encrypt_file(self, file_path: str, password: str) -> str:
        """
        Encrypt a file with password using AES-256
        
        Args:
            file_path: Path to file to encrypt
            password: Encryption password
            
        Returns:
            str: Path to encrypted file
        """
        # Generate random salt and IV
        salt = secrets.token_bytes(16)
        iv = secrets.token_bytes(16)  # AES block size
        
        # Derive key from password
        key = self._derive_key(password, salt)
        
        # Read file data
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        # Create AES cipher in CBC mode
        aes = pyaes.AESModeOfOperationCBC(key, iv=iv)
        
        # Pad data to multiple of 16 bytes (AES block size)
        padding_length = 16 - (len(file_data) % 16)
        file_data += bytes([padding_length]) * padding_length
        
        # Encrypt data
        encrypted_data = b""
        for i in range(0, len(file_data), 16):
            block = file_data[i:i+16]
            encrypted_block = aes.encrypt(block)
            encrypted_data += encrypted_block
        
        # Create output path
        output_path = file_path + '.Wh04ami'
        
        # Write encrypted file (salt + iv + encrypted_data)
        with open(output_path, 'wb') as file:
            file.write(salt)    # 16 bytes
            file.write(iv)      # 16 bytes  
            file.write(encrypted_data)
        
        return output_path
    
    def encrypt_data(self, data: bytes, password: str) -> bytes:
        """
        Encrypt raw data with password
        
        Args:
            data: Data to encrypt
            password: Encryption password
            
        Returns:
            bytes: Encrypted data (salt + iv + encrypted_data)
        """
        salt = secrets.token_bytes(16)
        iv = secrets.token_bytes(16)
        
        key = self._derive_key(password, salt)
        aes = pyaes.AESModeOfOperationCBC(key, iv=iv)
        
        # Pad data
        padding_length = 16 - (len(data) % 16)
        data += bytes([padding_length]) * padding_length
        
        # Encrypt
        encrypted_data = b""
        for i in range(0, len(data), 16):
            block = data[i:i+16]
            encrypted_block = aes.encrypt(block)
            encrypted_data += encrypted_block
        
        return salt + iv + encrypted_data
