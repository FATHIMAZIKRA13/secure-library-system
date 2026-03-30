from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # This ensures tables are created on startup
    print("🚀 Server starting at http://127.0.0.1:5000")
    app.run(debug=True)