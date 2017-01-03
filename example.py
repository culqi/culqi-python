import json
from culqi import Culqi

def main():
    culqi = Culqi("INSERTE_SU_LLAVE_PUBLICA","INSERTE_SU_LLAVE_PRIVADA")
    token = json.loads(culqi.createToken(
        "4111111111111111","PEN","123",9,2020,"q352454534","Muro","wmuro@me.com","William"
    ))
    print token["id"]

    plan = json.loads(culqi.createPlan("plan-test-CULQI107",1000,"PEN","day",2,10,"Plan de Prueba CULQI107",50))
    print plan["alias"]

if __name__ == "__main__":
    main()
