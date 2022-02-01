
from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

walnut = Pet(name='Walnut', species='dog', photo_url='https://scontent-man2-1.xx.fbcdn.net/v/t39.30808-6/263069466_10158647271822336_1410055865983425887_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeFNAUjYI9np8KhJ7GGN4Y7Dt4llxAoxboK3iWXECjFugi4DIkmU9TepQ758ruhycv0&_nc_ohc=i9J4a7KgEw4AX8Jesyg&_nc_ht=scontent-man2-1.xx&oh=00_AT9KIpHuV2L2mPUdq1e_dxDMdxR4LY_AKJAz87tmo2sFRA&oe=61FDA6BA', age=1, notes='He is a very stinky boy.')
whiskey = Pet(name='Whiskey', species='dog', photo_url='https://scontent-man2-1.xx.fbcdn.net/v/t1.18169-9/13716090_10153790454032336_4008628012791499306_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=cdbe9c&_nc_eui2=AeHwxWd_F8hlI0ThfLhnitRwAwEiTboaL2ADASJNuhovYA_LHYo4fBLRXdCz8tzgRz4&_nc_ohc=T7QgtCeuB_oAX-Hep5I&_nc_ht=scontent-man2-1.xx&oh=00_AT-4PeBfVSPY34SIrBAhmktNCOx_adHep_5QSlZG1f-drA&oe=621D5FB2', age='6', notes='Sweet boy who loves bunnies.')
fluffy = Pet(name='Fluffy', species='cat', age=3, notes='Loves to play.')
carrot = Pet(name='Carrot', species='bunny', photo_url='https://static9.depositphotos.com/1008280/1125/i/600/depositphotos_11250610-stock-photo-rabbit.jpg', age=5, notes = 'She loves veggies.')
spike = Pet(name='Spike', species='hedgehog', photo_url='https://www.thesprucepets.com/thmb/nuRZVBLSTh8yjg7Z6ATVnQZ2vLU=/1927x1445/smart/filters:no_upscale()/GettyImages-626916125-5b3a4a8046e0fb00379f682d.jpg', age=2, notes='Has a prickly side.')

db.session.add_all([walnut, whiskey, fluffy, carrot, spike])
db.session.commit()