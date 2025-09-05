import pandas as pd
import qrcode
import os

# Load Excel file (warden updates this)
# df = pd.read_excel("hostel_data.xlsx")
df = pd.read_excel("hostel_data.xlsx", engine="openpyxl")


# Group students by room
rooms = df.groupby("Room NO")

# Create folder for QR codes (if not exists)
os.makedirs("qr_codes", exist_ok=True)
max_capacity = 3
for room_no, students in rooms:
    # Prepare QR text
    qr_data = f"Room No: {room_no}\n\n"
    qr_data += f"Total Capacity of Student in Room: {max_capacity}\n"
    qr_data += f"Currently Occupied Students in Room: {len(students)}\n\n"

    for i, student in enumerate(students.itertuples(), 1):
        name = student.Name if student.Name != "-" else "Not Available"
        branch = student.Branch if student.Branch != "-" else "Not Available"
        year = student.Year if student.Year != "-" else "Not Available"
        phone = student.Phone if student.Phone != "-" else "Not Available"
        


        qr_data += f"Student {i}:\n"
        qr_data += f"  Name: {name}\n"
        qr_data += f"  Branch: {branch}\n"
        qr_data += f"  Year: {year}\n"
        qr_data += f"  Phone No: {phone}\n\n"

        # Fee Status
        qr_data += f"  Fee Status:\n"
        qr_data += f"      DSW Fee: {student._6}\n"      # 6th column → DSW Fee
        qr_data += f"      Hostel Fee: {student._7}\n"   # 7th column → Hostel Fee
        qr_data += f"      Mess Fee: {student._8}\n\n"   # 8th column → Mess Fee

    # Path for QR code
    qr_path = f"qr_codes/room_{room_no}.png"

    # ✅ Ensure overwrite: delete old file first
    if os.path.exists(qr_path):
        os.remove(qr_path)

    # Generate and save QR
    qr = qrcode.make(qr_data)
    qr.save(qr_path)

    print(f"♻️  QR updated for Room {room_no}: {qr_path}")
