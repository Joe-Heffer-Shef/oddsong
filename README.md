# OddSong

OddSong is a birdsong identifier that classifies bird species from audio recordings.

It processes audio through a pipeline: loading and resampling, segmenting into 3-second chunks, computing log-scaled Mel-spectrograms, classifying via a CNN model, and optionally filtering by geographic location and season.

Implementations are available in both **Python** (`oddsong/`) and **R** (`R/`).

## Installation

Install from source using pip:

```bash
git clone https://github.com/Joe-Heffer-Shef/oddsong.git
cd oddsong
pip install .
```

To install in editable mode for development:

```bash
pip install -e .
```

## Usage

### Python

```bash
python -m oddsong
```

### R

```r
source("R/identify.R")
identify("path/to/audio.wav")
```

Supported audio formats: WAV, MP3, FLAC, OGG.

## Pipeline

1. Load audio, resample to 48 kHz
2. Segment into 3-second windows
3. Compute Mel-spectrogram per segment
4. Classify each segment (CNN model → species confidence scores)
5. Filter detections by latitude, longitude, and week of year

## License

See [LICENSE](LICENSE).
