# Special Counter
# Demonstrates the break and continue statements

count = 0

while True:
    count += 1
    # end lop if count is greater than 10
    if count > 10:
        break
    # On skip le 5
    if count == 5:
        continue
    print(count)

input("\n\nPress enter to quit")
        
