from legal_doc_processing.utils import (
    _if_not_pipe,
    _ask,
)


def predict_nature_of_violations(feature, nlpipe=None):
    return [("--None--", -1)]