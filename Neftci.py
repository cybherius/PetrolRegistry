import base64
import hashlib
import zlib
import itertools
import random
import string

class PasswordObfuscator:
    def __init__(self):
        self.seed_value = 0xB4C0  # Valid hexadecimal value
        self.obfuscation_map = self._generate_obfuscation_map()
        
    def _generate_obfuscation_map(self):
        random.seed(self.seed_value)
        chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        shuffled = chars.copy()
        random.shuffle(shuffled)
        return dict(zip(chars, shuffled))
    
    def _reverse_map(self, mapping):
        return {v: k for k, v in mapping.items()}
    
    def _transform_data(self, data, transformation_func):
        return ''.join(transformation_func(c) for c in data)
    
    def _encode_layer_1(self, text):
        # First layer of encoding - Base64
        return base64.b64encode(text.encode()).decode()
    
    def _encode_layer_2(self, text):
        # Second layer - Character substitution
        return self._transform_data(text, lambda c: self.obfuscation_map.get(c, c))
    
    def _encode_layer_3(self, text):
        # Third layer - Hex representation
        return ''.join(f'{ord(c):02x}' for c in text)
    
    def _encode_layer_4(self, text):
        # Fourth layer - Compression
        compressed = zlib.compress(text.encode())
        return base64.b64encode(compressed).decode()
    
    def _decode_layer_4(self, text):
        # Reverse layer 4
        decoded = base64.b64decode(text.encode())
        return zlib.decompress(decoded).decode()
    
    def _decode_layer_3(self, text):
        # Reverse layer 3
        return ''.join(chr(int(text[i:i+2], 16)) for i in range(0, len(text), 2))
    
    def _decode_layer_2(self, text):
        # Reverse layer 2
        reverse_map = self._reverse_map(self.obfuscation_map)
        return self._transform_data(text, lambda c: reverse_map.get(c, c))
    
    def _decode_layer_1(self, text):
        # Reverse layer 1
        return base64.b64decode(text.encode()).decode()
    
    def obfuscate_password(self):
        # The actual password components
        components = [
            [66, 97, 107, 117],  # Baku
            [66, 108, 97, 99, 107],  # Black
            [71, 111, 108, 100],  # Gold
            [50, 48, 50, 53],  # 2025
            [33]  # !
        ]
        
        # Convert ASCII values to characters
        password = ''.join(''.join(chr(c) for c in component) for component in components)
        
        # Apply multiple layers of encoding
        layer1 = self._encode_layer_1(password)
        layer2 = self._encode_layer_2(layer1)
        layer3 = self._encode_layer_3(layer2)
        final_encoded = self._encode_layer_4(layer3)
        
        return final_encoded
    
    def reveal_password(self, encoded_data):
        # Reverse the encoding process
        layer4_decoded = self._decode_layer_4(encoded_data)
        layer3_decoded = self._decode_layer_3(layer4_decoded)
        layer2_decoded = self._decode_layer_2(layer3_decoded)
        password = self._decode_layer_1(layer2_decoded)
        
        return password

def generate_fake_data():
    """Generate fake data to make the code look more complex"""
    fake_hashes = [
        hashlib.md5("fake_data_1".encode()).hexdigest(),
        hashlib.sha256("fake_data_2".encode()).hexdigest(),
        hashlib.sha512("fake_data_3".encode()).hexdigest()
    ]
    
    fake_arrays = [
        [random.randint(0, 255) for _ in range(10)],
        [random.choice(string.ascii_letters) for _ in range(15)],
        [base64.b64encode(str(random.random()).encode()).decode() for _ in range(5)]
    ]
    
    return fake_hashes, fake_arrays

def perform_decoy_operations():
    """Perform operations that look important but are actually decoys"""
    # Create a large list of random numbers
    numbers = [random.randint(1000, 9999) for _ in range(100)]
    
    # Perform various operations that look complex
    transformed = list(map(lambda x: x * 2 - 7, numbers))
    filtered = list(filter(lambda x: x % 3 == 0, transformed))
    sorted_list = sorted(filtered, reverse=True)
    
    # More decoy operations
    matrix = [[i * j for j in range(5)] for i in range(5)]
    flattened = list(itertools.chain.from_iterable(matrix))
    
    return sorted_list, flattened

def main():
    # Generate fake data and perform decoy operations
    fake_hashes, fake_arrays = generate_fake_data()
    sorted_list, flattened = perform_decoy_operations()
    
    # Create the password obfuscator
    obfuscator = PasswordObfuscator()
    
    # Obfuscate the password
    encoded_password = obfuscator.obfuscate_password()
    
    # Finally, reveal and display the password
    password = obfuscator.reveal_password(encoded_password)
    print("Decoded Password:", password)

if __name__ == "__main__":
    main()
