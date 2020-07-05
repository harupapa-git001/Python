class Secretary:
    def __init__(self):
        self.appointment = {}
        
    def request_appointment(self, when, who):
        
        if(when in self.appointment):
            return False
        
        else:
            self.appointment[when] = who
            return True
            
    def get_schedule(self):
        return str(self.appointment)

'''
    まず秘書のSecretaryクラスです。
    アポイントの管理は今回の本質ではないので、辞書型を使ってキーに時間(文字列)、バリューに誰という形でアポイントを管理しています。
    同じ時間を別の客に指定された(既に同じキーが存在する)ときだけFalse(アポイントを取れない)を返して、そうでなければTrue(アポイントを取れた)を返し、アポイント管理の辞書データを更新します。
    
    これを request_appointmentメソッドとして実装します。
    そしてマネージャーがアポイントを確認するための get_scheduleメソッドを作成し、その辞書データを文字列として返しています。
    
'''
