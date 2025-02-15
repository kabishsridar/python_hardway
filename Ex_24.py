print("let's  practice everything.")
print('you\'d need to know \'about escapes with \\that do')
print('\n new lines and \t tabs.')
#now introducing\n to line feed
#now introducing\t to horizontal tab in this poem,it starts after some spaces
#now using three double quotes to print for many lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
and requires an explanation
\n\t\there there is none
"""

print("-----------------")
print(poem)
print("-----------------")


ten = 8+2+40-20-20
print(f"this should be {ten}")

#now introducing def funct.
def secret_formula(started):    
    ktm= started *50
    innova = ktm /100
    pulsar = innova/100
    return ktm , innova , pulsar

start_point= 1000
ktm , innova , pulsar = secret_formula(start_point)

#another way to format
print("with a starting point of : {}".format(start_point))

#the f in the print is used to assign the var
print(f"we'd have {ktm} ktm bikes, {innova} innova cars, and{pulsar} pulsar bikes.")


start_point = start_point/10
