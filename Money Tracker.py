# my money tracker thing i made
# because i keep forgetting where my money goes

stuff_i_bought = []

def main():
    print("hey")
    print("this is my money tracker")
    
    while True:
        print()
        print("what to do?")
        print("1 add thing i bought")
        print("2 delete thing")
        print("3 show all")
        print("4 total money spent")
        print("5 exit")
        
        c = input("> ")
        
        if c == "1":
            add_thing()
        elif c == "2":
            delete_thing()
        elif c == "3":
            show_all()
        elif c == "4":
            show_total()
        elif c == "5":
            print("Goodbye!")
            break
        else:
            print("what? just 1-5")

def add_thing():
    print("ok adding new thing")
    d = input("when? ")
    w = input("what? ")
    m = get_money()
    
    thing = {"date": d, "what": w, "money": m}
    stuff_i_bought.append(thing)
    print(f"added {w} - ${m}")

def get_money():
    while True:
        try:
            m = float(input("how much $"))
            if m <= 0:
                print("seriously?")
                continue
            return m
        except:
            print("no just number like 10.50")

def delete_thing():
    if len(stuff_i_bought) == 0:
        print("nothing to delete")
        return
    
    show_all()
    
    try:
        n = int(input("which number to delete? "))
        if n < 1 or n > len(stuff_i_bought):
            print("not a valid number")
            return
        
        thing = stuff_i_bought[n-1]
        del stuff_i_bought[n-1]
        print(f"deleted {thing['what']}")
    except:
        print("error")

def show_all():
    if len(stuff_i_bought) == 0:
        print("empty")
        return
    
    print()
    print("my spending:")
    total = 0
    for i in range(len(stuff_i_bought)):
        thing = stuff_i_bought[i]
        print(f"{i+1}. {thing['date']} - {thing['what']} - ${thing['money']:.2f}")
        total += thing['money']
    
    print(f"total: ${total:.2f}")

def show_total():
    if len(stuff_i_bought) == 0:
        print("nothing spent")
        return
    
    total = 0
    for thing in stuff_i_bought:
        total += thing['money']
    
    print(f"total spent: ${total:.2f}")

# start the thing
if __name__ == "__main__":
    main()
