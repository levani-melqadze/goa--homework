
lamp = {
    "color": "white",
    "type": "LED",
    "height": 40,
    "material": "plastic",
    "power": 9
}


print("Keys:")
for key in lamp:
    print(key)

# 3. Value-ების გამოყვანა
print("\nValues:")
for value in lamp.values():
    print(value)

# 4. Key-ები და Value-ების ერთად გამოყვანა
print("inKeys and Values:")
for key in lamp:
    print(key,  lamp[key])
