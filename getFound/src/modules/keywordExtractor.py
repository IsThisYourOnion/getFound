from transformers import (
    TokenClassificationPipeline,
    AutoModelForTokenClassification,
    AutoTokenizer,
)
from transformers.pipelines import AggregationStrategy
import numpy as np
from getFound.src.utils.utils import DataManager, clean_text



# Define keyphrase extraction pipeline

'''using KBIR despite it being fine tuned on scientific docs. works quite well on job descriptions. '''
class KeyphraseExtractionPipeline(TokenClassificationPipeline):
    def __init__(self, model, *args, **kwargs):
        super().__init__(
            model=AutoModelForTokenClassification.from_pretrained(model),
            tokenizer=AutoTokenizer.from_pretrained(model),
            *args,
            **kwargs
        )

    def postprocess(self, all_outputs):
        results = super().postprocess(
            all_outputs=all_outputs,
            aggregation_strategy=AggregationStrategy.SIMPLE,
        )
        return np.unique([result.get("word").strip() for result in results])



def keywords():
    # Load pipeline
    model_name = "ml6team/keyphrase-extraction-kbir-inspec"
    extractor = KeyphraseExtractionPipeline(model=model_name)
    manager = DataManager()
    text = manager.read_data('raw_job_text', 'txt', False)
    phrases = []
    combined_string = ' '.join(text)
    cleaned_combined_string = clean_text(combined_string)
    chunks = [cleaned_combined_string[i:i + 400] for i in range(0, len(cleaned_combined_string), 400)]
    for idx, chunk in enumerate(chunks):
        keyphrases = extractor(chunk)
        for phrase in keyphrases:
            phrases.append(phrase)
    manager.write_data('job_keywords', 'extracted_keywords', 'txt', phrases)

