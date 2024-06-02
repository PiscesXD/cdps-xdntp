import ntplib
import time

class NTP():
    def __init__(self , url = None):
        self.url = url

    def get_server_ntp(self,url):
        try:
            client = ntplib.NTPClient()
            response = client.request(url)
            return response.tx_time
        except Exception as e:
            raise ValueError(f"無法連接到NTP伺服器: {self.url} | 錯誤 : {e}")
        
    def torrance(self):
        if self.url is not None:
            local_time = time.time()
            ntp_time = self.get_server_ntp(self.url)
            return local_time - ntp_time
        else:
            raise ValueError("請填入NTP伺服器網址")
