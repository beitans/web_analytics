import re


string = "Jacqueline Scheifel <jscheifel98@web.de>"

# prog = re.compile(r"([a-z\d\.]+)@([a-z\.]+)")
# output = prog.match(string)


output = re.findall(r"(([a-z\d\.]+)@([a-z\.]+))",string)
print(output)