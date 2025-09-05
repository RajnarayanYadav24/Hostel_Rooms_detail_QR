import qrcode

# Hostel room details
room_no = "216"
max_capacity = 3
students = [
    {"Name": "Harsh Vardhan", "Branch": "MCA", "Year": "2nd", "Fee Status": {"DSW Fee":"Paid","Hostel Fee":"Paid","Mess Fee":"Pending"}},
    {"Name": "Aman Kannaujiya", "Branch": "MCA", "Year": "2nd", "Fee Status":{"DSW Fee":"Paid","Hostel Fee":"Paid","Mess Fee":"Paid"}},
    
]

# Prepare formatted text
details = f"Room No: {room_no}\n"
details += f"Capacity: {max_capacity}\n"
details += f"Total Occupide Students: {len(students)}\n\n"

for i in range(max_capacity):
    details += f"Student {i+1}:\n"
    if i < len(students):
      student = students[i]
      details += f"  Name: {student['Name']}\n"
      details += f"  Branch: {student['Branch']}\n"
      details += f"  Year: {student['Year']}\n"
      details += f"  Fee Status:\n"
      for fee_type, status in student["Fee Status"].items():
          details += f"    {fee_type}: {status}\n"
      details += "\n"
    else:
      details += "  Not Occupied\n"
    details += "\n"
         

# Generate QR code with formatted details
qr = qrcode.make(details)

# Save QR code image
qr.save("Room_216_qr.png")

print("QR code for Room 203 generated successfully!")
