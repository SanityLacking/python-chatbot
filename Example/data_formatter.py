import pandas as pd
import math

class Data_Formatter:
    df = None
    answer_list_english = []
    answer_list_korean = []
    '''
        qa_objects is a list of objects in the following format:
        Each object is made unique by the answer
        {
            AE => "Answer in english (string)",
            AK => "Answer in korean (string)",
            QE => [list_of_english_questions],
            QK => [list_of_korean_questions],
            Keywords => [list_of_keywords]
        }
    '''
    qa_objects = []

    '''
        Initialize the class with the file location
        Loads the csv file and sets up data
    '''
    def __init__(self, file_location):
        self.df = pd.read_csv(file_location)
        self.find_unique_answers()
        self.setup_objects()

    '''
        Finds all unique answers
        stores them in class list:
        answer_list_english
        answer_list_korean
    '''
    def find_unique_answers(self):
        answers_english = self.df['AE']
        answers_korean = self.df['AK']
        for i in range(len(answers_english)):
            if(answers_english[i] not in self.answer_list_english):
                self.answer_list_english.append(answers_english[i])
                self.answer_list_korean.append(answers_korean[i])

    '''
        Given an answer, return all keywords that relate
    '''
    def get_related_keywords(self, answer):
        keywords_unique = []
        keywords = self.df['Keywords']
        answers_english = self.df['AE']
        answers_korean = self.df['AK']
        for i in range(len(answers_english)):
            if(answers_english[i] == answer or answers_korean[i] == answer):
                try:
                    keywords_temp = [x.strip(' ') for x in keywords[i].split(',')]
                    for keyword in keywords_temp:
                        if(keyword not in keywords_unique):
                            keywords_unique.append(keyword)
                except AttributeError:
                    continue
                    #print("Ignored data at row " + str(i) + " in keywords column: " + str(keywords[i]))
        return keywords_unique

    '''
        Given an answer, return all questions that relate
    '''
    def get_related_questions(self, answer):
        questions_e_unique = []
        questions_k_unique = []
        questions_e = self.df['QE']
        questions_k = self.df['QK']
        answers_english = self.df['AE']
        answers_korean = self.df['AK']
        for i in range(len(answers_english)):
            if(answers_english[i] == answer or answers_korean[i] == answer):
                question_e_temp = questions_e[i]
                question_k_temp = questions_k[i]
                if(question_e_temp not in questions_e_unique
                and question_k_temp not in questions_k_unique):
                    questions_e_unique.append(question_e_temp)
                    questions_k_unique.append(question_k_temp)
        return questions_e_unique, questions_k_unique

    '''
        Setup objects in format specified above
    '''
    def setup_objects(self):
        for i in range(len(self.answer_list_english)):
            keywords = self.get_related_keywords(self.answer_list_korean[i])
            q_english, q_korean = self.get_related_questions(self.answer_list_korean[i])
            obj = {
                'AE': self.answer_list_english[i],
                'AK': self.answer_list_korean[i],
                'QE': q_english,
                'QK': q_korean,
                'Keywords': keywords
            }
            self.qa_objects.append(obj)

    '''
        Returns an array in the following format:
        [question, answer, question, answer ... question, answer]

    '''
    def get_training_array(self):
        q_k_arr = []
        q_e_arr = []
        for obj in self.qa_objects:
            for question in obj['QK']:
                q_k_arr.append(question)
                q_k_arr.append(obj['AK'])
            for question in obj['QE']:
                q_e_arr.append(question)
                q_e_arr.append(obj['AE'])
        return q_e_arr, q_k_arr

    '''
        Searches for relevant keywords in entered input
    '''
    def get_answer_with_keywords(self, entered_input):
        for obj in self.qa_objects:
            is_subset = set(obj['Keywords']).issubset([x.strip(' ') for x in entered_input.split(" ")])
            if(is_subset):
                return obj['AE'], obj['AK']
        return "Can you please make your question more specific?", "Can you please make your question more specific?"



if __name__ == "__main__":
    formatter = Data_Formatter("test_data.csv")
    print(formatter.get_training_array()[1])
    #print(formatter.get_training_array())
