sample = "de90a5"
print(tuple((int(sample[i:i+2], 16) for i in range(0, len(sample), 2))))