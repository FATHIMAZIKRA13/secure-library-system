from app import app, db
from app.models import User

with app.app_context():
    # Delete old admin if exists (to avoid conflicts)
    User.query.filter_by(username='admin').delete()
    db.session.commit()

    admin = User(
        username='admin',
        email='admin@library.com',
        role='admin'
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()

    print("✅ Admin user created successfully!")
    print("Email    : admin@library.com")
    print("Password : admin123")
    print("Role     : admin")
    print("\nYou can now login!")