## Language model

In this notebook, we will build a caracter-based language model i.e. a model which given a sequence of caracters predicts the next one. We will limit the use of high-level functions, and use a simple LSTM to predict the next caracter.

We will construct pairs of sentences and characters which follow, and train an LSTM to predict this next character.

### This notebook should be open in a google collab environment, because it requires GPU acceleration. but it does not require external data, so you won't have to mount your drive !

#### Note that, on GPU, the LSTM layer can be replaced by the CuDNNLSTM layer, which is a much faster GPU LSTM implementation.