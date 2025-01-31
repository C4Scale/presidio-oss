from typing import Iterator

import pytest

from presidio_analyzer.nlp_engine import SpacyNlpEngine


def test_simple_process_text(spacy_nlp_engine):
    nlp_artifacts = spacy_nlp_engine.process_text("simple text", language="en")
    assert len(nlp_artifacts.tokens) == 2
    assert not nlp_artifacts.entities
    assert nlp_artifacts.lemmas[0] == "simple"
    assert nlp_artifacts.lemmas[1] == "text"


def test_process_batch_strings(spacy_nlp_engine):
    nlp_artifacts_batch = spacy_nlp_engine.process_batch(
        ["simple text", "simple text"], language="en"
    )
    assert isinstance(nlp_artifacts_batch, Iterator)
    nlp_artifacts_batch = list(nlp_artifacts_batch)

    for text, nlp_artifacts in nlp_artifacts_batch:
        assert text == "simple text"
        assert len(nlp_artifacts.tokens) == 2


def test_nlp_not_loaded_value_error():
    unloaded_spacy_nlp = SpacyNlpEngine()
    with pytest.raises(ValueError):
        unloaded_spacy_nlp.process_text(
            "This should fail as the NLP model isn't loaded", language="en"
        )


def test_validate_model_params_missing_fields():
    model = {"lang_code": "en", "model_name": "en_core_web_lg"}

    for key in model.keys():
        new_model = model.copy()
        del new_model[key]

        with pytest.raises(ValueError):
            SpacyNlpEngine._validate_model_params(new_model)
