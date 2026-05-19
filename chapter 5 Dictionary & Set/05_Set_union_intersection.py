s1 = { 6,72,21,2}
s2 = {7,2,26,5}

print(s1.union(s2))
print(s1.intersection(s2))
  # ============================================
#        PYTHON SETS - COMPLETE PROGRAM
# ============================================

# ✅ SET BANAO
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("=" * 40)
print("        PYTHON SET OPERATIONS")
print("=" * 40)

print(f"\n🔵 Set A : {a}")
print(f"🟢 Set B : {b}")

# ============================================
# 1️⃣ ADD & UPDATE
# ============================================
print("\n--- ➕ ADD & UPDATE ---")

s = {1, 2, 3}
s.add(4)
print(f"add(4)       : {s}")       # {1, 2, 3, 4}

s.update([5, 6, 7])
print(f"update([5,6,7]) : {s}")    # {1, 2, 3, 4, 5, 6, 7}

# ============================================
# 2️⃣ REMOVE ELEMENTS
# ============================================
print("\n--- ➖ REMOVE ELEMENTS ---")

s = {1, 2, 3, 4, 5}
s.remove(3)
print(f"remove(3)    : {s}")       # {1, 2, 4, 5}

s.discard(99)
print(f"discard(99)  : {s}")       # No Error — {1, 2, 4, 5}

popped = s.pop()
print(f"pop()        : {popped} removed → {s}")

# ============================================
# 3️⃣ UNION
# ============================================
print("\n--- 🔗 UNION (|) ---")
print(f"A = {a}")
print(f"B = {b}")
print(f"A | B = {a.union(b)}")     # {1,2,3,4,5,6,7,8}

# ============================================
# 4️⃣ INTERSECTION
# ============================================
print("\n--- 🎯 INTERSECTION (&) ---")
print(f"A = {a}")
print(f"B = {b}")
print(f"A & B = {a.intersection(b)}")  # {4, 5}

# ============================================
# 5️⃣ DIFFERENCE
# ============================================
print("\n--- ➖ DIFFERENCE (-) ---")
print(f"A = {a}")
print(f"B = {b}")
print(f"A - B = {a.difference(b)}")    # {1, 2, 3}
print(f"B - A = {b.difference(a)}")    # {6, 7, 8}

# ============================================
# 6️⃣ SYMMETRIC DIFFERENCE
# ============================================
print("\n--- 🔄 SYMMETRIC DIFFERENCE (^) ---")
print(f"A = {a}")
print(f"B = {b}")
print(f"A ^ B = {a.symmetric_difference(b)}")  # {1,2,3,6,7,8}

# ============================================
# 7️⃣ SUBSET / SUPERSET / DISJOINT
# ============================================
print("\n--- 🔍 SUBSET | SUPERSET | DISJOINT ---")

x = {1, 2}
y = {1, 2, 3, 4}
z = {9, 10}

print(f"x = {x}, y = {y}, z = {z}")
print(f"x.issubset(y)    : {x.issubset(y)}")     # True
print(f"y.issuperset(x)  : {y.issuperset(x)}")   # True
print(f"x.isdisjoint(z)  : {x.isdisjoint(z)}")   # True

# ============================================
# 8️⃣ COPY
# ============================================
print("\n--- 📋 COPY ---")
original = {1, 2, 3}
copied   = original.copy()
copied.add(99)
print(f"Original : {original}")   # {1, 2, 3}  — safe!
print(f"Copied   : {copied}")     # {1, 2, 3, 99}

# ============================================
# 9️⃣ CLEAR
# ============================================
print("\n--- 🗑️ CLEAR ---")
temp = {1, 2, 3}
temp.clear()
print(f"After clear() : {temp}")   # set()

# ============================================
# 🔟 REAL LIFE EXAMPLE — Students
# ============================================
print("\n" + "=" * 40)
print("   🎓 REAL LIFE EXAMPLE - STUDENTS")
print("=" * 40)

class_A = {"Rahul", "Priya", "Amit", "Sara"}
class_B = {"Amit", "Sara", "Neha", "Ravi"}

print(f"\n📚 Class A : {class_A}")
print(f"📚 Class B : {class_B}")

print(f"\n Dono class mein (Common)  : {class_A & class_B}")
print(f" Koi bhi ek class mein     : {class_A | class_B}")
print(f" Sirf Class A mein         : {class_A - class_B}")
print(f" Sirf Class B mein         : {class_B - class_A}")
print(f" Sirf ek class mein (XOR)  : {class_A ^ class_B}")

print("\n" + "=" * 40)
print(" PROGRAM COMPLETE ")
print("=" * 40)


