# Dictionary-Based Compression for NewLang (Work in Progress)

Welcome to the dictionary-based compression and decompression algorithm for NewLang, an open-source project designed to minimize code size while maintaining readability. This algorithm is still a work in progress, and we encourage developers to contribute and help improve its performance and efficiency.

## Overview

This project focuses on creating a simple and effective compression format for NewLang code by:

- Replacing repeated words or phrases with shorter keys
- Removing quotes from dictionary items
- Providing an easy-to-use decompression method

The primary goal is to reduce the character count and file size, making NewLang code more efficient to transmit and store.

## Usage

To compress your NewLang code:

1. Identify repeated words or phrases
2. Create a dictionary (`d{}`) containing key-value pairs for each repeated word or phrase
3. Replace words or phrases in the code with their corresponding keys
4. Remove quotes from dictionary items

To decompress the compressed code:

1. Locate the dictionary (`d{}`)
2. Replace keys in the code with their corresponding values from the dictionary

## Contributing

We welcome contributors who share our vision for efficient and readable code compression. If you are interested in contributing to this project, there are many ways to get involved:

- Report bugs or suggest new features through our issue tracker
- Help us refine and optimize the compression and decompression algorithms
- Create documentation, tutorials, and other learning resources

Please note that this project is a work in progress and may undergo significant changes as we collaborate to create a better compression algorithm for NewLang.

Thank you for your interest in this project! We look forward to building a more efficient coding experience together.
