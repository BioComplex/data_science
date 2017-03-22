import pandas as pd
import numpy as np


class CoOcurrence(object):
    @staticmethod
    def get_ocurrence(df, ocurrence_id, entity_id, ocurrence_set, entity_set ):
        df = df.groupby([ocurrence_id, entity_id], as_index=True).agg('count')
        df['score'] = 1
        df = df.reset_index()[[ocurrence_id, entity_id, 'score']]

        df = CoOcurrence.replicate_entities(df, ocurrence_id=ocurrence_id, entity_id=entity_id,
                                            ocurrence_set=ocurrence_set, entity_set=entity_set)
        return df

    @staticmethod
    def get_cooccurence(df, min_occurences=0, min_entities=0):
        C = np.array(df).reshape(len(ocurrence_set), len(entity_set))

        C[:, np.sum(C, axis=0) <= min_occurences] = 0
        C = C[np.sum(C, axis=1) >= min_entities, :]
        CC = C.T.dot(C) * 1.
        return C, CC


    @staticmethod
    def replicate_entities(df, ocurrence_id, entity_id, ocurrence_set, entity_set):

        df = df.groupby([ocurrence_id, entity_id], as_index=True).agg('count')
        df['score'] = 1
        df = df.reset_index()[[ocurrence_id, entity_id, 'score']]

        return pd.DataFrame({ocurrence_id: np.append(df[ocurrence_id], np.repeat(ocurrence_set, len(entity_set))),
                             entity_id: np.append(df[entity_id], np.tile(entity_set, len(ocurrence_set))),
                             'score': np.append(df.score, len(entity_set) * len(ocurrence_set) * [0])}).groupby(
            [ocurrence_id, entity_id]).agg({'score': 'sum'})


ocurrence_id = "ocurrence"
entity_id = "entity"
ocurrence_set = ['o1', 'o1', 'o1', 'o2', 'o2', 'o3']
entity_set = ['e1', 'e2', 'e2', 'e2', 'e3', 'e4']

df = pd.DataFrame({ocurrence_id: ocurrence_set, entity_id: entity_set})

ocurrence_set = np.unique(['o1', 'o1', 'o1', 'o2', 'o2', 'o3'])
entity_set = np.unique(['e1', 'e2', 'e2', 'e2', 'e3', 'e4'])



df_ocurrence = CoOcurrence.get_ocurrence(df, ocurrence_id, entity_id, ocurrence_set, entity_set)

C, CC = CoOcurrence.get_cooccurence(df_ocurrence)