import hashlib

def calculate_hash(filename):
    try:
        with open(filename, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    except:
        return None

print("=== File Integrity Checker ===")
file = input("Enter file name: ")

hash1 = calculate_hash(file)

if hash1 is None:
    print("File not found!")
else:
    print("Original Hash:", hash1)
    input("Press Enter after modifying the file...")
    hash2 = calculate_hash(file)

    print("New Hash:", hash2)

    if hash1 == hash2:
        print("File is NOT changed.")
    else:
        print("WARNING! File has been modified.")
