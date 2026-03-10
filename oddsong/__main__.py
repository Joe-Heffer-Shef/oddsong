import argparse
import oddsong.song


def main():
    parser = argparse.ArgumentParser(
        prog="oddsong",
        description="Identify bird species from audio recordings.",
    )
    parser.add_argument(
        "audio_file",
        help="Path to an audio file (WAV, MP3, FLAC, or OGG).",
    )
    parser.add_argument(
        "--latitude",
        type=float,
        help="Observer latitude in decimal degrees for location filtering.",
    )
    parser.add_argument(
        "--longitude",
        type=float,
        help="Observer longitude in decimal degrees for location filtering.",
    )
    parser.add_argument(
        "--week",
        type=int,
        choices=range(1, 49),
        metavar="WEEK",
        help="Week of year (1–48) for seasonal filtering.",
    )

    args = parser.parse_args()
    species = oddsong.song.identify(args.audio_file)
    print(species)


if __name__ == "__main__":
    main()
