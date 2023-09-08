import tkinter as tk

def get_user_information():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    education = education_text.get("1.0", tk.END).strip()
    experience = experience_text.get("1.0", tk.END).strip()
    skills = skills_entry.get()

    user_info = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "education": education,
        "experience": experience,
        "skills": skills.split(","),
    }
    return user_info

def generate_resume():
    user_info = get_user_information()
    resume = f"""
    ------------------ RESUME ------------------
    Name: {user_info["name"]}
    Email: {user_info["email"]}
    Phone: {user_info["phone"]}
    Address: {user_info["address"]}
    
    Education:
    {user_info["education"]}
    
    Experience:
    {user_info["experience"]}
    
    Skills:
    {", ".join(user_info["skills"])}
    ---------------------------------------------
    """
    resume_output.delete("1.0", tk.END)
    resume_output.insert(tk.END, resume)

# Create the main application window
app = tk.Tk()
app.title("Resume Generator Bot")

# Labels and Entry fields
name_label = tk.Label(app, text="Full Name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

phone_label = tk.Label(app, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

address_label = tk.Label(app, text="Address:")
address_label.pack()
address_entry = tk.Entry(app)
address_entry.pack()

education_label = tk.Label(app, text="Education:")
education_label.pack()
education_text = tk.Text(app, height=5)
education_text.pack()

experience_label = tk.Label(app, text="Work Experience:")
experience_label.pack()
experience_text = tk.Text(app, height=5)
experience_text.pack()

skills_label = tk.Label(app, text="Key Skills (comma-separated):")
skills_label.pack()
skills_entry = tk.Entry(app)
skills_entry.pack()

# Generate resume button
generate_button = tk.Button(app, text="Generate Resume", command=generate_resume)
generate_button.pack()

# Resume Output Text field
resume_output = tk.Text(app, height=20)
resume_output.pack()

# Start the GUI main loop
app.mainloop()
