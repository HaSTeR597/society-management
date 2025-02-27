from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder="static")

# Temporary storage for complaints (Use a database in production)
complaints = []

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create-account')
def create_account():
    return render_template('create-account.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "123" and password == "123":
            print("✅ Redirecting to:", url_for('admin_dashboard'))
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin-login.html', error="❌ Invalid credentials")

    return render_template('admin-login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin-dashboard.html')

@app.route('/complaint')
def complaint():
    return render_template('complaint.html')

@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    name = request.form['name']
    complaint_text = request.form['complaint']
    
    complaints.append({'name': name, 'complaint': complaint_text})  # Store complaint

    return redirect(url_for('view_complaints'))  # Redirect to complaints list

@app.route('/complaints')
def view_complaints():
    return render_template('complaints.html', complaints=complaints)

@app.route('/view-bills')
def view_bills():
    return render_template('view_bills.html')

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')


# Print all registered routes for debugging
print("\n📌 Registered Routes in Flask:")
with app.test_request_context():
    for rule in app.url_map.iter_rules():
        print(f"➡ {rule} → {rule.endpoint}")

if __name__ == '__main__':
    app.run(debug=True)
