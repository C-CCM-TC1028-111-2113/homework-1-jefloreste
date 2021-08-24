def main (cost, messages, megas, mins):
    return (float)((cost*messages)+(cost*megas)+(cost*mins))

cost = 0.8
messages = int(input("How many messages were sent: "))
megas = float(input("How many megas were used: "))
mins = int(input("How many mins were spent: "))

print("Your total price is:", main (cost, messages, megas, mins))
