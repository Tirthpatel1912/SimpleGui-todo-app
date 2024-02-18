with open("./assets/binaryfile1img.jpg", "rb") as bin_file:
    bytes_value = bin_file.read()

with open("./assets/new_binaryfile.jpg", "wb") as bin1_file:
    bin1_file.write(bytes_value)
