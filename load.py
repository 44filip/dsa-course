# Honestly not sure how this works, will research later on Treehouse
def load_numbers(file_name):
  numbers = []
  with open(file_name) as f:
    for line in f:
      numbers.append(int(line))
  return numbers

# Same goes for this snippet of code
def load_strings(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]