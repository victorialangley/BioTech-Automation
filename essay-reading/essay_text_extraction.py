"""
essay_text_extraction.py
Author: Victoria Langley
Description: This script extracts text content from essays for further analysis.
"""

import os
import textract

class EssayTextExtractor:
    def __init__(self, essay_directory):
        self.essay_directory = essay_directory

    def extract_text(self):
        extracted_text = []

        for root, _, files in os.walk(self.essay_directory):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".docx"):
                    file_path = os.path.join(root, file)
                    text = self._extract_text_from_file(file_path)
                    extracted_text.append((file, text))

        return extracted_text

    def _extract_text_from_file(self, file_path):
        try:
            text = textract.process(file_path).decode("utf-8")
            return text
        except Exception as e:
            print(f"Error extracting text from {file_path}: {e}")
            return ""

if __name__ == "__main__":
    essays_directory = "essays"
    extractor = EssayTextExtractor(essays_directory)

    extracted_text = extractor.extract_text()

    for essay, text in extracted_text:
        print(f"Essay: {essay}")
        print(f"Extracted Text:\n{text[:300]}...\n")
