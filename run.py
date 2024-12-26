from app import create_app

# Create an instance of the Flask app
app = create_app()

# Run the app on localhost with debugging enabled
if __name__ == "__main__":
    app.run(debug=True)