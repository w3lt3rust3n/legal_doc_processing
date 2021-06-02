import os
import pytest

from tests.funct.utils import (
    make_features_dataframe,
    make_labels_dataframe,
    features_root,
    labels_root,
    accuracy,
)

import legal_doc_processing as ldp
from legal_doc_processing.utils import make_dataframe


class TestDataFrame:
    def test_build(self):
        """ """

        make_dataframe(n=10)