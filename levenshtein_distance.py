import streamlit as st


def levenshtein_distance(source: str, target: str) -> int:
    """Levenshtein algorithm is used to find the minimum number 
    of changes for the source to be turned into target

    Args:
        source (str): the word to be converted
        target (str): the word to be converted into

    Returns:
        int: smallest number of changes
    """
    distances = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

    for i in range(len(source) + 1):
        distances[i][0] = i
    for j in range(len(target) + 1):
        distances[0][j] = j

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if (source[i - 1] == target[j - 1]):
                distances[i][j] = distances[i - 1][j - 1]
                continue
            left_value = distances[i][j - 1]
            up_value = distances[i - 1][j]
            diag_value = distances[i - 1][j - 1]

            if (left_value <= up_value and left_value <= diag_value):
                distances[i][j] = left_value + 1
            elif (up_value <= left_value and up_value <= diag_value):
                distances[i][j] = up_value + 1
            else:
                distances[i][j] = diag_value + 1
    return distances[len(source)][len(target)]


def load_vocab(file_path):
    """Load the vocabulary from the text file

    Args:
        file_path (_type_): text file path

    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='./data/vocab.txt')


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word: ')

    if st.button("Compute"):
        leven_distances = dict()
        # compute levenshtein distance
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(
                source=word, target=vocab)

        # sorted by distance
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Volcabulary: ')
        col1.write(vocabs)

        col2.write('Distances: ')
        col2.write(sorted_distances)


if __name__ == '__main__':
    main()
