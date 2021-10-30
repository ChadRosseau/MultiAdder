print("Instructions: Input the category number followed by the hours.")
print("Example: 2 4.56")
print("Type 'results' to have current results reported.")

categories = [0] * 10

def printResults():
    for cat, hour in enumerate(categories):
        if hour != 0:
            print(f"Category {cat}: {hour} hours")
    print("")

while True:
    value = input("Please input your category and hours: ")
    if "results" in value.lower(): 
        ()
        continue
    try:
        split = value.split(" ")
        cat = int(split[0])
        hour = 2 + float(split[1])
    except:
        print("Invalid command, please try again")
        continue

    categories[cat] += hour
    print(f"\n{hour} hours added to category {cat}.\n")

