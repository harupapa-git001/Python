from secretary import*

class Manager:
    def __init__(self):
        self.sara = Secretary()
        
    def check_schedule(self):
        schedule = self.sara.get_schedule()
        print(schedule)
        
    def get_secretary(self):
        return self.sara

'''
    次にManagerのコードです。Managerはアポイントの確認機能があります。また、クライアントにたいして秘書を渡す機能もあります。

'''
