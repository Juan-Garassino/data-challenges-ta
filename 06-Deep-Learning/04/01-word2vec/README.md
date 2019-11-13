# Word embedding with word2vec

In this notebook, we will look at word2vec, a technique for word embedding.

The goal of word2vec is to provide a mapping from the dictionary of words present in a text to vectors of fixed dimension. The main motivation is that working on words directly is not possible (except with one-hot encoding in really large dimensions which do not behave well).

There are two ways to train a word2vec model. The first is to use continuous bag of words (CBOW). In this CBOW setting, the text is preprocessed to build:
- small sets (e.g. size 5) of neighborhing words in the text
- one other neighboring word in the text.
and it trains a neural network to predict this neighboring word from the other close words.
Example: text = 'the cat climbed the tree'
The bag of words and other word could be:
- 'the', 'climbed' -> cat
- 'cat', 'the' -> climbed
- 'climbed', 'tree' -> 'the'

To do so, the network learns en embedding i.e. a function which maps each word to a continuous vector in dimension 64. Then there is one dense layer and the network outputs a softmax on the number of words.

The second way is skip-gram, where this time, given a single word for context, the network attempts to find several words that are likely to occur next to it.

