from app import app, db
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()                    # Create tables on startup
        print("✅ Database tables initialized")
    print("🚀 Secure Library System running on Railway!")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)