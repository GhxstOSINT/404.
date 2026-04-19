from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# The beautifully styled HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gringotts Internal Network</title>
    <style>
        body {
            background-color: #0a0a0a;
            color: #d4af37; /* Gold */
            font-family: 'Book Antiqua', Palatino, serif;
            margin: 0;
            padding: 0;
            display: flex;
            height: 100vh;
        }
        .sidebar {
            width: 250px;
            background-color: #141414;
            border-right: 2px solid #d4af37;
            padding: 20px;
            box-shadow: 5px 0 15px rgba(0,0,0,0.8);
        }
        .sidebar h2 {
            text-align: center;
            border-bottom: 1px solid #d4af37;
            padding-bottom: 10px;
            font-size: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .sidebar a {
            display: block;
            color: #b08d28;
            text-decoration: none;
            margin: 15px 0;
            font-size: 16px;
            transition: 0.3s;
        }
        .sidebar a:hover {
            color: #fff;
            text-shadow: 0 0 5px #d4af37;
        }
        .main-content {
            flex-grow: 1;
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 36px;
            margin: 0;
            letter-spacing: 4px;
            text-shadow: 2px 2px 4px #000;
        }
        .parchment-container {
            background-color: #fdf5e6; /* Old paper color */
            color: #2b2b2b;
            width: 80%;
            max-width: 800px;
            min-height: 400px;
            padding: 30px;
            border-radius: 5px;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 20px rgba(0,0,0,0.7);
            font-family: 'Courier New', Courier, monospace;
            font-size: 16px;
            white-space: pre-wrap;
            border: 1px solid #c2a878;
        }
    </style>
</head>
<body>

    <div class="sidebar">
        <h2>Public Records</h2>
        <a href="/?parchment=rates.txt">» Exchange Rates</a>
        <a href="/?parchment=goblin_schedule.txt">» Shift Schedule</a>
        <a href="/?parchment=history.txt">» Bank History</a>
    </div>

    <div class="main-content">
        <div class="header">
            <h1>GRINGOTTS BANK</h1>
            <p>Internal Document Retrieval System</p>
        </div>
        
        <div class="parchment-container">{{ content }}</div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    requested_file = request.args.get('parchment', 'rates.txt')
    
    # THE FLAW: Blindly joining paths without stripping ../
    base_dir = os.path.abspath('public')
    target_path = os.path.join(base_dir, requested_file)
    
    try:
        with open(target_path, 'r') as f:
            file_content = f.read()
    except Exception as e:
        file_content = f"Magical Error: The requested parchment could not be found or summoned.\n\nPath attempted: {requested_file}"
        
    return render_template_string(HTML_TEMPLATE, content=file_content)

if __name__ == '__main__':
    print("Starting Gringotts Deluxe Portal on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000)
