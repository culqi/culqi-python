import json
from culqi import Culqi

def main():
    culqi = Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")
    data = json.loads(culqi.createToken(
        "4111111111111111","PEN","123",9,2020,"q352454534","Muro","wmuro@me.com","William"
    ))
    print data["id"]

if __name__ == "__main__":
    main()
