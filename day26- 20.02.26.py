
syslog="""
Feb 20 10:15:32 web-server sshd[12345]: Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2
Feb 20 10:16:01 web-server CRON[12350]: pam_unix(cron:session): session opened for user root by (uid=0)
Feb 20 10:16:01 web-server CRON[123512310]: pam_unix(cron:session): session opened for user shoot by (uid=0)
Feb 20 10:16:01 web-server CRON[23112]: pam_unix(cron:session): session opened for user big_man by (uid=0)
Feb 20 10:16:01 web-server CRON[212]: pam_unix(cron:session): session opened for user hacker by (uid=0)
Feb 20 10:16:02 web-server systemd[1]: Starting Daily rotation of log files...
Feb 20 10:16:05 web-server kernel: [1234.567890] EXT4-fs (sda1): mounted filesystem with ordered data mode.
"""

import re
import sys

# (\[[\d]*\])
# \[([\d]*)\]
# with open ('syslog.txt','w') as f:
#     f.write(syslog)
# CRON jobs = used to schedule scripts
# def show_time_of_pid(line):
#   pattern = r'^([\w\d :_]*)(?=computer).*\[([\d]*)\]'
#   result = re.search(pattern, line)
#   return result[1],result[2]

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

  # output --> CRON[12350] || user root 
# with open ('syslog.txt') as f:
#     pattern = r'(CRON\[\d*\])(.*)(user [\w]* )'
#     for line in f:
#         if 'CRON' not in line:
#            # print('next')
#             continue
#         #print(line.strip())
#         result = re.search(pattern=pattern,string=line)
#         print(result[1],'||', result[3])

