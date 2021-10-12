# Write a program to process log messages and find total time required to complete the build process.

# datetime [level] message
# Sample Log messages
# 2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s
# 2020-11-30T09:44:09Z [error] When writing to [http://localhost:8086]: Post "http://localhost:8086/write?db=telegraf": dial tcp 127.0.0.1:8086: connect: connection refused
# 2020-11-30T09:44:10Z [warning] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory
# 2020-11-30T09:44:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory
#"2020-11-30T09:44:09Z [error] When writing to ['http://localhost:8086']: Post "http://localhost:8086/write?db=telegraf": dial tcp 127.0.0.1:8086: connect: connection refused",

import time
from datetime import datetime

log_list = [
  '2020-11-30T09:41:10Z [info] Success in plugin: success getting disk io info: open /proc/diskstats: no such file or CASS: Instance Deployment started directory',
  '2020-11-30T09:42:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:43:49Z [info] CASS: Instance Deployment started.',
  '2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s.',
  '2020-11-30T09:44:09Z [error] When writing to ["http://localhost:8086"]: Post "http://localhost:8086": dial tcp 127.0.0.1:8086: connect: connection refused',
  '2020-11-30T09:44:10Z [warning] Error in plugin: warning getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:44:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:45:10Z [info] CASS: Instance Deployment configured.',
  '2020-11-30T09:45:10Z [warning] Warning in plugin: error getting disk io info: open /proc/diskstats: no such file or directory.',
  '2020-11-30T09:45:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:47:10Z [info] Info in plugin: error getting disk io info: open /proc/diskstats: no such file or directory in Instance Deployment',
  '2020-11-30T09:49:10Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:51:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:54:10Z [info] CASS: Instance Deployment complete.',
  '2020-11-30T09:54:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:55:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:57:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory'
]

def get_deployment_time(log_list):
    '''
    processes log messages and finds total time required to complete the build process in Seconds
    '''
    if not isinstance(log_list, list):
        return "Please enter a valid list of logs."

    new_list = []
    for log in log_list:
        dep_start = log.find('Deployment started')
        if dep_start != -1:
            new_list.append(log[:20])

        dep_end = log.find('Deployment complete')
        if dep_end != -1:
            new_list.append(log[:20])

    start_date_time = datetime.fromisoformat(new_list[0][:-1]) #first in the list
    end_date_time = datetime.fromisoformat(new_list[-1][:-1]) #last in the list

    total_time = (end_date_time - start_date_time).total_seconds()
    return total_time

if __name__ == "__main__":
    #running function here
    print(get_deployment_time(log_list))
    
  

