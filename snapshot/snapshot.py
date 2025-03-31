import argparse
import os
import time
import json
from snapshot.handlers.collector import SnapshotCollector
from snapshot.handlers.writer import SnapshotWriter

def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=5)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Number of snapshots to take", type=int, default=20)
    args = parser.parse_args()

    if args.n == 0:
        exit()

    if os.path.exists(args.f):
        os.remove(args.f)

    collector = SnapshotCollector()
    writer = SnapshotWriter(args.f)

    for _ in range(args.n):
        data = collector.collect()
        writer.write(data)

        os.system('clear')
        print(data, end="\r")	

        time.sleep(args.i)

if __name__ == "__main__":
    main()
