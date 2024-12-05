# brainfuck interpreter
# by github@gunny091(https://chadol.xyz/)

print("BrainFuck Interpreter by chadol27")
print("Version 1.0")

import sys
import time
from readchar import readchar

# Error message
def error(text):
  print(f"ERROR: {text}")
  exit()

# Get file name
if len(sys.argv) < 2:
  error("need file name")

filename = sys.argv[1]

# try to read file
try:
  with open(filename, "r") as file:
    code = file.read()
except:
  error("reading file")

# running data
pointer = 0
memory = {}
cellSize = 8

def toCellSize(value):
  return value % (2 ** cellSize)

def get():
  if pointer in memory:
    return memory[pointer]
  else:
    return 0
  
def set(value):
  memory[pointer] = toCellSize(value)

def add(value):
  set(get() + value)

# print
def prt():
  try: print(chr(get()), end="")
  except: pass

# input
def inp():
  read = readchar()
  print(read, end="")
  set(ord(read))

# move pointer
def mvp(value):
  global pointer
  pointer += value

def run(code):
  index = 0
  codeLen = len(code)
  debug = "//#debug" in code
  if "/#32bit" in code:
    cellSize = 32

  # repeat for end
  while index < codeLen:
    try:
      thisChar = code[index]
      if not thisChar in "+-><.,[]":
        index += 1
        continue
      # debug
      if debug: print(f"index {index} thisChar {thisChar} get {get()} pointer {pointer} memory {memory}")

      # parse, run
      if thisChar == '+':
        add(1)

      elif thisChar == "-":
        add(-1)

      elif thisChar == ">":
        mvp(1)

      elif thisChar == "<":
        mvp(-1)

      elif thisChar == ".":
        prt()

      elif thisChar == ",":
        inp()

      # repeat
      elif thisChar == "[":
        if debug: print("repeat")
        if get() == 0:
          while code[index] != "]":
            if debug: print("repeat index", index)
            index += 1
            if index >= codeLen:
              index = codeLen - 1
              break
          if debug: print("repeat index", index)

      elif thisChar == "]":
        if debug: print("repeat")
        if get() != 0:
          while code[index] != "[":
            if debug: print("repeat index", index)
            index += -1
            if index < 0:
              index = 0
              break
          if debug: print("repeat index", index)
    # error handling
    except Exception as err:
      error(err)
    # next char
    index += 1

print("-----")
startTime = time.time()
run(code)
endTime = time.time()
print("\n-----")
print(f"{endTime - startTime}s")