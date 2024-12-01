from typing import List

#https://www.keiruaprod.fr/blog/2021/11/23/getting-ready-for-adventofcode-in-python.html

def input_as_string(filename: str) -> str:
  """
  returns the content of the input file as a string
  """
  with open(filename) as f:
    return f.read().rstrip("\n")

def input_as_lines(filename: str) -> List[str]:
  """
  returns a list where each line in the input file is an element of the list
  """
  return input_as_string(filename).split("\n")

def input_as_ints(filename: str) -> List[int]:
  """
  returns a list where each line in the input file is an element of the list, 
  converted into an integer
  """
  lines = input_as_lines(filename)
  line_as_int = lambda l: int(l.rstrip("\n"))
  return list(map(line_as_int, lines))
