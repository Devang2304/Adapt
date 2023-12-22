
---

# [SyncPulse](https://pypi.org/project/SyncPulse/)


SyncPulse is a versatile CLI tool designed to simplify various file conversions and tasks. Whether you need to convert documents from one format to another, download YouTube videos or transcripts, or even convert text to speech, SyncPulse has you covered.

## Installation

```bash
pip install SyncPulse
```

## Usage

```bash
SyncPulse help
Usage: SyncPulse conversion_type input_path output_path
Valid conversion types: docx_to_pdf, pdf_to_docx, download_video of youtube, download_transcript of youtube, text_to_speech
```

### Examples

1. Convert DOCX to PDF:
    ```bash
    SyncPulse docx_to_pdf input.docx output.pdf
    ```

2. Convert PDF to DOCX:
    ```bash
    SyncPulse pdf_to_docx input.pdf output.docx
    ```

3. Download video from YouTube:
    ```bash
    SyncPulse download_video youtube_video_url output_path
    ```

4. Download transcript from YouTube:
    ```bash
    SyncPulse download_transcript youtube_video_url output_path
    ```

5. Text to Speech:
    ```bash
    SyncPulse text_to_speech "Hello, world!" output.mp3
    ```

## Project Description

SyncPulse aims to streamline common tasks by providing a user-friendly command-line interface for various conversions. It leverages popular libraries such as docx2pdf, pdf2docx, pytube, youtube_transcript_api, gtts, and pyfiglet to deliver seamless functionality.

## Contributing

Contributions are welcome! Please create issue if you have any idea and want to contribute

## License

This project is licensed under the MIT License

## Acknowledgments

Special thanks to the developers of the libraries that make SyncPulse possible.

## Contact

Devang Vartak - devangvartak2304@gmail.com

Project Link: [https://github.com/Devang2304/SyncPulse](https://github.com/Devang2304/SyncPulse)

---
