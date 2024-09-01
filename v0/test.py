from my import My

with open("example.my", "r") as file:
    code = file.read()

program = My(code)
print(program.run())