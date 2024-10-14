import time

zeit_in_ms_seit_1970 = time.time()
print(zeit_in_ms_seit_1970)

localtime = time.localtime()
print(f"{localtime[3]:02d}:{localtime[4]:02d}:{localtime[5]:02d}")

uhrzeit = time.strftime("%H:%M:%S")
print(f"Das ist die Uhrzeit mit strftime: {uhrzeit}")

print(type(localtime))