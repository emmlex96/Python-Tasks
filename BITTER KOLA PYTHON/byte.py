bytes_input = int(input("Enter number of bytes: "))

kilobytes = bytes_input / 1024
megabytes = kilobytes / 1024
gigabytes = megabytes / 1024

    print(f"(bytes_input) bytes")
    print(f"= (kilobytes:.4f) KB")
    print(f"= (megabytes:.6f) MB")
    print(f"= (gigabytes:.9f) GB")
