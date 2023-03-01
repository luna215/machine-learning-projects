import pickle



def generate():
    """Generate a piano a MIDI file"""
    with open("data/notes", 'rb') as filepath:
        notes = pickle.load(filepath)

    # Get all pitch names
    pitch_names = sorted(set(item for item in notes))
    n_vocab = len(set(notes))

    network_input, normalized_input = prepare_sequences(notes, pitch_names, n_vocab)
    model = create_network(normalized_input, n_vocab)
    prediction_output = generate_notes(model, network_input, pitch_names, n_vocab)
    create_midi(prediction_output)

def prepare_sequences(notes, pitch_names, n_vocab):
    """Prepare the sequences used by the Neural Network"""
    pass

def create_network(network_input, n_vocab):
    """Create the structure of the Neural Network"""
    pass

def generate_notes(model, network_input, pitch_names, n_vocab):
    """Generate notes from the Neural network based on a sequence of notes"""
    pass

def create_midi(prediction_output):
    """
    Convert the output from the prediction to notes and create a MIDI 
    file from the notes
    """
    pass

if __name__ == "__main__":
    generate()