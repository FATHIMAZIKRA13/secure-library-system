from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Database tables created/verified")
    print("🚀 Starting Secure Library System...")
    app.run(debug=False)   # debug=False for production