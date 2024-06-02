# create a user with valid email and password
from datetime import date, timedelta

from django.test import TestCase



from .models import (
    Artist,
)


class ArtistModelTest(TestCase):
   


    def test_create_artist(self):
        artist = Artist.objects.create(
            name = "sagar", 
            genre = "dev",
            dob = date(day=3, month=10, year=1998)
        )

        self.assertIsInstance(artist, Artist)
        self.assertEqual(artist.name, "sagar")
        self.assertEqual(artist.genre, "dev")
        self.assertEqual(artist.dob, date(day=3, month=10, year=1998))


    