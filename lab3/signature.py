# Define the parameters
a = 9
b = 11
c = 256  # MaxValue + 1
t0 = 201
n = 8  # Number of bits in a byte

# Define the document (message) for which we want to calculate sums
document = '1999000'

# Function to calculate KSumm
def calculate_KSumm(document):
    # Calculate the sum of ASCII values of characters in the document
    K = sum(ord(char) for char in document)

    # Check if K is greater than MaxValue and apply the condition
    MaxVal = c - 1
    KSumm = K if K <= MaxVal else K % c

    return KSumm

# Function to calculate SummKodBuk with gamma encoding
def calculate_SummKodBuk(document):
    # Initialize variables
    t = t0
    SummKodBuk = 0

    # Calculate the gamma encoding
    for char in document:
        # Calculate Ti using the recurrence formula
        Ti = (a * t + b) % c

        # Calculate Yi by XORing character code with Ti
        Yi = ord(char) ^ Ti

        # Add Yi to the SummKodBuk
        SummKodBuk += Yi

        # Update t for the next iteration
        t = Ti

    # Check if SummKodBuk is greater than MaxValue and apply the condition
    MaxVal = c - 1
    SummKodBuk = SummKodBuk if SummKodBuk <= MaxVal else SummKodBuk % c

    return SummKodBuk

# Calculate KSumm and SummKodBuk for the given document
KSumm = calculate_KSumm(document)
SummKodBuk = calculate_SummKodBuk(document)

# Print the results
print(f'KSumm: {KSumm}')
print(f'SummKodBuk: {SummKodBuk}')
