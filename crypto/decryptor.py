import os
import hashlib
import pyaes  # ← TAMBAH INI!

class FileDecryptor:
    def __init__(self):
        pass
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive AES key from password using PBKDF2"""
        key = hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode(), 
            salt, 
            100000,  # iterations
            32  # key length for AES-256
        )
        return key
    
    def decrypt_file(self, file_path: str, password: str) -> str:
        """
        Decrypt an encrypted file with password
        """
        try:
            # Read encrypted file
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            # Extract salt (16 bytes), IV (16 bytes), and encrypted data
            if len(file_data) < 32:
                raise Exception("File is too short to be a valid encrypted file")
                
            salt = file_data[:16]
            iv = file_data[16:32]
            encrypted_data = file_data[32:]
            
            # Derive key from password
            key = self._derive_key(password, salt)
            
            # Create AES cipher in CBC mode
            aes = pyaes.AESModeOfOperationCBC(key, iv=iv)
            
            # Decrypt data
            decrypted_data = b""
            for i in range(0, len(encrypted_data), 16):
                block = encrypted_data[i:i+16]
                decrypted_block = aes.decrypt(block)
                decrypted_data += decrypted_block
            
            # Remove padding
            if decrypted_data:
                padding_length = decrypted_data[-1]
                if padding_length <= 16:
                    decrypted_data = decrypted_data[:-padding_length]
            
            # Create output path
            if file_path.endswith('.Wh04ami'):
                output_path = file_path[:-10]  # Remove .encrypted
            else:
                name, ext = os.path.splitext(file_path)
                output_path = f"{name}_decrypted{ext}"
            
            # Add counter if file exists
            counter = 1
            original_output = output_path
            while os.path.exists(output_path):
                name, ext = os.path.splitext(original_output)
                output_path = f"{name}_{counter}{ext}"
                counter += 1
            
            # Write decrypted file
            with open(output_path, 'wb') as file:
                file.write(decrypted_data)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}")
