import os
from utils import loadFiles
from textProcessor import KeyphraseExtractionPipeline


def main():
    # Define output directory
    output_dir = 'data/keywords'
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    text = loadFiles()
    # Load pipeline
    model_name = "ml6team/keyphrase-extraction-kbir-inspec"
    extractor = KeyphraseExtractionPipeline(model=model_name)

    # Divide text into 400-character chunks
    chunks = [text[i:i + 400] for i in range(0, len(text), 400)]

    # Open file before starting the loop
    with open(f'{output_dir}/keywords.txt', 'w') as f:
        for idx, chunk in enumerate(chunks):
            keyphrases = extractor(chunk)

            # Write keyphrases to file
            for phrase in keyphrases:
                f.write("%s\n" % phrase)


if __name__ == "__main__":
    main()
