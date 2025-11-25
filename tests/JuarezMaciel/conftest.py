import pytest
from client import TMDbClient

@pytest.fixture
def client():
    TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZDA4N2E4ZDgyZTdiZDllNTUzMzEzMTc2YTgzODhjZCIsIm5iZiI6MTc2Mzg2MDgzMC45MjIsInN1YiI6IjY5MjI2MTVlMjhmMDRlNGMxOWRjZjhiZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hGTM8QnAfjrekrlFULxkbwupIHEEPTLBGYdD-Mn6bWQ"
    return TMDbClient(TOKEN)
