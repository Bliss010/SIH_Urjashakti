from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Chatbot knowledge base
knowledge_base = {
    "solar potential": "You can assess your rooftop's solar potential by using our interactive map. Just select your location, and the system will calculate the suitable area for solar panel installation.",
    "government subsidies": "Government subsidies can help reduce the cost of solar installations significantly. Visit the 'Subsidy Info' section on our platform for more details.",
    "installation process": "After assessing your rooftop potential, you can connect with our trusted local service providers for installation assistance.",
    "energy savings": "Switching to solar energy can save up to 20% annually on electricity costs depending on your usage and location.",
    "general": "Welcome to UrjaShakti! How can I assist you today? Type your query or select from the options below."
}

@app.route('/')
def index():
    # Serve the HTML chatbot interface
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    # Retrieve the response from the knowledge base or return a default message
    response = knowledge_base.get(
        message.lower(), 
        "I'm sorry, I don't have information on that. Please try rephrasing or contact support."
    )
    emit('response', response)

if __name__ == "__main__":
    # Run the Flask application with SocketIO support
    socketio.run(app, debug=True)
