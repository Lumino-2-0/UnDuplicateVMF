# UnDuplicateVMF

> Remove duplicated brushes from Source Engine VMF maps in seconds.

A simple Python utility that removes duplicated brushes from a Source Engine `.vmf` map file.

This tool was created after a Hammer / Hammer++ crash duplicated hundreds (or even thousands) of brushes directly on top of each other, making map editing nearly impossible.

## Features

- Detects duplicated `solid` blocks
- Ignores VMF object IDs when comparing brushes
- Removes exact duplicate brushes automatically
- Creates a cleaned VMF file
- Works with large Source Engine maps
- No external dependencies required

## Use Case

Imagine opening your map after a crash and noticing:

- Every wall appears twice
- Every brush exists in duplicate
- Pressing `PgUp` / `PgDn` cycles through identical objects
- Deleting a brush reveals another one underneath

This tool is designed to fix exactly that situation.

## Requirements

- Python 3.8+

## Installation

Clone the repository:

```bash
git clone https://github.com/Lumino-2-0/UnDuplicateVMF.git
cd UnDuplicateVMF
```

## Usage

Place your VMF file next to the script and edit the filenames if necessary:

```python
INPUT_VMF = "de_school.vmf"
OUTPUT_VMF = "de_school_clean.vmf"
```

Run:

```bash
python vmf_deduplicate.py
```

Example output:

```text
Duplicated solids removed: 1702
Output file created: de_school_clean.vmf
```

## How It Works

The script:

1. Parses all VMF `solid` blocks.
2. Removes brush IDs from comparison.
3. Generates a hash signature for each brush.
4. Keeps the first occurrence.
5. Removes subsequent identical duplicates.
6. Writes a cleaned VMF file.

## Example

Before:

```text
Wall A
Wall A (duplicate)
```

After:

```text
Wall A
```

## Warning

Always keep a backup of your original VMF before running the tool.

Although the script is designed to be safe, map corruption can occur if your VMF contains unusual structures or intentionally duplicated geometry.

## Supported Editors

- Hammer (++) Editor
- Most Source Engine VMF files (SDK 2013)

## License

MIT License

## Contributing

Pull requests, bug reports and improvements are welcome.

If you encounter a VMF that is not cleaned correctly, feel free to open an issue and attach a sample file.
