
from pr7_bundle_b import pr7_when as tmod, pr7_calcbox as mmod, pr7_lucky as rmod, pr7_uider as uidmod, pr7_fileside as fmod, pr7_dirpeek as xmod
import math

def menu():
    print("\n========================")
    print("Welcome to Multi-Utility Toolkit (variant 2)")
    print("========================")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("========================")

def dt_menu():
    print("Datetime and Time Operations:")
    print("1. Display current date/time")
    print("2. Difference between two ISO dates")
    print("3. Format a date string")
    print("4. Stopwatch")
    print("5. Countdown")
    print("6. Back")

def math_menu():
    print("Mathematical Operations:")
    print("1. Factorial")
    print("2. Compound Interest")
    print("3. Trig values")
    print("4. Areas")
    print("5. Back")

def rand_menu():
    print("Random Data Generation:")
    print("1. Random number")
    print("2. Random list sample")
    print("3. Password")
    print("4. OTP")
    print("5. Back")

def file_menu():
    print("File Operations:")
    print("1. Create file (x)")
    print("2. Write file (w)")
    print("3. Read file (r)")
    print("4. Append file (a)")
    print("5. Back")

def explore_menu():
    print("Explore Module Attributes:")
    print("1. math module")
    print("2. random module")
    print("3. toolkit package module list")
    print("4. Back")

def run():
    while True:
        menu()
        c = input("Enter your choice: ").strip()
        if c == "1":
            dt_menu()
            ch = input("Enter: ").strip()
            if ch == "1":
                print(tmod.current_dt())
            elif ch == "2":
                d1 = input("first date (YYYY-MM-DD): "); d2 = input("second date (YYYY-MM-DD): ")
                print(tmod.date_gap(d1+" 00:00:00", d2+" 00:00:00"))
            elif ch == "3":
                d = input("date time ISO (YYYY-MM-DD HH:MM:SS): ")
                fmt = input("format string (default %d-%m-%Y): ") or "%d-%m-%Y"
                print(tmod.pretty_date(d, fmt))
            elif ch == "4":
                print("elapsed:", tmod.timer_sw(1), "sec")
            elif ch == "5":
                print(tmod.down_timer(3))
        elif c == "2":
            math_menu(); ch = input("Enter: ").strip()
            if ch == "1":
                n = int(input("n: ")); print(mmod.get_fact(n))
            elif ch == "2":
                p=float(input("P: ")); r=float(input("R%: ")); t=float(input("T: ")); print(mmod.interest_calc(p,r,t))
            elif ch == "3":
                a=float(input("angle in degree: ")); print(mmod.do_trig(a))
            elif ch == "4":
                sh=input("shape (circle/rect/tri): ")
                if sh=="circle":
                    print(mmod.shape_area("circle", float(input("r: ")))) 
                elif sh=="rect":
                    print(mmod.shape_area("rect", float(input("w: ")), float(input("h: ")))) 
                else:
                    print(mmod.shape_area("tri", float(input("b: ")), float(input("h: ")))) 
        elif c == "3":
            rand_menu(); ch=input("Enter: ").strip()
            if ch == "1":
                print(rmod.any_number())
            elif ch == "2":
                print(rmod.mix_list())
            elif ch == "3":
                ln=int(input("length: ")); print(rmod.gen_pass(ln))
            elif ch == "4":
                print(rmod.otp_make())
        elif c == "4":
            print(uidmod.uuid4_make())
        elif c == "5":
            file_menu(); ch=input("Enter: ").strip()
            if ch == "1":
                nm=input("file name: "); 
                try:
                    print(fmod.new_file(nm))
                except FileExistsError:
                    print("already exists")
            elif ch == "2":
                nm=input("file name: "); txt=input("data: "); print(fmod.file_write(nm, txt))
            elif ch == "3":
                nm=input("file name: "); 
                try:
                    print(fmod.file_read(nm))
                except FileNotFoundError:
                    print("missing file")
            elif ch == "4":
                nm=input("file name: "); txt=input("append: "); print(fmod.file_append(nm, txt))
        elif c == "6":
            explore_menu(); ch=input("Enter: ").strip()
            if ch == "1":
                import math as M; print(xmod.see_dir(M))
            elif ch == "2":
                import random as R; print(xmod.see_dir(R))
            elif ch == "3":
                import pr7_bundle_b as P; print([m for m in dir(P) if m.startswith("pr7_")])
        elif c == "7":
            print("Goodbye!"); break
        else:
            print("Invalid.")

if __name__ == "__main__":
    run()
