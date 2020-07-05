from manager import*
from client import*

bob = Manager()

adam = Client("adam")
adam.set_contact_point(bob.get_secretary())
adam.make_appointment("10:30")

#adam could book? : True

charles = Client("charles")
charles.set_contact_point(bob.get_secretary())
charles.make_appointment("11:30")

#charles could book? : True

dag = Client("dag")
dag.set_contact_point(bob.get_secretary())
dag.make_appointment("10:30")

#dag could book? : False

bob.check_schedule()
{"11:30": "charles", "10:30": "adam"}

'''
    これらのコンポーネントを使うシナリオを 実行させるプログラムは以下となります。

'''
