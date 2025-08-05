from transformers import BartTokenizer, BartForConditionalGeneration
import torch

class TextSummarizer:
    def __init__(self, model_name='facebook/bart-large-cnn'):
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text, max_length=130, min_length=30, do_sample=False):
        inputs = self.tokenizer.batch_encode_plus(
            [text],
            max_length=1024,
            return_tensors='pt',
            truncation=True
        )
        summary_ids = self.model.generate(
            inputs['input_ids'],
            num_beams=4,
            max_length=max_length,
            min_length=min_length,
            early_stopping=True,
            do_sample=do_sample
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
