import os
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Product, Catagorie, ProductItem
from ..forms import ProductForm, AddProductItemForm
from directie.models import Leverancier

class AddStockViewTestCase(TestCase):

    def setUp(self):
        # Create a sample category if needed
        self.category = Catagorie.objects.create(name='Sample Category')
        self.leverancier = Leverancier.objects.create(bedrijfsnaam='Sample Leverancier', telefoon=1234567890,)


    def test_add_stock_view(self):
        # Create a sample image file for testing file upload
        # Get the directory of the current script (assuming this code is inside your test script)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Specify the path to your image file relative to the current script
        image_path = os.path.join(current_dir, 'test_images', 'logo.png')

        
        with open(image_path, 'rb') as f:
            image_content = f.read()

        image_file = SimpleUploadedFile("logo.png", image_content, content_type="image/png")

        # Data for the product form
        product_data = {
            'name': 'Test Product',
            'category': self.category.id,
            'EAN': '1234567890123',
            'afbeelding': image_file,
        }

        # Data for the product item form
        product_item_data = {
            'houdsbaarheiddatum': '2021-01-01',
            'leverancier': self.leverancier.id,
        }

        # Post data to the view
        response = self.client.post(reverse('add-stock'), {**product_data, **product_item_data, 'voorraad': 3})
        

        # Check if the view redirected successfully
        self.assertEqual(response.status_code, 302)

        # Check if the view redirected successfully
        self.assertEqual(response.status_code, 302)

        # Check if the product and product items are created
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(ProductItem.objects.count(), 3)

        # Optional: You can check other conditions as well, e.g., the redirected URL, content of the response, etc.

    # Add more test cases as needed
