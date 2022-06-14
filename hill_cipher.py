import numpy
 
#$
#$ HILL CIPHER!
#$ Author: Nicholas Develle
#$ 2022 - GPL2
#$


#
#_Initial input
#
prompt_string = input("Enter word to be encrypted [incl ., ?, ' ']: ")
prompt_array = list(prompt_string.lower())
_on_top_boolean = True
p_matrix = numpy.zeros( (2, int((len(prompt_array) + 1) / 2)))

#
#_Convert entry to plaintext 'P' matrix
#
i = 0
current = 0
while current < len(prompt_array):
  height = 0 if _on_top_boolean else 1
  if prompt_array[current] == ' ':
    p_matrix[height][i] = 28
  elif prompt_array[current] == '?':
    p_matrix[height][i] = 27
  elif prompt_array[current] == '.':
    p_matrix[height][i] = 26
  else:
    p_matrix[height][i] = ord(prompt_array[current]) - 97
    
  if (_on_top_boolean):
    _on_top_boolean = False
  else:
    _on_top_boolean = True
    i = i + 1
  current = current + 1
if not _on_top_boolean:
  p_matrix[len(p_matrix) - 1][len(p_matrix[0]) - 1] = 28

print()
print("Plaintext: ")
print(p_matrix)

#
#_KEY Matrix for decode and KEVINV for encode
#
KEY = numpy.array([[6, 4],
                   [4, 3]])
KEYINV = numpy.linalg.inv(KEY)

print()
print("Key and Inverse: ")
print(KEY)
print(KEYINV)

#
#_Encrypt to 'C' cryptic  matrix
#
c_matrix = KEYINV.dot(p_matrix)

print()
print("Encrypted matrix: ")
print(c_matrix)

#
#_Decrypt to 'R' recieved matrix
#
r_matrix = KEY.dot(c_matrix)

# Clock-29
i = 0
while i < len(r_matrix):
  j = 0
  while j < len(r_matrix[0]):
    if r_matrix[i][j] > 29 or r_matrix[i][j] < 0:
      r_matrix[i][j] = (r_matrix[i][j] % 29)
    j = j + 1
  i = i + 1
#

# this fixes floating issues
i = 0
while i < len(r_matrix):
  j = 0
  while j < len(r_matrix[0]):
    r_matrix[i][j] = round(r_matrix[i][j])
    j = j + 1
  i = i + 1
  
print()
print("Decrypted matrix: ")
print(r_matrix)

recieved_length = 2 * len(r_matrix[0]) 

recieved_array = list()
_on_top_boolean = True

#
#_Make readable
#
i = 0
current = 0
while i < len(r_matrix[0]):
  height = 0 if _on_top_boolean else 1
  if round(r_matrix[height][i]) == 28:
    recieved_array.append(' ')
  elif round(r_matrix[height][i]) == 27:
    recieved_array.append('?')
  elif round(r_matrix[height][i]) == 26:
    recieved_array.append('.')
  else:
    recieved_array.append(chr(round(r_matrix[height][i]) + 97))
  
  if _on_top_boolean:
    _on_top_boolean = False
  else:
    _on_top_boolean = True
    i = i + 1

print()
print()
print()
print("MESSAGE ARRIVED: ", end='')
print(''.join(recieved_array))