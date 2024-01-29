class CatMonitor:
    catid = ["C1", "C2", "C3", "C4", "C5"] #list of strings
    catname = ["Tabby", "Kitty", "Tommy", "Tikki", "Tammy"] # list of strings
    catage = [3, 1, 2, 6, 7]
    averageAge = (sum(catage)/len(catage)) # float
    oldestAge = max(catage) # int

# def stands for define
    
def newCat():
    # Part E
    # ask user to input new cat name and age to be appended to the list
    newCatId = str(input("Enter the ID of the new cat: "))
    newCatName = input("Enter the name of the new cat: ")
    newCatAge = int(input("Enter the age of the new cat: "))
    CatMonitor.catid.append(newCatId)
    CatMonitor.catname.append(newCatName)
    CatMonitor.catage.append(newCatAge)
    newaverageAge = (sum(CatMonitor.catage)/len(CatMonitor.catage)) # float
    print(CatMonitor.catid)
    print(CatMonitor.catname)
    print(CatMonitor.catage)
    print(newaverageAge)

def catidandname():
    for i in range(len(CatMonitor.catid)):
        print({CatMonitor.catid[i] : CatMonitor.catname[i]})

def catidandage():
    for i in range(len(CatMonitor.catid)):
        print({CatMonitor.catid[i] : CatMonitor.catage[i]})


newCat()
catidandname()
catidandage()