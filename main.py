import requests
import time
import sys
import os
import codecs
import uuid
from platform import system
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store running tasks globally
tasks = {}

@app.route('/', methods=['GET', 'POST'])
def send_messages():
    if request.method == 'POST':
        filexx = request.files['txtFile1']
        tokens = [token.decode('utf-8').strip() for token in filexx.readlines()]
        num_tokens = len(tokens)

        requests.packages.urllib3.disable_warnings()

        def cls():
            if system() == 'Linux':
                os.system('clear')
            else:
                if system() == 'Windows':
                    os.system('cls')

        cls()

        def liness():
            print('\u001b[37m' + '---------------------------------------------------')

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'
        }

        liness()

        access_tokens = [token.strip() for token in tokens]

        convo_id = request.form.get('threadId')  # Retrieve the conversation ID from the form data
        filex = request.files['txtFile']
        messages = [codecs.decode(message, 'utf-8').strip() for message in filex.readlines()]

        num_messages = len(messages)
        max_tokens = min(num_tokens, num_messages)

        haters_name = request.form.get('kidx')
        speed = int(request.form.get('time'))

        liness()

        # Generate a unique task ID
        task_id = str(uuid.uuid4())
        tasks[task_id] = True

        def message_sender():
            while tasks.get(task_id, False):
                try:
                    for message_index in range(num_messages):
                        if not tasks.get(task_id, False):
                            break

                        token_index = message_index % max_tokens
                        access_token = access_tokens[token_index]

                        message = messages[message_index].strip()

                        url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                        parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                        response = requests.post(url, json=parameters, headers=headers)

                        current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                        if response.ok:
                            print("[+] Message {} of Convo {} sent by Token {}: {}".format(
                                message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                            print("  - Time: {}".format(current_time))
                            liness()
                            liness()
                        else:
                            print("[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                                message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                            print("  - Time: {}".format(current_time))
                            liness()
                            liness()
                        time.sleep(speed)

                    print("\n[+] All messages sent. Restarting the process...\n")
                except Exception as e:
                    print("[!] An error occurred: {}".format(e))

        # Start the message sender in a new thread
        import threading
        threading.Thread(target=message_sender).start()

        return jsonify({"status": "Task started", "task_id": task_id})

    return '''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abhay Pratap Singh Supremacy</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body{
            background: url(https://i.postimg.cc/3Ncpzk64/85485e159080e54619c084488465f5ac.jpg);
        }
        .container{
            max-width: 500px;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin: 0 auto;
            margin-top: 0px;
        }
        .header{
            text-align: center;
            border: 2px solid rgb(255, 0, 0);
            animation: blink 1s linear infinite;
            padding-bottom: 0px;
            margin-bottom: 0px;
            font-weight: bold;
            margin: 0 auto;
        }
        .btn-submit{
            width: 100%;
            margin-top: 10px;
        }
        .footer{
            text-align: center;
            margin-top: 0px;
            color: #888;
        }
        .notification {
        	position: fixed;
        	top: 0;
        	left: 0;
        	width: 100%;
        	background-color: #f8f8f8;
        	padding: 10px;
        	text-align: center;
        	font-weight: bold;
        }
        @keyframes blink {
    0% {
      border-color: rgb(255, 0, 0);
    }
    50% {
      border-color: rgb(0, 255, 0);
    }
    100% {
      border-color: rgb(0, 0, 255);
    }
  }
        	
    </style>
</head>
<body>
    <header class="header mt-4">
    <h1 class="mb-3">[[ ♡Welcome In My Kingdom♡ ]]</h1>
    <h1 class="mt-3">☛︎Black Marvel Rulexx☚︎</h1>
    </header>
 
    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="txtFile1">Select Your Token File:</label>
                <input type="file" class="form-control" id="txtFile1" name="txtFile1" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="threadId">Enter Convo/Inbox UID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="txtFile">Select Your Abusing File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="kidx">Enter Your Hater's Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="time">Enter Delay Time in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit" id="submitBtn" onclick="alert('Thank you for submitting your details! Your program is running, please refresh the page for a new program!')">Submit Your Details</button>
        </form>
        <br>
        <form action="/stop" method="post">
            <div class="mb-3">
                <label for="taskId">Enter Task ID to Stop:</label>
                <input type="text" class="form-control" id="taskId" name="taskId" required>
            </div>
            <button type="submit" class="btn btn-danger btn-submit">Stop Task</button>
        </form>
    </div>
    <div class="footer">
        <p>© Developed By Abhay pratap Siingh</p>
        <p><a href="https://www.facebook.com/profile.php?id=100001696735334" target="_blank"></a></p>
        <p><a href="https://www.facebook.com/profile.php?id=100001696735334" target="_blank"></a></p>
        <div class="social-icons">
            <a href="https://github.com/4bh4y8055" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://www.facebook.com/profile.php?id=100001696735334" target="_blank"><i class="fab fa-facebook"></i></a>
            <a href="https://www.instagram.com/abhaysiingh01/" target="_blank"><i class="fab fa-instagram"></i></a>
        </div>
        <p>© 2024 All rights reserved</p>
    </div>
 
    <script>
        function showNotification() {
            const notification = document.createElement('div');
            notification.classList.add('notification');
            notification.textContent = 'Your Offline Server Is Running ❤️!!';
            document.body.appendChild(notification);
            setTimeout(() => {
                notification.remove();
            }, 3000);
        }
 
        const submitBtn = document.getElementById('submitBtn');
        submitBtn.addEventListener('click', showNotification);
    </script>
</body>
</html>
    '''

@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('taskId')
    if task_id in tasks:
        tasks[task_id] = False
        return jsonify({"status": "Task stopped", "task_id": task_id})
    else:
        return jsonify({"status": "Invalid task ID"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5450, debug=True, threaded=True)
      
