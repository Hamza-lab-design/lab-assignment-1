"""
RECORD CHECK  -  my version
===========================

Name  : hamza
Lane  :  AI /     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
hostname = input("Enter hostname: ")
gb_used = float(input("Enter GB used: "))
gb_total = float(input("Enter GB total: "))

gb_free = gb_total - gb_used
percent_used = gb_used / gb_total * 100

percent_free = gb_free / gb_total * 100

border = "=" * 35
print(border)
print(f" RECORD CHECK - {hostname}")
print(border)
print(f" {'Used':<12}; {gb_used:>10.2f}")
print(f" {'Total':<12}: {gb_total:>10.2f}")
print(f" {'Free':<12}: {gb_free:>10.2f}")
print(f" {'Percent Used':<12}: {percent_used:>10.2f}%")
print(f" {'Percent Free':<12}: {percent_free:>10.2f}%")




#

