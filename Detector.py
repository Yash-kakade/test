def detect_sequence(transitions):
    state_transitions = {}
    sequence = []
    initial_state = transitions[0][0] 


    for present_state, next_state, input_bit, output_bit in transitions:
        state_transitions[(present_state, input_bit)] = (next_state, output_bit)
        if output_bit == 1: 
            sequence.append(input_bit)


    last_transition = transitions[-1]
    detector_type = (
        "Non Overlapping Sequence Detector"
        if last_transition[1] == initial_state and last_transition[3] == 1
        else "Overlapping Sequence Detector"
    )
    
    detected_sequence = ''.join(sequence)
    return detected_sequence, detector_type

transitions1 = [
    ('a', 'b', '1', '0'),
    ('b', 'c', '0', '0'),
    ('c', 'a', '1', '1'),
]

transitions2 = [
    ('a', 'b', '1', '0'),
    ('a', 'a', '0', '0'),   
    ('b', 'a', '0', '0'),
    ('b', 'c', '1', '0'),
    ('c', 'd', '0', '0'),
    ('d', 'a', '0', '0'),
    ('d', 'b', '1', '1'),
]

# Test cases
sequence, detector_type = detect_sequence(transitions1)
print(sequence)
print(detector_type)  

sequence, detector_type = detect_sequence(transitions2)
print(sequence) 
print(detector_type)  
