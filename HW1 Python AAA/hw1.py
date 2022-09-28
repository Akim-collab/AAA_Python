from typing import List


class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.

    ...

    Attributes
    ----------
    corpus : List[str]
        A collection of text documents

    Methods
    -------
    converting_matrix_into_single_row(matrix: List[List[str]]) -> List[str]:
        Moving from lists of lists from one row to a list of these rows.

    fit_transform(self, corpus: List[List[str]]) -> List[int]:
        Accepts a text corpus and returns a term-document matrix.

    get_feature_names(self) -> List[str]:
        Returns a list of features (unique words from the corpus).
    """

    @staticmethod
    def converting_matrix_into_single_row(matrix: List[List[str]]) -> List[str]:
        """
        Moving from lists of lists to a list.

        Parameters
        ----------
        matrix : List[List[str]]

        Returns
        -------
        lst : List[str]
        """
        lst = []
        for line in matrix:
            lst += line
        return lst

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Accepts a text corpus and returns a term-document matrix.

        Parameters
        ----------
        corpus: List[List[str]]
            Text corpus

        Returns
        -------
        count_matrix : List[List[int]]
            A term-document matrix
        """
        corpus = [text.split() for text in [text.lower() for text in corpus]]
        self.feature_names = list(set(CountVectorizer.converting_matrix_into_single_row(corpus)))
        count_matrix = []
        for text in corpus:
            dict_features = dict.fromkeys(self.feature_names, 0)
            for word in text:
                dict_features[word] += 1
            count_matrix.append(list(dict_features.values()))
        return count_matrix

    def get_feature_names(self) -> List[str]:
        """
        Returns a list of features (unique words from the corpus).

        Returns
        -------
        feature_names : List[str]
            A list of features (unique words from the corpus)
        """
        return self.feature_names


if __name__ == '__main__':
    pass
