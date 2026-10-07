import os
import sys
from app import create_app, db
from app.seed_data import seed_database

app = create_app()

def init_db():
    """Ensure database tables and initial verified DIET institutional data exist."""
    with app.app_context():
        try:
            db.create_all()
            seed_database()
            print("================================================================")
            print("  NEXCAMPUS - Dhanekula Institute of Engineering & Technology   ")
            print("================================================================")
            print("  Database initialized & seeded with verified institutional data.")
            print("  Demo Access Credentials:")
            print("    * Admin:   admin@diet.ac.in   / Admin@123")
            print("    * Faculty: faculty@diet.ac.in / Faculty@123")
            print("    * Student: student@diet.ac.in / Student@123")
            print("================================================================")
        except Exception as e:
            print(f"Error initializing database: {e}", file=sys.stderr)

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() in ['true', '1']
    print(f"Starting NexCampus application at http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=debug)
