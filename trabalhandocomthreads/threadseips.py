from threading import Thread
# com isso consegue fazer o multithread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {}\n'.format(piloto, trajeto) )
        

t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[2, 'João'])

t_carro1.start()
t_carro2.start()
