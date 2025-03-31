# Snapshot Utility

## Description
A Python-based system monitoring tool that captures CPU, memory, swap usage, and running processes.

## Installation
Clone the repository and install the package:
```bash
git clone https://github.com/bekonRymkhanov/psutil-package.git snapshot-util
cd snapshot-util // or folder where setup.py is located
pip install -U .
```

## Usage

Run the snapshot tool with:

```bash
snapshot -i 1 -n 10 -f output.json
```
Arguments:

-  -i : Interval between snapshots (default: 5 seconds)

-   -n : Number of snapshots to take (default: 20)

-   -f : Output file name (default: snapshot.json)

## Uninstall
```bash
pip uninstall snapshot
```