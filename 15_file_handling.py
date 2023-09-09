def count_word_frequencies(filename):
    """Count the frequency of each word in a file."""
    
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Open and read the file
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.split()

            # For each word in the line, update the word frequency
            for word in words:
                # Convert word to lowercase and remove any punctuation at the end
                word = word.lower().strip('.,!?()[]{}":;')
                # If the word is in the dictionary, increment its count by 1
                if word in word_freq:
                    word_freq[word] += 1
                # Otherwise, add the word to the dictionary with a count of 1
                else:
                    word_freq[word] = 1

    return word_freq


if __name__ == "__main__":
    filename = input("Please enter the filename: ")
    frequencies = count_word_frequencies(filename)
    for word, freq in frequencies.items():
        print(f"{word}: {freq}")
