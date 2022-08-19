import re

x="IN KLU AT KLU"
y=re.findall("KL",x)
print(x)
print(y)
z=re.search("IN",x)
print(z)
print(re.sub("IN","WHY",x))
print(re.split("KLU",x))


