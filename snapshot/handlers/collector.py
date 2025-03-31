import time
import psutil

class SnapshotCollector:
    """Handles system snapshot collection."""

    def collect(self):
        """Collects system stats."""
        cpu_times = psutil.cpu_times_percent(interval=1)
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return {
            "Tasks": self.get_task_summary(),
            "%CPU": {"user": cpu_times.user, "system": cpu_times.system, "idle": cpu_times.idle},
            "KiB Mem": {"total": mem.total//1000, "free": mem.free//1000, "used": mem.used//1000},
            "KiB Swap": {"total": swap.total//1000, "free": swap.free//1000, "used": swap.used//1000},
            "Timestamp": int(time.time())
        }

    def get_task_summary(self):
        total, running, sleeping, stopped, zombie = 0, 0, 0, 0, 0

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
