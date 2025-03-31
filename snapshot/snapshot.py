"""
Make snapshot

{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
"""
import argparse
import json
import os
import time
import psutil

class Snapshot:
    """Handles system snapshot collection."""
    
    def __init__(self):
        self.snapshot = {
            "Tasks": {},
            "%CPU": {"user": 0, "system": 0, "idle": 0},
            "KiB Mem": {"total": 0, "free": 0, "used": 0},
            "KiB Swap": {"total": 0, "free": 0, "used": 0},
            "Timestamp": 0
        }
    def get_task_summary(self):
        total = 0
        running = 0
        sleeping = 0
        stopped = 0
        zombie = 0

        for proc in psutil.process_iter(attrs=['status']):
            total += 1
            status = proc.info['status']

            if status == psutil.STATUS_RUNNING:
                running += 1
            elif status == psutil.STATUS_SLEEPING:
                sleeping += 1
            elif status == psutil.STATUS_STOPPED:
                stopped += 1
            elif status == psutil.STATUS_ZOMBIE:
                zombie += 1

        return {
                "total": total,
                "running": running,
                "sleeping": sleeping,
                "stopped": stopped,
                "zombie": zombie
        }
    def collect(self):
        self.snapshot["Tasks"] = self.get_task_summary()

        self.snapshot["%CPU"]["user"] = psutil.cpu_times().user
        self.snapshot["%CPU"]["system"] = psutil.cpu_times().system
        self.snapshot["%CPU"]["idle"] = psutil.cpu_times().idle

        self.snapshot["KiB Mem"]["total"] = psutil.virtual_memory().total
        self.snapshot["KiB Mem"]["free"] = psutil.virtual_memory().free
        self.snapshot["KiB Mem"]["used"] = psutil.virtual_memory().used

        self.snapshot["KiB Swap"]["total"] = psutil.swap_memory().total
        self.snapshot["KiB Swap"]["free"] = psutil.swap_memory().free
        self.snapshot["KiB Swap"]["used"] = psutil.swap_memory().used

        self.snapshot["Timestamp"] = int(time.time())
        return self.snapshot


def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=5)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output",type=int, default=20)
    args = parser.parse_args()


    if args.n == 0:
        exit()
    if os.path.exists(args.f):
        os.remove(args.f)
    snapshot_tool = Snapshot()
    while True:
        if args.n == 0:
            break
        else:
            args.n -= 1    
        

        with open(args.f,"a") as file:
            json.dump(snapshot_tool.collect(), file)
            file.write("\n")
            
        os.system('clear')
        print(snapshot_tool.collect(), end="\r")	
        time.sleep(args.i)


if __name__ == "__main__":
    main()
