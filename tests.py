import subprocess
import sys
import re
import os
import difflib

# -----------------------------
# Remove comments + clean code
# -----------------------------
def remove_comments_space(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    # Remove all whitespace (spaces, tabs, newlines, etc.)
    text = "".join(text.split())
    return text


def print_result(test_name, passed):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")


# -----------------------
# File Checks
# -----------------------

REQUIRED_FILES = [
        "restaurant.h",
        "restaurant.cpp",
        "menuItem.h",
        "menuItem.cpp",
        "main.cpp",
        "Output.txt",
        "drink.txt",
        "food.txt",
        "input.txt",
        "food.h",
        "food.cpp",
        "drink.h",
        "drink.cpp"
    ]
EXEC = "./restaurant"
# -----------------------------
# Check required files
# -----------------------------
def check_files():
    print("Checking required files...")
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:", ", ".join(missing))
        return False
    return True


# -----------------------------
# Check menuItem.h file
# -----------------------------
def check_menuItem_header():
    print("Checking menuItem.h...")
    with open("menuItem.h") as f:
        header = remove_comments_space(f.read())

    if "protected" not in header:
        print("Missing: protected access specifier")
        return False
    
    if "virtualvoiddisplay()" not in header:
        print("Missing: virtual void display()")
        return False
    
    if "virtual~MenuItem()" not in header:
        print("Missing: virtual ~MenuItem()")
        return False
    
  
    return True


# -----------------------------
# Check menuItem.cpp file
# -----------------------------
def check_menuItem_cpp():
    print("Checking menuItem.cpp...")
    with open("menuItem.cpp") as f:
        cpp = remove_comments_space(f.read())

    if "MenuItem::~MenuItem()" not in cpp:
        print("Missing: Destructor")
        return False
    if "voidMenuItem::display()" not in cpp:
        print("Missing: display() implementation")
        return False
    if "virtual"  in cpp:
        print("Remove: virtual keyword")
        return False
    
 
    return True
 
# -----------------------------
# Check food.h file
# -----------------------------
def check_food_header():
    print("Checking food.h...")
    with open("food.h") as f:
        header = remove_comments_space(f.read())

    if "classFood:publicMenuItem" not in header:
        print("Missing: inheritance from MenuItem")
        return False
    
    if "voiddisplay()" not in header:
        print("Missing: void display()")
        return False
    
    if "~Food()" not in header:
        print("Missing:  ~Food()")
        return False
    
  
    return True

# -----------------------------
# Check food.cpp file
# -----------------------------
def check_food_cpp():
    print("Checking food.cpp...")
    with open("food.cpp") as f:
        cpp = remove_comments_space(f.read())

    if "Food::~Food()" not in cpp:
        print("Missing: Destructor")
        return False
    if "voidFood::display()" not in cpp:
        print("Missing: display() implementation")
        return False
  
    
 
    return True
   
# -----------------------------
# Check drink.h file
# -----------------------------
def check_drink_header():
    print("Checking drink.h...")
    with open("drink.h") as f:
        header = remove_comments_space(f.read())

    if "classDrink:publicMenuItem" not in header:
        print("Missing: inheritance from MenuItem")
        return False
    
    if "voiddisplay()" not in header:
        print("Missing: void display()")
        return False
    
    if "~Drink()" not in header:
        print("Missing:  ~Drink()")
        return False
    
  
    return True

# -----------------------------
# Check drink.cpp file
# -----------------------------
def check_drink_cpp():
    print("Checking drink.cpp...")
    with open("drink.cpp") as f:
        cpp = remove_comments_space(f.read())

    if "Drink::~Drink()" not in cpp:
        print("Missing: Destructor")
        return False
    if "voidDrink::display()" not in cpp:
        print("Missing: display() implementation")
        return False
  
    
 
    return True
# -----------------------------
# Check restaurant.h file
# -----------------------------
def check_restaurant_header():
    print("Checking restaurant.h...")
    with open("restaurant.h") as f:
        header = remove_comments_space(f.read())

    if "voidoperator+(constMenuItem&)" not in header:
        print("Missing: void operator+(const MenuItem&)")
        return False
    
    if "Restaurant&operator=(constRestaurant&)" not in header:
        print("Missing: Restaurant& operator = (const Restaurant&)")
        return False
    
    if "friendostream&operator<<(ostream&,constRestaurant&)" not in header:
        print("Missing: friend ostream& operator<<(ostream&, const Restaurant&)")
        return False
    
    if "displayRestaurantData" in header:
        print("Remove: displayRestaurantData method declaration")
        return False
    
    if "maxItem" not in header:
        print("Missing: maxItem variable declaration")
        return False
    
    
    if "MenuItem*items" not in header:
        print("Missing: MenuItem* items declaration")
        return False
    if "MenuItem*getItems()" not in header:
        print("Missing: MenuItem* getItems()")
        return False
    if "~Restaurant()" not in header:
        print("Missing: ~Restaurant() Destructor")
        return False

    return True

    



# -----------------------------
# Check restaurant.cpp file
# -----------------------------
def check_restaurant_cpp():
    print("Checking restaurant.cpp...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments_space(f.read())

    if "voidRestaurant::operator+(constMenuItem&" not in cpp:
        print("Missing: void Restaurant::operator+(const MenuItem&)")
        return False
    
    if "Restaurant&Restaurant::operator=(constRestaurant&" not in cpp:
        print("Missing: Restaurant& Restaurant::operator = (const Restaurant&)")
        return False
    
    if "ostream&operator<<(ostream&" not in cpp:
        print("Missing: ostream& operator<<(ostream&, const Restaurant&)")
        return False
    
    if "displayRestaurantData" in cpp:
        print("Remove: displayRestaurantData method")
        return False
    
    
    if "MenuItem*Restaurant::getItems" not in cpp:
        print("Missing: MenuItem* MenuItem::getItems")
        return False
    if "Restaurant::~Restaurant()" not in cpp:
        print("Missing: Restaurant::~Restaurant() Destructor")
        return False
    
    
    if cpp.count("newMenuItem") <5:
        print("There should be at least 5 dynamic allocation of MenuItem array using new keyword in the cpp file.")
        return False
    if cpp.count("delete[]items") <3:
        print("Missing: delete [] items check 1) destructor, 2)in the assignment operator overload and 3)add method")
        return False
    return True
    
 


 





# -----------------------------
# Check main file
# -----------------------------
def check_main():
    print("Checking main.cpp...")

    with open("main.cpp", "r") as f:
        content = remove_comments_space(f.read())
    
    if "new" and "delete" not in content:
        print("Either missing new or delete keyword. Needs to dynamically allocate and deallocate properly.")
        return False

    
    return True
    
    


# -----------------------------
# Build project
# -----------------------------
def build():
    print("Building project...")

    result = subprocess.run(["make"], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Build failed:\n")
        print(result.stderr)
        return False 
    return True


# -----------------------------
# Run program
# -----------------------------
def run_program():
    print("Running program...")

    if not os.path.exists(EXEC):
        print(" Executable not found")
        sys.exit(1)
    with open("input.txt", "r") as fin:
        result = subprocess.run([EXEC], stdin=fin,capture_output=True, text=True,timeout=10)

    if result.returncode != 0:
        print(" Program crashed")
        print(result.stderr)
        sys.exit(1)

    print("Program output captured.")
    return result.stdout.strip()


# ---------------------------
# Run make clean
# ---------------------------
def check_make_clean():
    try:
        subprocess.run(
            ["make", "clean"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        obj_files = [f for f in os.listdir(".") if f.endswith(".o")]
        exe_files = os.path.exists(EXEC)
        # if not os.path.exists(EXEC):
            
        #     sys.exit(1)
        print ("Checking make clean...")

        if exe_files:
            print("Executable restaurant is not removed.")
            return False 

        if obj_files:
            print("Not all the .o files are removed.")
            return False

        return True

    except Exception:
        return False


# -----------------------------
# Load expected output
# -----------------------------
def load_expected():
    with open("Output.txt", "r") as f:
        return f.read().strip()


# -----------------------------
# Compare outputs
# -----------------------------
def compare_output():
    print("Comparing output with Output.txt...")

    actual = run_program()
    expected = load_expected()

    if actual == expected:
        print("Output matches exactly!")
        return True
    print("Output does NOT match!\nCheck output.txt")
    
# print(" Output does NOT match!\n")

    diff = difflib.unified_diff(
    expected.splitlines(),
    actual.splitlines(),
    fromfile="Expected (Output.txt)",
    tofile="Actual (Program Output)",
    lineterm=""
    )

    print("Difference Report:")
    print("  --- : Expected output")
    print("  +++ : Your program output")
    print("  -   : Line missing or incorrect in your output")
    print("  +   : Line produced by your program that differs from expected")
    print("      : Lines without a symbol match in both outputs")
    print()

    for line in diff:
        if line.startswith("@@"):
            continue
        print(line)
    return False

# -----------------------------
# Main
# -----------------------------
def main():
    total = 0
    passed = 0

    

    tests = [
        ("Required Files Exist", check_files),
        ("MenuItem Header Declarations", check_menuItem_header),
        ("MenuItem CPP Implementations", check_menuItem_cpp),
        ("Restaurant Header Declarations", check_restaurant_header),
        ("Restaurant CPP Implementations", check_restaurant_cpp),
        ("Food Header Declarations", check_food_header),
        ("Food CPP Implementations", check_food_cpp),
        ("Drink Header Declarations", check_drink_header),
        ("Drink CPP Implementations", check_drink_cpp),
        ("main.cpp Structure", check_main),
        ("Makefile Builds", build),
        ("Executable Created and Output Matching", compare_output),
        ("Make Clean Works", check_make_clean),
        
        
    ]

    for name, func in tests:
        total += 1
        result = func()
        print_result(name, result)

        if result:
            passed += 1

    if passed == total:
        print("\n======================")
        print("Project Passed")
        print("======================")
        sys.exit(0)
    else:
        print("\n======================")
        print("Project Failed")
        print("======================")
        sys.exit(1)
   


if __name__ == "__main__":
    main()