from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit
        # an empty list item, She hits enter on the empty input box

        # The homepage refreshes, and there is an error message saying that the list items cannont be blank

        # She tries again with some text for the item, which now works

        # Perversly, she now decides to submit a second blank list item

        # She rececies a similar warning on the list page

        # And she can correct it by filling some text in.
        self.fail('write me!')


