from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

@app.route('/')
def hello():
    client_ip = request.remote_addr
    logging.info(f"===== NEW REQUEST =====")
    logging.info(f"Received request from: {client_ip}")
    
    for header, value in request.headers.items():
        logging.info(f"Header: {header}, Value: {value}")
    
    for cookie, value in request.cookies.items():
        logging.info(f"Cookie: {cookie}, Value: {value}")

    user_agent = request.user_agent
    logging.info(f"Browser: {user_agent.browser}")
    logging.info(f"Browser Version: {user_agent.version}")
    logging.info(f"Platform: {user_agent.platform}")
    logging.info(f"Language: {user_agent.language}")
    logging.info(f"String: {user_agent.string}")
    
    logging.info(f"===== END REQUEST =====")

    return 'Your hamster points have been multiplied! 🐹🚀\nUpdates usually take about an hour to propagate'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
