import string

def is_pangram(str):
  # Create a set of all lowercase letters
  alphabet_set = set(string.ascii_lowercase)

  # Convert input string into lowercase and create a set of characters
  input_set = set(str.lower())

  # Check if all alphabet letters are present in the input set
  return alphabet_set.issubset(input_set)

# Example usage

test_string = input("Enter the input string:")
result = is_pangram(test_string)
print(f"Is the string pangram? Answer is {result}")
