# ddr.py
## Simple python script to use cheap aliexpress usb ddr mats as OSC controllers.

Example mat:
https://de.aliexpress.com/item/1005007560164286.html?spm=a2g0o.productlist.main.1.a754uQSUuQSUWy&algo_pvid=60c2640e-3037-4a37-83f6-f8e7339fba2a&algo_exp_id=60c2640e-3037-4a37-83f6-f8e7339fba2a-0&pdp_npi=4%40dis%21EUR%2116.54%2113.72%21%21%21125.18%21103.83%21%40211b813f17304949406132139e3457%2112000041295561236%21sea%21AT%210%21ABX&curPageLogUid=swWXsZmiVvwB&utparam-url=scene%3Asearch%7Cquery_from%3A

Made using evdev and python-osc libraries:
https://python-evdev.readthedocs.io/en/latest/
https://python-osc.readthedocs.io/en/latest/

Default ip and port are localhost:8000, but you can change them running the script like this:
python ddr.py 192.168.0.23 7575 (ip and port)
