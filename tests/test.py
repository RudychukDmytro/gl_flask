import unittest

from app import Vote, app, db


class TestApp(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        

    def test_vote(self):
        tester = app.test_client(self)
        response = tester.post('/vote', data=dict(vote='option1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        vote = Vote.query.filter_by(vote='option1').first()
        self.assertIsNotNone(vote)
        

if __name__ == '__main__':
    unittest.main()
