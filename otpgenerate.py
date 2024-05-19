import pyotp

# Generate a secret key
secret_key = pyotp.random_base32()

# Create a TOTP object with a custom expiration interval (60 seconds)
totp = pyotp.TOTP(secret_key, interval=60)

# Generate and print the TOTP
print("Your OTP is:", totp.now())