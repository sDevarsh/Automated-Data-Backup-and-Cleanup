from datetime import datetime
import subprocess
import time
import threading
import logging
import schedule
import os
logging.basicConfig(filename='backupLogs.log',
                    format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

cleanup_threshold_days = 7


def backup_files(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = f"{backup_dir}/backup_{timestamp}"

    try:
        # shutil.copytree(source_dir, backup_folder)
        s = subprocess.call(f"cp -r {source_dir} {backup_folder}", shell=True)

        print(f"Backup created at {backup_folder}")
        logger.info(f"Backup created at {backup_folder} with status code {s}")

    except Exception as e:
        print("Error: ", e)


def cleanup_files(source_dir):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    try:
        s = subprocess.call(f"rm -rf {source_dir}", shell=True)

        print(f"Cleanup at {source_dir}")
        logger.info(f"Cleanup conducted at {source_dir} with status code {s}")
    except Exception as e:
        print("Error: ", e)


def task1():
    schedule.every().day.at("09:30:30").do(
        backup_files, source_dir=source_directory, backup_dir=backup_directory)


def task2():
    schedule.every().monday.do(cleanup_files, source_dir=cleanup_folder)


if __name__ == "__main__":

    global source_directory
    global backup_directory
    global cleanup_folder
    source_directory = "./file"
    backup_directory = "./backupFol"
    cleanup_folder = "./backupFol\\backup_2023-08-29_09-53-41"

    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    while True:
        schedule.run_pending()
        time.sleep(1)
