import unittest
from application.run import app  # Import your Flask app
from application.manage_globals.main import translate  # Assuming your translation module is named translation_module

class TestTranslation(unittest.TestCase):
    def test_translation(self):
        input_language = "english"  # Example input language
        output_language = "spanish"  # Example output language
        text_to_translate = "Hello"  # Example text to translate
        
        # Call the translate function
        translated_text = translate(input_language, output_language, text_to_translate)
        
        # Assert that the translated text is not empty
        self.assertIsNotNone(translated_text)
        # Add more assertions as needed
        
class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'index.html', response.data)

    def test_global_language(self):
        response = self.app.get('/languages/global')
        self.assertEqual(response.status_code, 200)
        # Assert further based on the expected response

    def test_local_language(self):
        response = self.app.get('/languages/local')
        self.assertEqual(response.status_code, 200)
        # Assert further based on the expected response

    def test_translation(self):
        # Mocking request args for translation
        with app.test_request_context('/translate?globalLang=english&localLang=spanish&dataText=hello'):
            response = app.full_dispatch_request()
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            # Assert further based on the expected response

if __name__ == '__main__':
    unittest.main()