from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()        # Ensure tables are created
        print("✅ Database tables initialized")
    print("🚀 Server starting...")
    app.run(debug=True)