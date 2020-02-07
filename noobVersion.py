import requests
import json
from time import sleep


def makeRequest(stop):
    response = ''
    try:#comprueba si se puede establecer conexión con la API
        req = requests.get('http://api.interurbanos.welbits.com/v1/stop/' + stop)
        if req.text.find('error') == -1:#comprueba si la parada existe
            if len(json.loads(req.content.decode('utf8'))['lines']) > 0:#comprueba si hay buses
                for line in json.loads(req.content.decode('utf8'))['lines']:#lista todos los buses
                    if line['lineBound'] == 'A Madrid (Intercanbiador De Moncloa)':#detecta si van a moncloa
                        try: 
                            if line['waitTime'].split(' ')[1] == 'min':
                                if line['waitTime'].split(' ')[0] == '1':
                                    response += 'Queda ' + line['waitTime'].split(' ')[0] + ' minuto\n'
                                
                                else:
                                    response += 'Quedan ' + line['waitTime'].split(' ')[0] + ' minutos\n'#minutos restantes

                        except:
                            response += 'Próximo bus: ' + line['waitTime'] + '\n'#Hora de llegada

            else:
                response = 'No hay buses'

        else:
            response = 'No existe la parada'

    except:
        response = 'No se pudo establecer conexión.'
    
    return response

if __name__ == "__main__":
    while True:
        print(makeRequest('20647'))
        sleep(30)
