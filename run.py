from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully")
    print("🚀 Secure Library System is running...")
    app.run(host="0.0.0.0", port=5000, debug=False)