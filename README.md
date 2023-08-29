# Automated-Data-Backup-and-Cleanup
 Python application that performs periodical backup and clean up of data files from a specific directory.
 
 Data Backup:
 Copy all files from a source directory to a backup directory at a specific interval (e.g., daily).
 Use the subprocess module to execute the necessary shell commands for copying files.
 
 Data Cleanup:
 Delete files older than a certain number of days from the source directory to save space.
 Use the subprocess module to execute shell commands for file deletion.
 
 Logging:		
 Log the backup and cleanup operations along with timestamps to a log file.
 Use the logging module to create and manage logs.	
 
 Scheduling:
 Schedule the backup and cleanup tasks to run automatically daily at 2 PM.
 Use the schedule module to set up the desired scheduling intervals.
 	
 Threading:
 Perform the backup and cleanup tasks concurrently using threads.
 Use the threading module to manage multiple tasks simultaneously.
