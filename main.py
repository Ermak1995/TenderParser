import argparse
import csv

from parser import parse_tenders



def save_to_csv(tenders, path='tenders.csv'):
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=tenders[0].keys())
        writer.writeheader()
        writer.writerows(tenders)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max', type=int, default=100)
    parser.add_argument('--output', type=str, default='tenders.csv')
    args = parser.parse_args()

    tenders = parse_tenders(args.max)
    save_to_csv(tenders, args.output)

    print(f"Saved {len(tenders)} tenders to {args.output}")


if __name__ == "__main__":
    main()
