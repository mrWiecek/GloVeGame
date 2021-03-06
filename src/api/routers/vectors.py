from fastapi import APIRouter
from embeddings.glove import WordVectors

vectors = WordVectors()
router = APIRouter()

@router.get("/closest/{word}")
async def get_closest_words(word: str):
    return vectors.closest_words(word)

@router.get("/analogy")
async def get_analogy(word1: str, word2: str, word3: str):
    return vectors.analogy(word1, word2, word3)
