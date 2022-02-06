from unittest import TestCase
from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test_db'

app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()
        
    def tearDown(self):
        db.session.rollback()
        
class FlaskTests(TestCase):
    def test_redirect_from_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 302)
            self.assertIn('</h1>', html)