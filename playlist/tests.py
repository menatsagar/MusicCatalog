from django.test import TestCase

from playlist.models import Artist

# Create your tests here.
    # create an artist with missing name
        # create an artist with valid data
def test_create_artist_with_valid_data(self):
    artist = Artist(name="John Doe", genre="Rock", dob="1980-01-01")
    assert artist.name == "John Doe"
    assert artist.genre == "Rock"
    assert artist.dob == "1980-01-01"
def test_create_artist_with_missing_name(self):
    with pytest.raises(ValueError):
        Artist(genre="Rock", dob="1980-01-01")
        