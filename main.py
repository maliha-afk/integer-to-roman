def int_to_roman(num):
  
  roman_map = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
  }
  result = ""
  for value, symbol in roman_map.items():
    while num >= value:
      result += symbol
      num -= value
  return result

integer_input = int(input("enter your number:"))
roman_value = int_to_roman(integer_input)
print(f"The Roman numeral equivalent of {integer_input} is {roman_value}")
