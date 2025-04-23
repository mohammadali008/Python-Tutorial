text = " Python is Fun! "

print(text.strip())              # حذف فاصله‌ها
print(text.lower())              # حروف کوچک
print(text.replace("Fun", "Awesome"))  # جایگزینی

if "Python" in text:
    print("Yes, it contains Python!")

for ch in text:
    if ch.isupper():
        print(f"Uppercase: {ch}")
