from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-to app.  She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-to item striaght away

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        #1: Buy peacock feathers as an item in a to-do list

        # There is still a text box iviting her to add another item.  She enters "USe peacock feather to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.  Then she see that the site has generated a unique URL for her
        # there is some explanantory text to that effect

        # She visits that URL - her to-do list is still there.
        # Satisfied, she goes back to sleep

if __name__ == ' __main__':
    unittest.main(warnings='ignore')
