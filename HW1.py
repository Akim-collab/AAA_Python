class CountVectorizer():
    
    @staticmethod
    def converting_matrix_into_single_row(matrix):
        lst = []
        for line in matrix:
            lst += line
        return lst
    
    def fit_transform(self, corpus):
        corpus = [text.split() for text in [text.lower() for text in corpus]]
        self.feature_names = list(set(CountVectorizer.converting_matrix_into_single_row(corpus)))
        count_matrix = []
        for i in range(len(corpus)):
            dict_features = dict.fromkeys(self.feature_names, 0)
            for j in range(len(corpus[i])):
                dict_features[corpus[i][j]] += 1
            count_matrix.append(list(dict_features.values()))
        return count_matrix
    
    def get_feature_names(self):
        return self.feature_names



