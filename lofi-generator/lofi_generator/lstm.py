"""
Module prepare midi file data and feeds it
to the Neural Network for training
"""

def train_network():
    """Train a Neural Network to generate music"""

    notes = get_notes()

    # Get amount of pitch names
    n_vocab = len(set(notes))

    network_input, network_output = prepare_sequence(notes, n_vocab)

    model = create_network(network_input, n_vocab)

    train(model, network_input, network_output)

def get_notes():
    """
    Get all the notes and chords from the midi files in
    ./midi_songs direcotry
    """
    pass


def prepare_sequence(notes, n_vocab):
    """Prepare the sequence used by the Neural Network"""
    pass


def create_network(network_input, n_vocab):
    """Create the structure of the Neural Network"""
    pass


def train(model, network_input, network_output):
    """Train the Neural Network"""
    pass