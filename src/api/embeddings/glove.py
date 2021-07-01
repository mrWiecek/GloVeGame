import torch
import torchtext.vocab
import logging

class WordVectors(object):

    def __init__(self):
        logging.warning("Loading Vectors...")
        self.vectors = torchtext.vocab.GloVe(name = '6B', dim = 100)
        logging.warning("Vectors loaded")

    def _get_vector(self, word):
        assert word in self.vectors.stoi, f'*{word}* is not in the vocab!'
        return self.vectors.vectors[self.vectors.stoi[word]]

    def _closest_words(self, vector, n = 10):
        distances = [(closest_word, torch.dist(vector, self._get_vector(closest_word)).item())
                    for closest_word in self.vectors.itos]

        return sorted(distances, key = lambda w: w[1])[:n]

    def _parse_output(self, output):
        return [{"name": item[0], "distance": item[1]} for item in output]

    def closest_words(self, word, n = 10):
        vector = self._get_vector(word)

        return self._parse_output(self._closest_words(vector, n))

    def analogy(self, word1, word2, word3, n=5):
        
        #get vectors for each word
        word1_vector = self._get_vector(word1)
        word2_vector = self._get_vector(word2)
        word3_vector = self._get_vector(word3)
        
        #calculate analogy vector
        analogy_vector = word2_vector - word1_vector + word3_vector
        
        #find closest words to analogy vector
        candidate_words = self._closest_words(analogy_vector, n+3)
        
        #filter out words already in analogy
        candidate_words = [(word, dist) for (word, dist) in candidate_words
                        if word not in [word1, word2, word3]][:n]

        return self._parse_output(candidate_words)
